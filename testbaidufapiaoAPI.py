# encoding:utf-8

import requests
import base64
import json
import requests
'''
增值税发票识别
'''
# encoding:utf-8

# client_id 为官网获取的AK， client_secret 为官网获取的SK
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=6FlEkzTZhREpWzPiWWtGGdjt&client_secret=wqoMOGQEMGOlc8DVCyLfgjnKhinsSYH6'
response = requests.get(host)
if response:
    print(response.json())
    token=response.json()['access_token']

request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/vat_invoice"
# 二进制方式打开图片文件
f = open('img/fpphoto.jpg', 'rb')
img = base64.b64encode(f.read())

params = {"image":img}

access_token = token+''
request_url = request_url + "?access_token=" + access_token
headers = {'content-type': 'application/x-www-form-urlencoded'}
response = requests.post(request_url, data=params, headers=headers)
if response:
    print (json.dumps(response.json(), sort_keys=True, indent=2,ensure_ascii=False))

jiaoyan_url="https://etax.zhejiang.chinatax.gov.cn/zjgfdzswjfpyh/fpzwcx/query.do"
ywlx="DZSWJ_FPCX_DZFP"
fpdm=response.json()["words_result"]["InvoiceCode"]
fphm=response.json()["words_result"]["InvoiceNum"]
kjfsbh=response.json()["words_result"]["SellerRegisterNum"]
kprq=response.json()["words_result"]["InvoiceDate"]
#je=response.json()["words_result"]["AmountInFiguers"]
je="2000.00"
kprq=kprq[0:4]+kprq[5:7]+kprq[8:10]





url = "https://etax.zhejiang.chinatax.gov.cn/zjgfdzswjfpyh/fpzwcx/query.do"
#payload="{\"ywlx\":\"DZSWJ_FPCX_DZFP\",\"fpdm\":\"033002000211\",\"fphm\":\"42012044\",\"kjfsbh\":\"91330382L37317581T\",\"kprq\":\"20200922\",\"je\":\"200.00\"}"
payload="{\"ywlx\":\""+ywlx+"\",\"fpdm\":\""+fpdm+"\",\"fphm\":\""+fphm+"\",\"kjfsbh\":\""+kjfsbh+"\",\"kprq\":\""+kprq+"\",\"je\":\""+je+"\"}"

headers = {
  'Content-Type': 'application/json','User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36','Host':'etax.zhejiang.chinatax.gov.cn'
}

response = requests.request("POST", url, headers=headers, data=payload)

if response.json()["resultObj"]["returnState"]["returnCode"]=="00":
    print("发票是真的")
else:
    print("假的")