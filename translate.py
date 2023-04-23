import json
import googletrans
import os
import threading

CACHE_ROOT_PATH = "./cache/"


class Translate(object):

    def __init__(self, src="en", dest="zh-cn", enable_google_translate=True):
        self.lang_dir = os.path.join(CACHE_ROOT_PATH, f"{src}_{dest}")
        if not os.path.exists(self.lang_dir):
            os.mkdir(self.lang_dir)

        self.google_dir = os.path.join(self.lang_dir, "google")
        if not os.path.exists(self.google_dir):
            os.mkdir(self.google_dir)

        self.google_cache_file = os.path.join(self.google_dir, f"google_cache_{src}_{dest}.json")

        print(googletrans.LANGUAGES)
        self.enable_google_translate = enable_google_translate
        self.translator = googletrans.Translator()
        self.google_cache_changed = False
        self.lang_src = src
        self.lang_dest = dest
        self.lock = threading.Lock()
        self.cache = {}
        self.google_cache = self.load_google_cache()
        self.cache.update(self.google_cache)
        self.cache.update(self.load_csv_cache())
        self.cache.update(self.load_txt_cache())
        print(f"Loaded {len(self.cache)} translations")

    def load_google_cache(self):

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

    def load_csv_cache(self):
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
                    cache.update({self.fix_tags(line[0]): line[1].strip()})
        print(f"Loaded {len(cache)} translations from csv files")
        return cache

    @staticmethod
    def fix_tags(text: str) -> str:
        text.replace("_", " ").strip()
        return text

    def load_txt_cache(self):
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
                        cache.update({self.fix_tags(line[0]): line[1].strip()})
        print(f"Loaded {len(cache)} translations from txt files")
        return cache

    def google_translate(self, txt, src="en", dest="zh-cn"):
        if not self.enable_google_translate:
            return None
        try:
            result = self.translator.translate(txt, src=src, dest=dest)
            print(f"google: {txt} -> {result.text}")
            return result.text
        except Exception as e:
            print(e)
            return None

    def translate(self, txt: str) -> str | None:
        if txt in self.cache:
            return self.cache[txt]

        result = self.google_translate(txt, self.lang_src, self.lang_dest)
        if result is not None:
            with self.lock:
                self.cache.update({txt: result})
                self.google_cache.update({txt: result})
                self.google_cache_changed = True
        return result

    def save_cache(self):

        if not self.google_cache_changed:
            return

        with self.lock:
            with open(self.google_cache_file, "w+", encoding="UTF-8") as f:
                f.write(json.dumps(self.google_cache, ensure_ascii=False, indent=4))
            self.google_cache_changed = False


if __name__ == '__main__':
    t = Translate('en', 'zh-cn')
    print(t.translate("1girl"))
    print(t.translate("hello"))
    t.save_cache()
