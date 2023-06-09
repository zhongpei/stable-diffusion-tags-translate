import os
from translate import Translate


def translate(tag_type=None):
    tags = []
    with open("./tags/danbooru.csv", encoding="UTF-8") as f:
        lines = f.readlines()
        print(f"Loaded {len(lines)} lines")
        for l in lines:
            tag, ttype = l.split(",")[:2]
            tag = tag.strip()
            if tag_type is not None:
                if ttype != tag_type:
                    continue
            tags.append(tag)

    t = Translate(src="en", dest="zh-cn")
    tags_dict = {}
    bz = 1000
    for i in range(0, len(tags), bz):
        result_len = len(tags[i:i + bz])
        result = t.translate(tags[i:i + bz])
        if result is not None:
            for j in range(result_len):
                if result[j] is not None:
                    tags_dict.update({tags[i + j]: result[j]})

        print(f"Translated {i} tags -> {result}")
        t.save_cache()

    print(f"Translated {len(tags_dict)} tags ,not translated {len(tags) - len(tags_dict)} tags")
    result_list = [[k, v] for k, v in tags_dict.items()]
    result_list.sort(key=lambda x: x[0])
    return result_list


if __name__ == "__main__":
    # booru_dataset_tag_manager_translate
    result_list = translate("0")
    with open("./data/zh-CN-min.txt", "w+", encoding='utf-8') as f:
        f.write("\n".join(f"{x[0]}={x[1]}" for x in result_list))

    result_list = translate()
    with open("./data/zh-CN.txt", "w+", encoding='utf-8') as f:
        f.write("\n".join(f"{x[0]}={x[1]}" for x in result_list))

    # a1111-sd-webui-tagcomplete
    with open("./data/danbooru-zh-CN.csv", "w+", encoding='utf-8') as f:
        f.write("\n".join(f"{x[0]},{x[1]}" for x in result_list))
