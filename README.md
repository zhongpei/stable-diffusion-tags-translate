# stable-diffusion-tags-translate

tanslate stable diffusion prompt tags

[中文](README.zh-CN.md)|[English](README.md)|[日本語](README.ja.md)|[Russian](README.ru.md)


* using google translate
    * cache the result in `json` file
* support multi-threading
* support many languages
* support edit cache file manually(txt,csv)
    * `txt`: one line one word with `=`
    * `csv`: one line one word with `,`
    * `txt`,`csv`,google cache(`json`) can be used together
    * `txt` is higher priority than csv and google translate cache

## Realases

Download [Chinese translate tags(40K+)](https://github.com/zhongpei/stable-diffusion-tags-translate/releases/tag/v1.0)

* `zh-CN.txt` for [BooruDatasetTagManager](https://github.com/starik222/BooruDatasetTagManager)
* `zh-CN-min.txt` for [BooruDatasetTagManager](https://github.com/starik222/BooruDatasetTagManager) 
  * (small file for speed launch)
  * please rename to `zh-CN.txt`
* `danbooru-zh-CN.csv` for [a1111-sd-webui-tagcomplete](https://github.com/DominikDoom/a1111-sd-webui-tagcomplete)

## google translate support languages

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

## Usage

translate.py

``` python
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


## example 1

* translate tags from `en` to `zh-cn`
* `zh-CN.txt` for booru_dataset_tag_manager_translate
* `danbooru-zh-CN.csv` for a1111-sd-webui-tagcomplete 


``` bash
mkdir data
python booru_translate.py
```

## example 2
* translate gpt data from `en` to `zh-cn`
* comparison_gpt4_data_en.json

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