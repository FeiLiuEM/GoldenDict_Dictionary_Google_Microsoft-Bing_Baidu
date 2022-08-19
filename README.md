# Goldendict online translate

This is a method for goldendict using google, microsoft, and baidu translate.


## Google translator

There are 2 ways:

### 1.[translate-shell](https://github.com/soimort/translate-shell)

install translate-shell:

`sudo apt install translate-shell`

add to goldendict:

`edit-dictionaries-sources-programs`

Add new program

type : `plain text`

name : `google translate`

command line : `trans -e google -s auto -t zh-CN -show-original n -show-original-phonetics n -show-translation y -no-ansi -show-translation-phonetics n -show-prompt-message n -show-languages y -show-original-dictionary n -show-dictionary n -show-alternatives n “%GDWORD%”`


### 2.[google-translate-for-goldendict](https://github.com/xinebf/google-translate-for-goldendict)

install (python = 3.7+):

`pip3 install google-translate-for-goldendict`

add to goldendict:

`edit-dictionaries-sources-programs`

Add new program

type : `plain text`

name : `google translate`

command line : `python -m googletranslate zh-CN %GDWORD%`


## Microsoft translate

Follow the process of [azure doc](https://docs.microsoft.com/en-us/azure/cognitive-services/translator/quickstart-translator?tabs=csharp) to create your own translator resource.

Then, copy the `microsoft_translate.py` to your file. Remember changing the key and endpoint to your own.

add to goldendict:

`edit-dictionaries-sources-programs`

Add new program

type : `plain text`

name : `microsoft translate`

command line : `python3 yourfilepath/microsoft_translate.py %GDWORD%`


## Baidu translate

Follow the process of [baidu open translate platform](https://fanyi-api.baidu.com/api/trans/product/desktop), and create your own appid.

Then, copy the `baidu_translate.py` to your file. Remember changing the appid and key to your own.

add to goldendict:

`edit-dictionaries-sources-programs`

Add new program

type : `plain text`

name : `baidu translate`

command line : `python3 yourfilepath/baidu_translate.py %GDWORD%`

`baidu_translate.py` refers to the article of [e891377](https://blog.csdn.net/e891377/article/details/103399520). Thank for e891377 very much.
