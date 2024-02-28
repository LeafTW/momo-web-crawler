import urllib.request
import urllib.parse
def create_request():
    url='https://shopee.tw/api/v4/search/search_items?brandids=1695290&by=relevancy&extra_params=%7B%22global_search_session_id%22%3A%22gs-d51407b4-1158-4637-80d2-2898800a346c%22%2C%22search_session_id%22%3A%22ss-de037bd7-2109-438f-bcdc-577af5c21647%22%7D&filters=8&keyword=%E5%86%B0%E7%AE%B1&limit=60&newest=0&order=desc&page_type=search&scenario=PAGE_GLOBAL_SEARCH&skip_autocorrect=1&version=2&view_session_id=fe83c145-1bc4-4d1b-a244-142537f51830'

    headers={
        'Accept': 'application/json',
        'Accept-Language': 'zh-TW,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Af-Ac-Enc-Dat': 'AAcyLjkuMS0yAAABiSU09TwAABAeAzAAAAAAAAAAAi465FdBJjDHG2D7Rfic/dLEz5gOTRVGZWAsMzRyvNrv9VoNGG2wHGoZ+Hd58CAhbDoO+MwSNiqNqjfsmDdVzjliPN1dmk9dWrGLa3RlN98GufvaL5f/NhMnw8f21UXD2mkb2JtaGu6mk1vlSSndtvlmO5TN5qggv3YQdpXUQJvNHm0xlBN5QCFuh0m2a7iQsFUA38iqGPJK/e+qxrRR8l/rz7gcYoU4SupFjicPUmA4FV5PplTN8HaiZJpSsJ8Fr1LarOMX62ITm9QsOI4keU3/BMdE7lINDv0ZUZBVjxabTDTEXgKvwGjWjkxYEn7LwCx+oLphADPADj0nEhba9Evm2Wc/QR/4tXPTPQhC6IAvLExR8pMHL5cyiMTNvgFvmBKQ+KVfAfD+HBQIBW0XS/XUvJ6lIs0njiNZRLdrnNHOa0keZTfFJ4dnvtiGevj7Jf0d7D91NUSAybY6BDuYB6MbWmmFm4nQ8D626nB7rerG1zypyVyqPLAn+EX/M6j/n2SQM5hroYEnr3l0g7m+c8sN/UQ9tre1b9o5f86tU5uxvdYnuYzaSwO/1GXe2Xe6/gfPKa8D4cCKiQCMwzFuMupYLWHJCqIrPjU+emTZmlk9jkCKAozaSwO/1GXe2Xe6/gfPKa87/xPoxFmICzjLguBkThXXZ5bEy5gP2F6rkSjtHpL/AsG19vqGwWdBbeyLXP6cNFqeyakW0IuKjgX1+ZffSi00Uc0GsoJIS67uDp/IzmPQK74Fgo5sqJmfexml31UqpXOeyakW0IuKjgX1+ZffSi00cxJD7E2wjrl13csvrzhnYJf/NhMnw8f21UXD2mkb2JuFTM2zX08f0V2KJOs4lhA+CmNP1FWmqeRGnfubVN/y46YrO5hv1Mplr18FvvBMBKKxqi/ChyBmmWSoM2j4Hse2uhOxEXwD8eG8cbN1slrxBYNb3DvJsAwfdFOhNQyZ4aiMzALIkz8dHcR859XZETMUxD3SJD18JCYSgrv8PqyP0l+D1o/j7MLIrJbQh21oSWJ8rWiN8GoAqCbByH4hJcjIE3lAIW6HSbZruJCwVQDfyKc/KzbIML8pyQev7E44iHI=',
        'Af-Ac-Enc-Sz-Token': 'PcsiX9fJw36d2Ssd2f095w==|tTeYKR/qHX+wIW4SxFGRyuAMJxTCkDZcb9HAiHavSjR5akg4sHCS9S51g+2dWXbT9iQrLbzgfyIBcVxUTtWw4TR12UwQxw/GOQ==|1a2vTRSl3ZhbDD8U|06|3',
        'B1626324': 'S5:KGM1e04V1h3QIkpE6\'BaR+#[(E-IaD,=MJ3l)Rs<3eltKMA>e@8%n]\'Q3VAGnLQb]@NfrF_U%kmgZ668\\n8k`hs#qS>ZST]Ua*p5Z57-0<^JPj+@S00RV3)!_ZQBsQ)K9PeJgSFYeH$e&,E6sZ`o;$q;3G>BM_BXi&#EFrt=(q"G2T(M7.BV@&[_2]9)KVbNNND](Oj4ZN#3XuchB!chK])Cgd$R(a$[#n%1II31AgN_e:U$BpM\'u-k$=PE5@UHi(BY576l3]<nFW"7#0@jT4^N.uZRiq/%JuLKbA7ZqV+M,c/*+LkbL50m8(_R1*,EpF\\anV!E?6>ugn.^XAb.hnBOHY7VM/$Xi\GTEJV)J[`S*9W7/2X"u\C%s^k^@X3XF`,m ',
        'Content-Type': 'application/json',
        'Cookie': '_fbp=fb.1.1677245903254.33393504; SPC_F=OD7AjcAbcI4F8ZhAdAv2YS0OKdGWxi6s; REC_T_ID=8214c483-b448-11ed-ab22-f4ee08290b63; SPC_CLIENTID=T0Q3QWpjQWJjSTRGbbtpmoafigxozune; __stripe_mid=d7583f72-f56d-4316-a4c2-201af2d97180aad618; _fbc=fb.1.1679655301630.IwAR0cWt6cgeFu_wQ2xGxlVsqmM4WFnkDleRpVkuMiL0fgxYB2oTuVbR5zjec; SC_DFP=ayYUsyAVxDnsfVbdsJkyGxBhUqmExTQg; _gcl_au=1.1.1353168036.1685616395; __LOCALE__null=TW; csrftoken=o8WbF8jxOYKdW51VaMrDTnftRNdHz19k; SPC_EC=-; SPC_U=-; SPC_SI=aquaZAAAAABUTmd1dGVYS19y8wIAAAAAMjd5M0RwSHE=; SPC_R_T_ID=KDB7/AW0tCy1FGxOigTHHc+LjiqAYoCYNSRBMCOaQOT2dhcUe3UGTXEytWoNhCCX/YYTGnvKbGS3b1gdGImHOIOj0cP1pqGOTXF+KnNtEg26SjilEP5B8si7h8VeaI6rvqRsus0c3ipeYCkqUbkfbZ4Y1FjYD0d8fLiqlq56rQI=; SPC_R_T_IV=UjhtdWdxUjI0eWdQVkJ4dA==; SPC_T_ID=KDB7/AW0tCy1FGxOigTHHc+LjiqAYoCYNSRBMCOaQOT2dhcUe3UGTXEytWoNhCCX/YYTGnvKbGS3b1gdGImHOIOj0cP1pqGOTXF+KnNtEg26SjilEP5B8si7h8VeaI6rvqRsus0c3ipeYCkqUbkfbZ4Y1FjYD0d8fLiqlq56rQI=; SPC_T_IV=UjhtdWdxUjI0eWdQVkJ4dA==; _QPWSDCXHZQA=ffbe94fc-7901-4d3d-9cdd-8f6723940889; shopee_webUnique_ccd=PcsiX9fJw36d2Ssd2f095w%3D%3D%7CtTeYKR%2FqHX%2BwIW4SxFGRyuAMJxTCkDZcb9HAiHavSjR5akg4sHCS9S51g%2B2dWXbT9iQrLbzgfyIBcVxUTtWw4TR12UwQxw%2FGOQ%3D%3D%7C1a2vTRSl3ZhbDD8U%7C06%7C3; ds=f11060639083e155e9181bc593306c9c; AMP_TOKEN=%24NOT_FOUND; _ga=GA1.2.1165606106.1683191621; _gid=GA1.2.1633148262.1688546378; _dc_gtm_UA-61915057-6=1; _ga_RPSBE3TQZZ=GS1.1.1688546375.5.1.1688546388.47.0.0',
        'E3a5394e': '^?VJA)oA[s.e;APrM?KIj?X,j',
        'Referer':'https://shopee.tw/search?brands=1695290&filters=8&keyword=%E5%86%B0%E7%AE%B1&noCorrection=true&page=0',
        'Sec-Ch-Ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Microsoft Edge";v="114"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': '"macOS"',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'Sz-Token': 'PcsiX9fJw36d2Ssd2f095w==|tTeYKR/qHX+wIW4SxFGRyuAMJxTCkDZcb9HAiHavSjR5akg4sHCS9S51g+2dWXbT9iQrLbzgfyIBcVxUTtWw4TR12UwQxw/GOQ==|1a2vTRSl3ZhbDD8U|06|3',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.67',
        'X-Api-Source': 'pc',
        'X-Csrftoken': 'o8WbF8jxOYKdW51VaMrDTnftRNdHz19k',
        'X-Requested-With': 'XMLHttpRequest',
        'X-Sap-Access-F': '3.2.114.6.0|13|2.9.1-2_5.3.73_0_356|df0184df59f24579ab132781629edcc7228ca1260ed745|10900|100',
        'X-Sap-Access-S': 'P72sZZjD0wE9FCSmuN2OF9k--Y9CiPg2JBQvFEwgMuk=',
        'X-Sap-Access-T': '1688546389',
        'X-Sap-Ri': '582ca5646a131c810533813829f20ba1349a6022042587d6',
        'X-Shopee-Language': 'zh-Hant',
        'X-Sz-Sdk-Version': '2.9.1-2@1.2.2',
    }
    # data=urllib.parse.urlencode(data).encode('utf-8')
    request = urllib.request.Request(url=url,headers=headers)
    return request

def create_response(request):
    response=urllib.request.urlopen(request)
    content=response.read().decode('utf-8')
    return content

import json
def down_load(content):
    with open('momo.json','w',encoding='utf-8')as fp:
        fp.write(content)

if __name__ == '__main__':
    response=create_request();
    content=create_response(response)
    down_load(content)
    print(content)
