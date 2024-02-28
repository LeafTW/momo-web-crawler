import urllib.request

url='https://www.mcdonalds.com/googleappsv2/geolocation?latitude=25.0329694&longitude=121.5654177&radius=5&maxResults=75&country=tw&language=zh-tw'

headers={
'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.67'
}

request=urllib.request.Request(url=url,headers=headers)

response=urllib.request.urlopen(request)

content=response.read().decode('utf-8')

import json

with open('mcdonalds.json', 'w', encoding='utf-8') as fp:
    fp.write(content)
print(content)