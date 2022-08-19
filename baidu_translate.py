#coding: utf8
 
import http.client
import hashlib
import json
import urllib
import random
import sys


def content_baidu_translate(content):
    """
    百度翻译官方提示的方法
    """
    appid = 'yourappid'  # 填写你的appid
    secretKey = 'yourkey'  # 填写你的密钥
    httpClient = None
    myurl = '/api/trans/vip/translate'
    q = content
    fromLang = 'en' # 源语言
    toLang = 'zh'   # 翻译后的语言
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
        jsonResponse = response.read().decode("utf-8")# 获得返回的结果，结果为json格式
        js = json.loads(jsonResponse)  # 将json格式的结果转换字典结构
        #print(jsonResponse)
        content_print_byformat(js) # 打印结果
    except Exception as e:
        print(e)
    finally:
        if httpClient:
            httpClient.close()


def content_print_byformat(js):
    """
    控制打印格式
    参考资料 http://api.fanyi.baidu.com/doc/21
    """
    #srcStr = str(js["trans_result"][0]["src"])  # 取得翻译前的文本
    dstStr = str(js["trans_result"][0]["dst"])  # 取得翻译后的文本结果
    
    # 反过滤规则001
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
    # 过滤规则001
    # 不知道是自己的原因还是百度翻译有点坑
    if("\n" in bb):
        bb = bb.replace("\n", "\\r\\n")

    # 过滤规则002
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
    只翻译短语或者长句，不翻译单词
    单词查询通过朗文5++ LDOCE5查询
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
    主方法
    """
    content_filter_len(content)
    pass


if __name__ == '__main__':
    #入口
    # 参考 来源于：http://http://blog.csdn.net/lcyong_
    baidu_translate_goldendict(sys.argv[1])
