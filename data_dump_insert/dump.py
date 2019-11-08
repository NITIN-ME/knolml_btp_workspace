import pymongo
import json

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

print(myclient.list_database_names())


mongoClientDB = myclient['mywikidump']
collection = mongoClientDB['mywikicollection']
json_file = open('data.json')
array = [line[:-1] for line in json_file]
#json_file = json.dumps(json_file)
#data = json.load(json_file)
#print(array)

final_array = []

#for item in array:
	#final_array.append(json.loads(item))

#print(final_array)
#collection.insert_many(array, ordered=False)


for item in array:
	#print(item)
	ins = json.loads(item)
	collection.insert(ins)