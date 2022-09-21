#coding: utf8
 
import sys
import requests, uuid, json



def content_microsoft_translate(content):
    """
    Official method from Microsoft
    """
    
    # Add your subscription key and endpoint
    subscription_key = "yourkey"  # your key here
    endpoint = "yourendpoint"     # your endpoint here

    # Add your location, also known as region. The default is global.
    # This is required if using a Cognitive Services resource.
    location = "yourlocation"     # your location here

    path = '/translate?api-version=3.0'
    params = '&from=en&to=zh-Hans'
    constructed_url = endpoint + path + params

    headers = {
        'Ocp-Apim-Subscription-Key': subscription_key,
        'Ocp-Apim-Subscription-Region': location,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }

    # You can pass more than one object in body.
    body = [{
        'text': content
    }]

    try:
        request = requests.post(constructed_url, headers=headers, json=body)
        response = request.json()

        result=json.dumps(response, sort_keys=True, indent=4, ensure_ascii=False, separators=(',', ': '))

        #content_print_byformat(result[73:-66])
        print(result[73:-66])

    except Exception as e:
        print(e)


def content_print_byformat(js):
    """
    set print format
    """
    #srcStr = str(js["trans_result"][0]["src"])  # the context you want to translate
    dstStr = js  
    
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
    content_microsoft_translate(bb)
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


def microsoft_translate_goldendict(content):
    """
    主方法main
    """
    content_filter_len(content)
    pass


if __name__ == '__main__':
    #入口
    # 参考 来源于：http://http://blog.csdn.net/lcyong_
    microsoft_translate_goldendict(sys.argv[1])
