# -*- coding: UTF-8 -*-
import glob
import os
from pdf_extractor import extract_pdf_content
import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

#指定pdf路径
pdf_path = "/root/dataset/shi_test1/"
#获得所有pdf路径
pdfs = glob.glob("{}/*.pdf".format(pdf_path))

print(pdfs)
#把从第一篇pdf中抽取的文本内容保存在content变量里
content = extract_pdf_content(pdfs[0])
#将文本内容转化为单词列表
words_list = re.findall(r"[a-zA-Z]\w+", content)
#不想要其出现的符号
#punctuations = ['(',')',',',';',':','[',']']
stop_words = stopwords.words('the','a','an','and')
keywords = [word for word in words_list if word in stop_words]
#print(words_list)
print(keywords)
#print(len(words_list))
