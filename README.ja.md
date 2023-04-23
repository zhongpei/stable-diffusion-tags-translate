# 安定拡散タグ翻訳

安定した拡散タグを翻訳する

[中文](README.zh.md)｜[英語](README.md)｜[日本語](README.ja.md)｜[ロシア](README.ru.md)

-   グーグル翻訳を使って
    -   結果をキャッシュする`json`ファイル
-   マルチスレッドをサポート
-   多くの言語をサポート
-   キャッシュファイルの手動編集をサポート (txt、csv)
    -   `txt`: 1 行 1 語で`=`
    -   `csv`: 1 行 1 語で`,`
    -   `txt`、`csv`,グーグルキャッシュ(`json`）併用可能
    -   `txt`csv や Google 翻訳のキャッシュよりも優先度が高い

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

t.save_cache()
```
