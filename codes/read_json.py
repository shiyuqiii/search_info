import ujson


def get_uni_list():
	with open ("/root/dataset/train/new_all.json") as f:
		temp = ujson.load(f)
		#print(len(temp))
	return temp
