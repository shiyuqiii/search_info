# -*- coding: UTF-8 -*-
from __future__ import division
import glob
import os
import Levenshtein
from pdf_extractor import extract_pdf_content
import re
from read_json import get_uni_list
import difflib
import json
import os.path


def get_content_list():
	#指定pdf路径
	pdf_path = "/root/dataset/test/pdf/"
	#获得所有pdf路径
	pdfs = glob.glob("{}/*.pdf".format(pdf_path))
	#把从第一篇pdf中抽取的文本内容保存在content变量里
	return pdfs


def word_distance(s, t):
    s = s.lower().strip()
    t = t.lower().strip()
    d = Levenshtein.distance(s, t)
    return d


def word_equal(s, t):
    return word_distance(s, t) <= 1


def get_uni_context(pdfs, n):
	
	content = extract_pdf_content(pdfs[n])
	#找到content中所有的单词，考虑's以及-的情况
	content = re.sub(r'\-\n+','',content)
	content = re.sub(r'\n+',' ',content)
	#print(content)
	words_list = re.findall(r"[a-zA-Z|'\'''\-'']+", content)
	#print(type(words_list))
	#print(len(words_list))

	#获得所有学校的下标
	uni_index = [idx for idx, value in enumerate(words_list) if word_equal(value,'University') or word_equal(value,'Institute')]
	#获得所有学校的上下文信息	
	#print(uni_index) #输出“Univeristy”关键词在文章中的位置
	uni_context = {}
	for i in range(len(uni_index)):
		if uni_index[i]-15 > 0:
			uni_context[i] = [item.lower() for item in words_list[uni_index[i]-15 : uni_index[i]+15]]
		else:
			uni_context[i] = [item.lower() for item in words_list[0 : uni_index[i]+15]]

	return uni_context


def macth_uni_name2():
	university = {}
	pdfs = get_content_list()
	#print(pdfs)
	'''
	for n in range(len(pdfs)):
		pdf_name = os.path.basename(pdfs[n])
		pdf_name = os.path.splitext(pdf_name)[0]
		
		if pdf_name == '1901.00001':
			print(n)
	'''
	#for n in range(len(pdfs)):
		#uni_context[i]表示这篇文章中出现的第i个学校的上下文信息
	uni_context = get_uni_context(pdfs, 28)
	pdf_name = os.path.basename(pdfs[28])
	pdf_name = os.path.splitext(pdf_name)[0]
	print(pdf_name)

	#uni_list 保存的是世界大学名单
	uni_list = get_uni_list()
	#uni_list[5483]
	print(len(uni_context))
	for k in range(len(uni_context)):
		print(uni_context[k])
	begin = 0
	for j in uni_list:
		for i in range(len(uni_context)):
			uni_name = uni_list[j]['fullname'].lower().split()
			matcher = difflib.SequenceMatcher(None, uni_context[i], uni_name)
			eps = 1e-2
			threshold = 2 * len(uni_name) / (len(uni_name)\
				+ len(uni_context[i])) - eps
			longest_match = matcher.find_longest_match(0, len(uni_context[i]), 0, len(uni_name))
			if matcher.ratio() >= threshold and longest_match.size >= len(uni_name):
				print(matcher.ratio())
				print(threshold)
				#print(uni_context[i])
				if begin == 0:
					print(uni_list[j]['fullname'])
					university.setdefault(pdf_name, []).append(uni_list[j]['fullname'])
					begin = 1
				else:
					if uni_list[j]['fullname'] not in university[pdf_name]:
						print(uni_list[j]['fullname'])
						university.setdefault(pdf_name,[]).append(uni_list[j]['fullname'])
					
	extract_university = {"affliation":university}
	with open('./extract_university.json', 'w') as f:
		json.dump(extract_university, f)


if __name__ == "__main__":
	#macth_uni_name()
	#get_content_list()
	macth_uni_name2()
	






#uni_number = words_list.count('University')#关键词"University"的个数
#uni_list保存所有'University'关键词的下标
#uni_index = [idx for idx, value in enumerate(words_list) if value=='University']
#print(uni_index)

