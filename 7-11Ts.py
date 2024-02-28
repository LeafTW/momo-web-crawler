import urllib.request
import urllib.parse


def create_data(town):
    data = {
        'commandid': 'SearchStore',
        'city': '新北市',
        'town': town,
    }
    data_uncode = urllib.parse.urlencode(data).encode('utf-8')
    return data_uncode


def create_request(town):
    url = 'https://emap.pcsc.com.tw/EMapSDK.aspx'

    headers = {
        # 'Accept': '*/*',
        # 'Accept-Language': 'zh-TW,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        # 'Connection': 'keep-alive',
        # # 'Content-Length': '157',
        # 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'Cookie': 'ASP.NET_SessionId=iwdsyulksdle4vfsrtpsp5fx; SET_EC_COOKIE=rd1378o00000000000000000000ffff0ac80815o443; _ga=GA1.1.540553415.1688560715; _ga_5G3DBR5GCK=GS1.1.1688560714.1.0.1688560716.0.0.0; citrix_ns_id=AAE7SWSlZDvm5RcVAAAAADs4Wj6jLnj-PXS0O02r_jOEnjNmr4u9sIYwtllmmfsOOw==qGWlZA==ejs0R8KsCboiZWj8cKjD_rIWaEQ=',
        # 'Host': 'emap.pcsc.com.tw',
        # 'Origin': 'https://emap.pcsc.com.tw',
        # 'Referer': 'https://emap.pcsc.com.tw/emap.aspx',
        # 'Sec-Ch-Ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Microsoft Edge";v="114"',
        # 'Sec-Ch-Ua-Mobile': '?0',
        # 'Sec-Ch-Ua-Platform': '"macOS"',
        # 'Sec-Fetch-Dest': 'empty',
        # 'Sec-Fetch-Mode': 'cors',
        # 'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.67',
        # 'X-Requested-With': 'XMLHttpRequest',
    }
    request = urllib.request.Request(url=url, data=create_data(town), headers=headers)
    return request


def create_response(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content


def download(content,town):
    with open('7-11'+town+'.json', 'w', encoding='utf-8') as fp:
        fp.write(content)


if __name__ == '__main__':
    townar=['蘆洲區','三重區']
    for page in townar:
        request = create_request(page)
        content = create_response(request)
        print(content)
        download(content,page)
