import ujson
import Levenshtein



def word_distance(s, t):
    s = s.lower().strip()
    t = t.lower().strip()
    d = Levenshtein.distance(s, t)
    return d


def word_equal(s, t):
    return word_distance(s, t) <= 1


#with open("./ground_truth.json") as f:
with open("./new_all.json") as f:
#with open("./extract_university.json") as f:
    data = ujson.load(f)

for i in data:
	if "Queen's University" in data[i]['fullname']:
	#if word_equal(data[i]['fullname'], "Queen's University"): 
		print(i, data[i]['fullname'])
#for x in data:
#	print(x, data[x])

