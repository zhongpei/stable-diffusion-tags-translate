import os
from translate import Translate


def translate():
    tags = []
    with open("./tags/danbooru.csv", encoding="UTF-8") as f:
        lines = f.readlines()
        print(f"Loaded {len(lines)} lines")
        for l in lines:
            tag = l.split(",")[0].strip()
            tags.append(tag)

    t = Translate(src="en", dest="zh-cn", enable_google_translate=False)
    tags_dict = {}
    for tag in tags:
        result = t.translate(tag)
        if result is not None:
            tags_dict.update({tag: result})
    print(f"Translated {len(tags_dict)} tags ,not translated {len(tags) - len(tags_dict)} tags")
    with open("./data/zh-CN.txt", "w+") as f:
        f.write("\n".join([f"{k}={v}" for k, v in tags_dict.items()]))


if __name__ == "__main__":
    translate()
