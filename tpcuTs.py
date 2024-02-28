import urllib.request

url='http://www.pcschool.tv/2018/classrecords.aspx'

headers={
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'zh-TW,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': '_gid=GA1.2.714790051.1688662954; _qg_fts=1688662955; QGUserId=6152445374317490; _qg_cm=2; ASP.NET_SessionId=whsd4i45vtdddk45txqb0sry; Token=DB47A48C2CA251271A0822B317A18039EDA483B88425FDFEC00F9079739B4DF156DCD48074E30F601BAF5C6A38D04EB7383FE479DB322DC968EF9C3C3673E9153B3630B9830787BFA8D7183675814D9B75B9F6CBE4F87E9B8AE10E94FBBDA7EBAB6F91D9B19CAA0A2959B312D7E478F6840A38F86CA9811E320DCC98F6C0E200ABFAD7704912A9325971102666D02EA6C8FACFD594EFD1D68267C33B3A16428E929ACD6B1B1681D6BD3F076AB08677BA; _ga=GA1.2.496332488.1688662954; _ga_8LY1FWBJRK=GS1.1.1688662954.1.1.1688663498.0.0.0',
    'Host': 'www.pcschool.tv',
    'Referer':'http://www.pcschool.tv/2018/classroom.aspx',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.67',
}


request=urllib.request.Request(url=url,headers=headers)

response=urllib.request.urlopen(request)

content=response.read().decode('utf-8')

print(content)
