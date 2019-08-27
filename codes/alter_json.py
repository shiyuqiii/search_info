import ujson


with open("./whed_database_all.json") as f:
    data = ujson.load(f)

data["22101"]['fullname'] = 'University of Chinese Academy of Sciences'

with open('./new_all.json', 'w') as f:
	ujson.dump(data, f)