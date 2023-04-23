import json
import copy
from translate import Translate


def translate_json():
    translator = Translate(src="en", dest="zh-cn")

    with open("./data/danbooru-tags.json", encoding="UTF-8") as f:
        tags = json.load(f)
    print(f"Loaded {len(tags)} tags")

    count = 0
    translate_count = 0
    fix_tag_names = [tag["name"].replace("_", " ") for tag in tags]
    bz = 100
    for i in range(0, len(fix_tag_names), bz):
        result_len = len(fix_tag_names[i:i + bz])
        result = translator.translate(fix_tag_names[i:i + bz])
        if result is not None:
            for j in range(result_len):
                tags[i + j]["zh_cn"] = result[j]
        else:
            for j in range(result_len):
                tags[i + j]["zh_cn"] = ""
        print(f"Translated {i} tags -> {result}")
        translator.save_cache()

    with open("./data/danbooru-tags-zh-cn-translate.json", "w+", encoding="UTF-8") as f:
        f.write(json.dumps(tags, ensure_ascii=False))
    print(f"\n\nTranslated {translate_count} tags, {count - translate_count} failed. (Total {count} tags)")


if __name__ == "__main__":
    translate_json()
