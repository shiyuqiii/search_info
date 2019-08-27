import requests
import glob
import os
from bs4 import BeautifulSoup


url = "http://arxiv.org/list/cs.CV/1903?show=50"
headers = {
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
    "Accept-Encoding":"gzip, deflate, br",
    "Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,ja;q=0.7",
    "Cache-Control":"max-age=0",
    "Connection":"keep-alive",
    "Host":"arxiv.org",
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36"
}


response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text)
href_list = soup.findAll('span', {'class': 'list-identifier'})
paper_urls = []
filenames = []

for href in href_list:
    paper_url = "http://arxiv.org" + href.contents[2].attrs["href"] + ".pdf"
    paper_urls.append(paper_url)
    filename = href.contents[2].attrs["href"] + ".pdf"
    filenames.append(filename[1:])

if os.path.isdir("pdf"):
    downloaded_files = glob.glob("pdf/*.pdf")
else:
    downloaded_files = []
    os.mkdir("pdf")

for paper_url, filename in zip(paper_urls, filenames):
    if filename in downloaded_files:
        print("%s downloaded" % filename)
        continue
    else:
        print("Downloading %s" % paper_url)
    response = requests.get(paper_url, headers=headers)
    content = response.content
    f = open(filename, "wb")
    f.write(content)
    f.close()
