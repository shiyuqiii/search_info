import requests
import glob
import os
import ujson
from bs4 import BeautifulSoup
import re
import time


fields = ["Engineering", "Information Sciences", "Mathematics and Computer Science", "Technology"]
totalNum = [9970, 8519, 9080, 4673]


def get_short_name(s):
    p1 = re.compile(r'[(](.*?)[)]', re.S)
    return re.findall(p1, s)


def extract_information_from_html(contents):
    soup = BeautifulSoup(contents)
    odd_ret = soup.findAll('li', {'class': 'odd clearfix plus'})
    even_ret = soup.findAll('li', {'class': 'even clearfix plus'})

    uni_ret = odd_ret + even_ret

    result = {}
    for i in uni_ret:
        uid = i.contents[1].contents[1].contents[0].attrs["id"]
        tmp = dict( 
                    fullname=i.contents[3].contents[3].contents[1].contents[2].strip(),
                    location=i.contents[3].contents[1].contents[0].strip(),
                    alias=i.contents[3].contents[5].contents[0].strip(),
                    abbr=get_short_name(i.contents[3].contents[5].contents[0].strip())
                )
        result[uid] = tmp

    member_ret = soup.findAll('li', {'class': 'iaumember clearfix plus'})
    for i in member_ret:
        uid = i.contents[1].contents[1].contents[0].attrs["id"]
        tmp = dict(
                fullname=i.contents[3].contents[5].contents[1].contents[2].strip(),
                location=i.contents[3].contents[1].contents[0].strip(),
                alias=i.contents[3].contents[7].contents[0].strip(),
                abbr=get_short_name(i.contents[3].contents[7].contents[0].strip())
              )
        result[uid] = tmp
    return result


def do_crawler(fid):
    url = "https://whed.net/results_institutions.php?Chp2=%s" % fields[fid].replace(" ", "%20")
    headers = {
        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        "Accept-Encoding":"gzip, deflate, br",
        "Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,ja;q=0.7",
        "Cache-Control":"max-age=0",
        "Connection":"keep-alive",
        "Host":"whed.net",
        "Origin":"https://whed.net",
        "Referer":"https://whed.net/results_institutions.php?Chp2=%s" % fields[fid].replace(" ", "%20"),
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36"
    }

    form_data = {
        "where":"(FOS LIKE '%|" + fields[fid] + "|%')",
        "requete":"(Fields of study=%s)" % fields[fid],
        "total":"%d" % totalNum[fid],
        "ret":"home.php",
        "quick":"0",
        "Chp0":"",
        "debut":"0",
        "use":"",
        "afftri":"yes",
        "stat":"Fields of study",
        "sort":"InstNameEnglish,iBranchName",
        "nbr_ref_pge":"100"
    }

    debut = 0
    result = {}
    while debut < totalNum[fid]:
        form_data["debut"] = str(debut)
        debut += 100
        response = requests.post(url, headers=headers, data=form_data)

        contents = response.text
        tmp_result = extract_information_from_html(contents)

        print(debut, len(tmp_result))
        result.update(tmp_result)
        # time.sleep(2)

    with open("whed_database_%s.json" % fields[fid].replace(" ", ""), "w") as f:
        ujson.dump(result, f)


def merge_all():
    file_list = ["whed_database_%s.json" % field.replace(" ", "") for field in fields]
    result = {}
    for filename in file_list:
        with open(filename, "r") as f:
            contents = ujson.load(f)
            result.update(contents)
    return result


# do_crawler(2)

result = merge_all()
print(len(result))
with open("whed_database_all.json", "w") as f:
    ujson.dump(result, f)
