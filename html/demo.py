# -*- coding: utf-8 -*-
import requests

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,la;q=0.6',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': 'Secure; xn_dvid_kf_20053=DC381F-E8536EB2-3CE5-B1E4-E4E8-598EA3E181EB; Hm_lvt_9ccb67a5cecd875ee397dd1a978ff7bd=1710899504; xn_sid_kf_20053=1710899504625749; JSESSIONID=A16B54F129DE479C983F36A9CEB34705; Hm_lpvt_9ccb67a5cecd875ee397dd1a978ff7bd=1710905382',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get('https://www.yunnanbaiyao.com.cn/list/ynbyPc/1/92/auto/6/0.html', headers=headers)
print(response.text)