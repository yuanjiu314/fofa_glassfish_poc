import requests
import base64
from lxml import etree
import time

headers ={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'cookie':'Hm_lvt_19b7bde5627f2f57f67dfb76eedcf989=1673016888; _ga=GA1.1.1605595110.1673016888; __fcd=JYLubnDuSTXIF3acYJPFiA8S; befor_router=%2Fresult%3Fqbase64%3DImdsYXNzZmlzaCIgJiYgY291bnRyeT0iQ04iICYmIHBvcnQ9IjQ4NDgi%26page%3D1%26page_size%3D20; is_flag_login=0; fofa_token=eyJhbGciOiJIUzUxMiIsImtpZCI6Ik5XWTVZakF4TVRkalltSTJNRFZsWXpRM05EWXdaakF3TURVMlkyWTNZemd3TUdRd1pUTmpZUT09IiwidHlwIjoiSldUIn0.eyJpZCI6MjQyMTg4LCJtaWQiOjEwMDEzODM2MiwidXNlcm5hbWUiOiLlhYPphZIiLCJleHAiOjE2NzM4MzkzMDl9.J3o02AiC41nINIMWTQulV6gZeibhm2j_xBUXc7yvNiI3vuZnQLXNeJ785vu-f9DZ2v2-CCmOwWqzqhceOofixw; user=%7B%22id%22%3A242188%2C%22mid%22%3A100138362%2C%22is_admin%22%3Afalse%2C%22username%22%3A%22%E5%85%83%E9%85%92%22%2C%22nickname%22%3A%22%E5%85%83%E9%85%92%22%2C%22email%22%3A%22om2bg0sr_hloqdexywscs6jarhqa%40open_wechat%22%2C%22avatar_medium%22%3A%22https%3A%2F%2Fthirdwx.qlogo.cn%2Fmmopen%2Fvi_32%2FFE5ibp4mqSH3zr8bq6UBOC54HPh7CxgE2niaSXcicB8rcmBgk84QVbOwKFjQw96ia3WXdQic1DFBaAvOnKnaW4NFE6A%2F132%22%2C%22avatar_thumb%22%3A%22https%3A%2F%2Fthirdwx.qlogo.cn%2Fmmopen%2Fvi_32%2FFE5ibp4mqSH3zr8bq6UBOC54HPh7CxgE2niaSXcicB8rcmBgk84QVbOwKFjQw96ia3WXdQic1DFBaAvOnKnaW4NFE6A%2F132%22%2C%22key%22%3A%22b4009c9ed96c9be64d11852e439495a8%22%2C%22rank_name%22%3A%22%E6%B3%A8%E5%86%8C%E7%94%A8%E6%88%B7%22%2C%22rank_level%22%3A0%2C%22company_name%22%3A%22%E5%85%83%E9%85%92%22%2C%22coins%22%3A0%2C%22can_pay_coins%22%3A0%2C%22credits%22%3A0%2C%22expiration%22%3A%22-%22%2C%22login_at%22%3A1673580109%7D; isRedirect=1; baseShowChange=false; viewOneHundredData=false; _ga_9GWBD260K9=GS1.1.1673577978.3.1.1673585939.0.0.0; Hm_lpvt_19b7bde5627f2f57f67dfb76eedcf989=1673585940'
}

search = '"glassfish" && country="CN" && port="4848"'
for page in range(1,6):
    print('正在提取第%s页'%str(page))
    try:
        search_data_base64 = base64.b64encode(search.encode('utf-8'))
        search_data = str(search_data_base64.decode('utf-8'))
        url = 'https://fofa.info/result?&qbase64='+search_data+'&page='+str(page)

        response = requests.get(url,headers=headers).content
        soup = etree.HTML(response)
        target_ip = soup.xpath('//a[@target="_blank"]/@href')
        ip = '\n'.join(target_ip)
        print(ip)
        with open(r'ip.txt','a+') as f:
            f.write(ip+'\n')
            #f.close() with自带关闭
        time.sleep(0.5)
    except Exception as e:
        pass
