import json
import googletrans
import os
import threading
from typing import List, Dict
import redis
import sys, traceback

USE_GOOGLE_TRANSLATE = os.environ.get("USE_GOOGLE_TRANSLATE", "true").lower() == "true"
CACHE_ROOT_PATH = os.environ.get("TRANSLATE_CACHE_DIR", "./cache/")
USE_REDIS_CACHE = os.getenv("USE_REDIS_CACHE", "false").lower() == "true"


class Translate(object):
    def __init__(
            self,
            src="en",
            dest="zh-cn",
            enable_google_translate=USE_GOOGLE_TRANSLATE,
            redis_host_port="127.0.0.1:6379",

    ):
        self.lang_dir = os.path.join(CACHE_ROOT_PATH, f"{src}_{dest}")
        if not os.path.exists(self.lang_dir):
            os.mkdir(self.lang_dir)

        self.google_dir = os.path.join(self.lang_dir, "google")
        if not os.path.exists(self.google_dir):
            os.mkdir(self.google_dir)

        self.google_cache_file = os.path.join(self.google_dir, f"google_cache_{src}_{dest}.json")

        # print(googletrans.LANGUAGES)
        self.enable_google_translate = enable_google_translate
        print(f"Enable google translate: {self.enable_google_translate}")
        self.translator = googletrans.Translator()
        self.google_cache_changed = False
        self.lang_src = src
        self.lang_dest = dest

        self.redis_key = os.path.split(CACHE_ROOT_PATH)[-1]
        self.redis = self.redis_host = self.redis_port = None
        if redis_host_port is not None:
            self.redis_host, self.redis_port = redis_host_port.split(":")
            self.redis_port = int(self.redis_port)

        self.lock = threading.Lock()
        self.cache = {"": ""}
        self.google_cache = self._load_google_cache()
        self.cache.update(self.google_cache)

        print(f"Using redis cache: {USE_REDIS_CACHE}")

        if USE_REDIS_CACHE:
            self.redis = redis.Redis(host=self.redis_host, port=self.redis_port)
            redis_result = self._load_redis_cache()
            print(f"Loaded {len(redis_result)} translations from redis")

            self.cache.update(redis_result)

        self.cache.update(self._load_csv_cache())
        self.cache.update(self._load_txt_cache())

        # self.cache = self._fix_cache(self.cache)
        print(f"Loaded {len(self.cache)} translations cache")

    @staticmethod
    def _fix_cache(cache: Dict[str, str]) -> Dict[str, str]:
        new_cache = {}
        for k, v in cache.items():
            if k != v:
                new_cache.update({k.strip(): v.strip()})
        return new_cache

    def _load_redis_cache(self):
        data = self.redis.hgetall(self.redis_key)

        rdict = {k.decode("utf8"): v.decode("utf8") for k, v in data.items()}
        return rdict

    def _load_google_cache(self):

        if not os.path.exists(self.google_cache_file):
            with open(self.google_cache_file, "w+", encoding="UTF-8") as f:
                f.write("{}")
        if not os.path.exists(self.google_cache_file):
            return {}
        for fn in os.listdir(self.google_dir):
            with open(os.path.join(self.google_dir, fn), encoding="UTF-8") as f:
                cache = json.load(f)
            print(f"Loaded {len(cache)} from {fn}")
        return cache

    def _load_csv_cache(self):
        input_path = os.path.join(self.lang_dir, "csv")
        cache = {}
        for fn in os.listdir(input_path):
            if not fn.endswith(".csv"):
                continue

            with open(os.path.join(input_path, fn), encoding="UTF-8") as f:
                lines = f.readlines()
                print(f"Loading {fn}...{len(lines)}")
                for line in lines:
                    line = line.strip().split(",")
                    if len(line) != 2:
                        continue
                    cache.update({self._fix_tags(line[0]): line[1].strip()})
        print(f"Loaded {len(cache)} translations from csv files")
        return cache

    @staticmethod
    def _fix_tags(text: str) -> str:
        text = text.replace("_", " ").strip()
        return text

    def _load_txt_cache(self):
        input_path = os.path.join(self.lang_dir, "txt")
        cache = {}
        for root, dirs, files in os.walk(input_path):
            for fn in files:
                if not fn.endswith(".txt"):
                    continue

                with open(os.path.join(root, fn), encoding="UTF-8") as f:
                    lines = f.readlines()
                    print(f"Loading {fn}...{len(lines)}")
                    for line in lines:
                        line = line.strip().split("=")
                        if len(line) != 2:
                            continue
                        cache.update({self._fix_tags(line[0]): line[1].strip()})
        print(f"Loaded {len(cache)} translations from txt files")
        return cache

    def google_translate(self, txt: str, src="en", dest="zh-cn") -> str | List[str] | None:

        if not self.enable_google_translate:
            return None

        if isinstance(txt, list) and len(txt) == 0:
            return []

        if isinstance(txt, str) and len(txt) == 0:
            return ""

        try:
            # print(f"google: {txt} {src} {dest}")
            result = self.translator.translate(txt, src=src, dest=dest)

            print(f"google text: {txt} -> {result.text}")
            return result.text
        except Exception as e:
            traceback.print_exc(file=sys.stdout)
            print(e)
            return None

    def translate(self, txt: str | List[str]) -> str | List[str] | None:
        if self.lang_src == self.lang_dest:
            return txt

        if txt is None:
            return None

        if isinstance(txt, list):
            return [self._translate(t) for t in txt]
        return self._translate(txt)

    def _translate(self, txt: str) -> str | None:
        txt = self._fix_tags(txt)
        if txt in self.cache:
            return self.cache[txt]

        result = self.google_translate(txt, self.lang_src, self.lang_dest)
        if result is not None:

            if self.redis is not None:
                self.redis.hset(self.redis_key, mapping={txt: result})

            with self.lock:
                self.cache.update({txt: result})
                self.google_cache.update({txt: result})
                self.google_cache_changed = True

        return result

    def dump_cache(self, indent=4) -> str:
        return json.dumps(self.cache, ensure_ascii=False, indent=indent)

    def save_cache(self):
        if not self.google_cache_changed:
            return

        if self.redis is not None:
            self.redis.hset(self.redis_key, mapping=self.google_cache)

        with self.lock:
            with open(self.google_cache_file, "w+", encoding="UTF-8") as f:
                f.write(json.dumps(self.google_cache, ensure_ascii=False, indent=4))
            print(f"Saved {len(self.google_cache)} to {self.google_cache_file}...")
            self.google_cache_changed = False


if __name__ == '__main__':
    t = Translate('en', 'zh-cn')
    # print(t.translate("1girl"))
    # print(t.translate("hello"))
    print(t.translate(["hello world jj", "say goodbye"]))
    t.save_cache()
