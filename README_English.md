# GoldenDict Dictionary of online translators

This is a method for goldendict using Google, Microsoft/Bing, and Baidu translate online.

System：`debian 11 (bullseye)`. Software：`GoldenDict 1.5.0-RC2`.

## 1 Google translate

There are 2 methods:

### 1.1 [translate-shell](https://github.com/soimort/translate-shell)

#### install translate-shell:

`sudo apt install translate-shell`

#### add to Goldendict:

`edit-dictionaries-sources-programs`

Add new program

type : `plain text`

name : `google translate`

command line : `trans -e google -s auto -t zh-CN -show-original n -show-original-phonetics n -show-translation y -no-ansi -show-translation-phonetics n -show-prompt-message n -show-languages y -show-original-dictionary n -show-dictionary n -show-alternatives n “%GDWORD%”`

### 1.2 [google-translate-for-goldendict](https://github.com/xinebf/google-translate-for-goldendict)

#### install (python = 3.7+):

`pip3 install google-translate-for-goldendict`

#### Add to Goldendict:

`edit-dictionaries-sources-programs`

Add new program

type : `plain text`

name : `google translate`

command line : `python -m googletranslate zh-CN %GDWORD%`

## 2 Microsoft/Bing translate

#### Follow the process of [Azure doc](https://docs.microsoft.com/en-us/azure/cognitive-services/translator/quickstart-translator?tabs=csharp) to create your own translator resource. The process need visa card and no charge. Microsoft Azure will start to charge after 2 million words each month.

#### Then, copy the `microsoft_translate.py` to your file. Remember changing the key, endpoint and location to your own.

#### Add to Goldendict:

`edit-dictionaries-sources-programs`

Add new program

type : `plain text`

name : `microsoft translate`

command line : `python3 your_file_path/microsoft_translate.py %GDWORD%`

## 3 Baidu translate

#### Follow the process of [Baidu Translate Platform](https://fanyi-api.baidu.com/api/trans/product/desktop), and create your own appid. It has no charge. 5 thousand free words for normal developers and 1 million free words for certificated developers.

#### Then, copy the `baidu_translate.py` to your file. Remember changing the appid and key to your own.

#### Add to Goldendict:

`edit-dictionaries-sources-programs`

Add new program

type : `plain text`

name : `baidu translate`

command line : `python3 your_file_path/baidu_translate.py %GDWORD%`

`baidu_translate.py` refers to the article of [e891377](https://blog.csdn.net/e891377/article/details/103399520). Thank for e891377 very much.
