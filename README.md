# GoldenDict Dictionary of online translators

# GoldenDict添加网络翻译工具翻译  [[English version](README_English.md)]

这个项目将谷歌翻译、微软/必应翻译和百度翻译添加到GoldenDict中。

## 1 谷歌翻译

谷歌翻译添加到GoldenDict有两种方法:

### 1.1 [translate-shell](https://github.com/soimort/translate-shell)

#### 安装translate-shell:

`sudo apt install translate-shell`

#### 添加到Goldendict:

`编辑——词典来源——程序——添加`

类型 : 纯文本

名称 : `google translate`

命令行 : `trans -e google -s auto -t zh-CN -show-original n -show-original-phonetics n -show-translation y -no-ansi -show-translation-phonetics n -show-prompt-message n -show-languages y -show-original-dictionary n -show-dictionary n -show-alternatives n “%GDWORD%”`

### 1.2 [google-translate-for-goldendict](https://github.com/xinebf/google-translate-for-goldendict)

#### 安装 (python = 3.7+):

`pip3 install google-translate-for-goldendict`

#### 添加到Goldendict:

`编辑——词典来源——程序——添加`

类型 : `plain text`

名称 : `google translate`

命令行 : `python -m googletranslate zh-CN %GDWORD%`

## 2 微软/必应翻译

#### 首先按照[Azure doc](https://docs.microsoft.com/en-us/azure/cognitive-services/translator/quickstart-translator?tabs=csharp)上的描述建立你的翻译resource 。

#### 然后，将 `microsoft_translate.py` 粘贴到你的文件夹中。 记得将文件中的key, endpoint 和 location 都改成你自己的。

#### 添加到Goldendict:

`编辑——词典来源——程序——添加`

类型 : `plain text`

名称 : `microsoft translate`

命令行 : `python3 your_file_path/microsoft_translate.py %GDWORD%`

## 3 百度翻译

#### 按照百度翻译开放平台[Baidu Translate Platform](https://fanyi-api.baidu.com/api/trans/product/desktop)的流程进行开发者注册，建立APP并获取appid及key。

#### 然后，将 `baidu_translate.py` 粘贴到你的文件夹中。记得将文件中的appid 和 key 都修改成刚才申请的。

#### 添加到Goldendict:

`编辑——词典来源——程序——添加`

类型 : `plain text`

名称 : `baidu translate`

命令行: `python3 your_file_path/baidu_translate.py %GDWORD%`

`baidu_translate.py` 参考了[e891377的文章](https://blog.csdn.net/e891377/article/details/103399520)。非常感谢e891377

`baidu_translate.py` refers to the article of [e891377](https://blog.csdn.net/e891377/article/details/103399520). Thank for e891377 very much.
