import json
import copy
from translate import Translate


def translate_json():
    translator = Translate(src="en", dest="zh-cn")

    with open("./data/danbooru-tags.json", encoding="UTF-8") as f:
        tags = json.load(f)
    print(f"Loaded {len(tags)} tags")
    count = 0
    for tag in tags:
        tag_name = copy.copy(tag["name"]).replace("_", " ")
        text = translator.translate(tag_name)
        print(f"Translated {tag['name']} -> {text}")
        count += 1
        if count % 10 == 0:
            translator.save_cache()
        if text is not None:
            tag["zh_cn"] = text
        else:
            tag["zh_cn"] = ""
    with open("./data/danbooru-tags-zh-cn-translate.json", "w+", encoding="UTF-8") as f:
        f.write(json.dumps(tags, ensure_ascii=False))


if __name__ == "__main__":
    translate_json()
