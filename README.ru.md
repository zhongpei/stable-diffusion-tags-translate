# стабильная-диффузия-теги-перевести

tanslate stable diffusion prompt tags

[Китайский](README.zh-CN.md)\|[Английский](README.md)\|[Японский](README.ja.md)\|[Русский](README.ru.md)

-   с помощью гугл переводчика
    -   кэшировать результат в`json`файл
    -   кешировать результат в Redis
-   поддержка многопоточности
-   поддержка многих языков
-   поддержка редактирования файла кеша вручную (txt, csv)
    -   `txt`: одна строка одно слово с`=`
    -   `csv`: одна строка одно слово с`,`
    -   `txt`,`csv`,кеш гугла(`json`) можно использовать вместе
    -   `txt`имеет более высокий приоритет, чем csv и кэш перевода google

## Релизы

Скачать[Chinese translate tags(40K+)](https://github.com/zhongpei/stable-diffusion-tags-translate/releases/tag/v1.0)

-   `zh-CN.txt`для[BooruDatasetTagManager](https://github.com/starik222/BooruDatasetTagManager)
-   `zh-CN-min.txt`для[BooruDatasetTagManager](https://github.com/starik222/BooruDatasetTagManager)
    -   (небольшой файл для быстрого запуска)
    -   пожалуйста, переименуйте в`zh-CN.txt`
-   `danbooru-zh-CN.csv`для[a1111-sd-webui-tagcomplete](https://github.com/DominikDoom/a1111-sd-webui-tagcomplete)

## языки поддержки гугл переводчик

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

## Применение

транслайте.по

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

### даже

-   TRANSLATE_CACHE_DIR
    -   имя каталога кеша
    -   по умолчанию:`./cache`
    -   при использовании кеша redis это ключ хэша redis
-   USE_REDIS_CACHE
    -   `true` use redis for translate cache
    -   перевести более 1000 тегов, рекомендуется кэш Redis
    -   хост по умолчанию:`localhost`порт:`6379`
    -   параметр`Translate('en', 'zh-cn',redis_host_port="1.1.1.1:6300")`
-   ИСПОЛЬЗОВАТЬ GOOGLE TRANSLATE
    -   `true`Используйте Гугл переводчик
    -   `false` disable google translate only use cache
    -   параметр`Translate('en', 'zh-cn',use_google_translate=False)`

## пример 1

-   перевести теги из`en`к`zh-cn`
-   `zh-CN.txt`для booru_dataset_tag_manager_translate
-   `danbooru-zh-CN.csv`для a1111-sd-webui-tagcomplete

```bash
mkdir data
python booru_translate.py
```

## пример 2

-   перевести данные gpt из`en`к`zh-cn`
-   сравнение\_gpt4_data_en.json

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
TRANSLATE_CACHE_DIR=./cache.gpt4 USE_REDIS_CACHE=true all_proxy="http://127.0.0.1:6152" python gpt4_data_translate.py

```
