import json
import os.path

pdfs = ['/root/dataset/test/pdf/1901.00563.pdf', '/root/dataset/test/pdf/1901.00675.pdf']
uni_name = ['Institute of Technology', 'Institute of Technology', 'Polytechnic University']

dic = {}
for i in range(len(pdfs)):
	for j in range(len(uni_name)):
		new = os.path.basename(pdfs[i])
		new = os.path.splitext(new)[0]
		if j == 0:
		#if uni_name[j] not in dic[pdfs[i]]:
			dic.setdefault(new,[]).append(uni_name[j])
		else:
			if uni_name[j] not in dic[new]:
				print(new)
				dic.setdefault(new,[]).append(uni_name[j])

#print(dic["/root/dataset/test/pdf/1901.00563.pdf"])
print(dic)
with open('./test.json', 'w') as f:
    json.dump(dic, f)