import pymongo
import json

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

#print(myclient.list_database_names())


def insert_into_database(name, topic):
	#print("name: ", name)
	#print("topic: ", topic)

	mongoClientDB = myclient['mywikidump']
	collection = mongoClientDB[topic]
	topic = topic + '.xml'
	json_file = open(name,  encoding="utf8")
	array = [line[:-1] for line in json_file]
	array[-1] = array[-1] + "}"
	#json_file = json.dumps(json_file)
	#data = json.load(json_file)
	#print(array)

	final_array = []

	#for item in array:
		#final_array.append(json.loads(item))

	#print(final_array)
	#collection.insert_many(array, ordered=False)


	for item in array:
		#pass
		#print("item: ", item)
		ins = json.loads(item)
		collection.insert(ins)