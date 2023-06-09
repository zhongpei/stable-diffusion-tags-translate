# 安定拡散タグ翻訳

安定拡散プロンプトタグを翻訳する

[中文](README.zh-CN.md)｜[英語](README.md)｜[日本語](README.ja.md)｜[ロシア](README.ru.md)

-   グーグル翻訳を使って
    -   結果をキャッシュする`json`ファイル
    -   結果をredisにキャッシュする
-   マルチスレッドをサポート
-   多くの言語をサポート
-   キャッシュファイルの手動編集をサポート (txt、csv)
    -   `txt`: 1 行 1 語で`=`
    -   `csv`: 1 行 1 語で`,`
    -   `txt`、`csv`,グーグルキャッシュ(`json`) 併用可能
    -   `txt`csv や Google 翻訳のキャッシュよりも優先度が高い

## リリース

ダウンロード[中国語翻訳タグ(40K+)](https://github.com/zhongpei/stable-diffusion-tags-translate/releases/tag/v1.0)

-   `zh-CN.txt`ために[BooruDatasetTagManager](https://github.com/starik222/BooruDatasetTagManager)
-   `zh-CN-min.txt`ために[BooruDatasetTagManager](https://github.com/starik222/BooruDatasetTagManager)
    -   (高速起動用の小さなファイル)
    -   に改名してください`zh-CN.txt`
-   `danbooru-zh-CN.csv`ために[a1111-sd-webui-tagcomplete](https://github.com/DominikDoom/a1111-sd-webui-tagcomplete)

## Google 翻訳のサポート言語

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

## 使用法

ｔ欄ｓァて。ｐｙ

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

### 偶数

-   TRANSLATE_CACHE_DIR
    -   キャッシュディレクトリ名
    -   デフォルト：`./cache`
    -   redis キャッシュを使用する場合、これは redis ハッシュのキーです
-   USE_REDIS_CACHE
    -   `true`変換キャッシュに redis を使用する
    -   1000 以上のタグを翻訳するには、redis キャッシュをお勧めします
    -   デフォルトのホスト:`localhost`ポート：`6379`
    -   パラメータ`Translate('en', 'zh-cn',redis_host_port="1.1.1.1:6300")`
-   USE_GOOGLE_TRANSLATE
    -   `true`グーグル翻訳を使う
    -   `false`Google 翻訳を無効にしてキャッシュのみを使用する
    -   パラメータ`Translate('en', 'zh-cn',use_google_translate=False)`

## 例 1

-   タグを翻訳`en`に`zh-cn`
-   `zh-CN.txt`booru_dataset_tag_manager_translate の場合
-   `danbooru-zh-CN.csv`a1111-sd-webui-tagcomplete の場合

```bash
mkdir data
python booru_translate.py
```

## 例 2

-   から gpt データを変換する`en`に`zh-cn`
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
TRANSLATE_CACHE_DIR=./cache.gpt4 USE_REDIS_CACHE=true all_proxy="http://127.0.0.1:6152" python gpt4_data_translate.py

```
