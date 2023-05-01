import json
from translate import Translate
import time


def translate_json():
    translator = Translate(src="en", dest="zh-cn")

    with open("./data/comparison_gpt4_data_en.json", encoding="UTF-8") as f:
        content = json.load(f)
    print(f"Loaded {len(content)} gpt4")

    count = 0
    translate_count = 0
    content_zh = []

    for c in content:
        instruction = c.get("instruction", "")
        output = c.get("output", ["", ])
        instruction_zh = translator.translate(instruction)
        output_zh = translator.translate(output)
        content_zh.append(
            {
                "instruction": instruction_zh,
                "input": c["input"],
                "output": output_zh,
            }
        )
        translate_count += 1
        
        if translate_count % 100 == 0:
            translator.save_cache()

    with open("./data/comparison_gpt4_data_zh.json", "w+", encoding="UTF-8") as f:
        f.write(json.dumps(content_zh, ensure_ascii=False))
    print(f"\n\nTranslated {translate_count} , {count - translate_count} failed. (Total {count} )")


if __name__ == "__main__":
    while True:
        try:
            translate_json()
        except Exception as e:
            print(e)
            time.sleep(60)
