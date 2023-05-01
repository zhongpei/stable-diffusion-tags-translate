# 稳定扩散标签翻译

翻译稳定扩散提示标签

[中文](README.zh-CN.md)\|[英语](README.md)\|[日本人](README.ja.md)\|[俄语](README.ru.md)

-   使用谷歌翻译
    -   将结果缓存在`json`文件
-   支持多线程
-   支持多种语言
-   支持手动编辑缓存文件(txt,csv)
    -   `txt`: 一行一个字`=`
    -   `csv`: 一行一个字`,`
    -   `txt`,`csv`,谷歌缓存(`json`) 可以一起使用
    -   `txt`优先级高于 csv 和谷歌翻译缓存

## 发布

下载[中文翻译标签(40K+)](https://github.com/zhongpei/stable-diffusion-tags-translate/releases/tag/v1.0)

-   `zh-CN.txt`为了[Booru数据集标签管理器](https://github.com/starik222/BooruDatasetTagManager)
-   `zh-CN-min.txt`为了[Booru数据集标签管理器](https://github.com/starik222/BooruDatasetTagManager)
    -   （用于快速启动的小文件）
    -   请重命名为`zh-CN.txt`
-   `danbooru-zh-CN.csv`为了[a1111-sd-webui-tagcomplete](https://github.com/DominikDoom/a1111-sd-webui-tagcomplete)

## 谷歌翻译支持语言

<details>
<summary>google translate support languages</summary>

```json
{
  'af': 'afrikaans',
  'sq': 'albanian',
  'am': 'amharic',
  'ar': 'arabic',
  'hy': 'armenian',
  'az': 'azerbaijani',
  'eu': 'basque',
  'be': 'belarusian',
  'bn': 'bengali',
  'bs': 'bosnian',
  'bg': 'bulgarian',
  'ca': 'catalan',
  'ceb': 'cebuano',
  'ny': 'chichewa',
  'zh-cn': 'chinese (simplified)',
  'zh-tw': 'chinese (traditional)',
  'co': 'corsican',
  'hr': 'croatian',
  'cs': 'czech',
  'da': 'danish',
  'nl': 'dutch',
  'en': 'english',
  'eo': 'esperanto',
  'et': 'estonian',
  'tl': 'filipino',
  'fi': 'finnish',
  'fr': 'french',
  'fy': 'frisian',
  'gl': 'galician',
  'ka': 'georgian',
  'de': 'german',
  'el': 'greek',
  'gu': 'gujarati',
  'ht': 'haitian creole',
  'ha': 'hausa',
  'haw': 'hawaiian',
  'iw': 'hebrew',
  'he': 'hebrew',
  'hi': 'hindi',
  'hmn': 'hmong',
  'hu': 'hungarian',
  'is': 'icelandic',
  'ig': 'igbo',
  'id': 'indonesian',
  'ga': 'irish',
  'it': 'italian',
  'ja': 'japanese',
  'jw': 'javanese',
  'kn': 'kannada',
  'kk': 'kazakh',
  'km': 'khmer',
  'ko': 'korean',
  'ku': 'kurdish (kurmanji)',
  'ky': 'kyrgyz',
  'lo': 'lao',
  'la': 'latin',
  'lv': 'latvian',
  'lt': 'lithuanian',
  'lb': 'luxembourgish',
  'mk': 'macedonian',
  'mg': 'malagasy',
  'ms': 'malay',
  'ml': 'malayalam',
  'mt': 'maltese',
  'mi': 'maori',
  'mr': 'marathi',
  'mn': 'mongolian',
  'my': 'myanmar (burmese)',
  'ne': 'nepali',
  'no': 'norwegian',
  'or': 'odia',
  'ps': 'pashto',
  'fa': 'persian',
  'pl': 'polish',
  'pt': 'portuguese',
  'pa': 'punjabi',
  'ro': 'romanian',
  'ru': 'russian',
  'sm': 'samoan',
  'gd': 'scots gaelic',
  'sr': 'serbian',
  'st': 'sesotho',
  'sn': 'shona',
  'sd': 'sindhi',
  'si': 'sinhala',
  'sk': 'slovak',
  'sl': 'slovenian',
  'so': 'somali',
  'es': 'spanish',
  'su': 'sundanese',
  'sw': 'swahili',
  'sv': 'swedish',
  'tg': 'tajik',
  'ta': 'tamil',
  'te': 'telugu',
  'th': 'thai',
  'tr': 'turkish',
  'uk': 'ukrainian',
  'ur': 'urdu',
  'ug': 'uyghur',
  'uz': 'uzbek',
  'vi': 'vietnamese',
  'cy': 'welsh',
  'xh': 'xhosa',
  'yi': 'yiddish',
  'yo': 'yoruba',
  'zu': 'zulu'
}

```

</details>

## 用法

translate.朋友

```python
from translate import Translate

t = Translate('en', 'zh-cn')

print(t.translate("1girl"))
print(t.translate("hello"))

# batch translate
print(t.translate(["hello world", "say goodbye"]))

# save cache
t.save_cache()

# dump cache to json
t.dump_cache()
```

## 示例 1

-   翻译标签来自`en`到`zh-cn`
-   `zh-CN.txt`对于 booru_dataset_tag_manager_translate
-   `danbooru-zh-CN.csv`对于 a1111-sd-webui-tagcomplete

```bash
mkdir data
python booru_translate.py
```

## 示例 2

-   从翻译gpt数据`en`到`zh-cn`
-   comparison_gpt4_data_en.json

```bash
# install requirements
pip install -r requirements.txt

# make data dir
mkdir -p ./data
cp comparison_gpt4_data_en.json ./data/comparison_gpt4_data_en.json

# make cache dir
mkdir -p ./cache.gpt4/en_zh-cn/txt
mkdir -p ./cache.gpt4/en_zh-cn/csv

# use  proxy and cache
TRANSLATE_CACHE_DIR=./cache.gpt4 all_proxy="http://127.0.0.1:6152" python gpt4_data_translate.py

```
