import pymongo
import json

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mongoClientDB = myclient['mywikidump']




def getAllauthors(topic):
	mycol = mongoClientDB[topic]
	st = set()
	for item in mycol.find():
		aut = item['username']
		st.add(aut)
	return st


def getAllCommentofAuthor(topic, authorname):
	mycol = mongoClientDB[topic]
	arr = []
	for item in mycol.find({'username':authorname}):
		arr.append(item)
	return arr


def getAuthorWithMostContribution(topic):
	author_list = list(getAllauthors(topic))
	max_author = ''
	mx = 0
	for author in author_list:
		arr = getAllCommentofAuthor(topic, author)
		if(len(arr) > mx):
			mx = len(arr)
			max_author = author
	return max_author


def findAllSections(topic):
	mycol = mongoClientDB[topic]
	st = set()
	for item in mycol.find():
		aut = item['header']
		st.add(aut)
	return st


print(getAllauthors('Torque'))
print("\n\n")
print("max_author: ", getAuthorWithMostContribution('Torque'))
print("\n\n")
arr = getAllCommentofAuthor('Torque', 'Sbyrnes321')


print("\n\n\n\n")
for item in arr:
	print(item)
	print("\n\n\n\n")

print("\n\n\n")

arr = findAllSections('Torque')

print(arr)