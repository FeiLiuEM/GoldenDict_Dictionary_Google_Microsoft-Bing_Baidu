#coding: utf8
 
import http.client
import hashlib
import json
import urllib
import random
import sys


def content_baidu_translate(content):
    """
    Official method from Baidu
    """
    appid = 'yourappid'  # your appid here
    secretKey = 'yourkey'  # your key here
    httpClient = None
    myurl = '/api/trans/vip/translate'
    q = content
    fromLang = 'en' # The language you want to translate from.
    toLang = 'zh'   # The language you want to translate to.
    salt = random.randint(32768, 65536)
    sign = appid + q + str(salt) + secretKey
    sign = hashlib.md5(sign.encode()).hexdigest()
    myurl = myurl + '?appid=' + appid + '&q=' + urllib.parse.quote(
        q) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(
        salt) + '&sign=' + sign
 
    try:
        httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
        httpClient.request('GET', myurl)
        # response是HTTPResponse对象
        response = httpClient.getresponse()
        jsonResponse = response.read().decode("utf-8")# get the result with the type of json
        js = json.loads(jsonResponse)  # transfer json to dict
        #print(jsonResponse)
        content_print_byformat(js) # print the result
    except Exception as e:
        print(e)
    finally:
        if httpClient:
            httpClient.close()


def content_print_byformat(js):
    """
    set print format
    reference http://api.fanyi.baidu.com/doc/21
    """
    #srcStr = str(js["trans_result"][0]["src"])  # the context you want to translate
    dstStr = str(js["trans_result"][0]["dst"])  # result
    
    # Text adjustment 
    #if("\\r\\n" in srcStr):
    #    srcStr = srcStr.replace("\\r\\n","\n")
    if("\\r\\n" in dstStr):
        dstStr = dstStr.replace("\\r\\n","\n")
    #print(srcStr)
    #print(" ")
    print(dstStr)
    pass


def content_filter_word(content):
    """
    过滤内容
    """
    bb= content
    # Text adjustment 1
    # 不知道是自己的原因还是百度翻译有点坑
    if("\n" in bb):
        bb = bb.replace("\n", "\\r\\n")

    # Text adjustment 2
    tup1 = ('来源：力扣（LeetCode）',
            '链接：https://leetcode-cn.com/problems/',
            '著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。')
    if(tup1[0] in bb):
        cc = bb.split(tup1[0])
        bb = cc[0]
        pass
    content_baidu_translate(bb)
    pass


def content_filter_len(content):
    """
    Translate sentences only
    """
    if(len(content.split())>=2):
        #print('content大于等于2')
        content_filter_word(content)
    else:
        #print('content小于2，不翻译')
        print('^_^')
    pass


def baidu_translate_goldendict(content):
    """
    主方法main
    """
    content_filter_len(content)
    pass


if __name__ == '__main__':
    #入口
    # 参考 来源于：http://http://blog.csdn.net/lcyong_
    baidu_translate_goldendict(sys.argv[1])
