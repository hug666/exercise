import requests
import re


def getHTMLText(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/100.0.4896.88 Safari/537.36 '
        }
        res = requests.get(url, headers=headers)
        res.raise_for_status()
        res.encoding = res.apparent_encoding
        print(res.text)
        return res.text
    except:
        return ''


def get_url(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/100.0.4896.127 Mobile Safari/537.36',
        'cookie': 'global_cookie=za5zsy2lt28klocfgx6nbc2en40l268jrt4; ASP.NET_SessionId=tpez4deakbuiluskavmf55r3; '
                  'zf_csrfcookie=OXvhIeXZPZinOTqYbVSr6zDdhroUdY1zHzrjsKyxO-uWtdGjeOXlWG8LxSinlcwbjqCCsw2; city=hn; '
                  'g_sourcepage=zf_fy%5Elb_pc; __utma=147393320.848879548.1650378176.1650378176.1650378176.1; '
                  '__utmc=147393320; __utmz=147393320.1650378176.1.1.utmcsr=search.fang.com|utmccn=('
                  'referral)|utmcmd=referral|utmcct=/; __utmt_t0=1; __utmt_t1=1; __utmt_t2=1; '
                  'Captcha'
                  '=2B39693538736E516C4A704539515843702F43795443624F7931686A6F556956537171766E79586750765A616E504542634C64626747647572712F355245752B4255722F4C746557766A6B3D; unique_cookie=U_za5zsy2lt28klocfgx6nbc2en40l268jrt4*2; __utmb=147393320.6.10.1650378176 '
    }
    r = requests.get(url, headers=headers)
    # print(r.text)
    new_text = r.text
    if r'<title>跳转...</title>' in new_text:
        result = re.findall(r'''<div\sclass="redirect".+?href="(.+?)".+?</ a>''', new_text, re.VERBOSE | re.DOTALL)
        newurl = result
        print(newurl)


def parseText(text):
    p1 = '<p class="font15 mt12 bold">(.{2,5})<span class="splitline">'
    pp1 = re.findall(p1, text, re.S)
    # print(pp1)


def main():
    # url="https://hn.zu.fang.com/"
    url = 'https://hn.zu.fang.com/house/i{}/'
    for x in range(31, 34):
        page_url = url.format(x)
        # print(page_url)
        new_url = get_url(page_url)
    text = getHTMLText(new_url)
    parseText(text)


if __name__ == '__main__':
    main()

'''
任务：爬取房天下租房信息第一页——第三页的租房模式、月租金、面积、房屋格局、房屋地点。
第二页https://hn.zu.fang.com/house/i32/?rfss=1-08b540092e1a81ab35-a2
第二页https://hn.zu.fang.com/house/i32/
第三页https://hn.zu.fang.com/house/i33/
第三页https://hn.zu.fang.com/house/i33/?rfss=1-4985c28fab1a042db2-a3
'''
