import re
import glob
import json
import insert
import os

cmd = "mongodump --out=C:\\Users\\NITIN\\Desktop\\xml_files_parse\\bson_folder"

def readFile(filepath):
	with open(filepath, 'r', encoding="utf8") as content_file:
		content = content_file.read()
		return content

def getDataInstances(filepath):
	stri = readFile(filepath)
	iter_ = re.finditer(r"==.*==", stri)
	indices = [m.start(0) for m in iter_]

	dataPoints = []

	for i in range(len(indices)):
		if i+1 == len(indices):
			data = stri[indices[i]:]
		else:	
			data = stri[indices[i]:indices[i+1]]
		dataPoints.append(data)

	return dataPoints


def jsonify(data):
	json = {}

	#print(data)
	
	p = re.compile("\[\[User:.*\]\]")
	try:
		user = p.findall(data)[0][7:-2].split("|")[0]
	except:
		return None
	#print("user: ", user)
	json['username'] = user
	#print(data)


	p = re.compile("\[\[User:.*")
	#print(data)
	#print("\n\n\n")
	dateandtime = p.findall(data)[0].split("]")[-1]#.strip()
	#p = re.compile("[\d]{2}:[\d]{2},.*[\d]{4}")
	p = re.compile("[\d]{2}:[\d]{2}.*['UTC)]")

	#haha =dateandtime
	dateandtime = p.findall(dateandtime)#[0].strip()
	if(len(dateandtime) == 0):
		#print(dateandtime)
		#print(haha)
		#print(data)
		json['dateandtime'] = ''
	else:
		json['dateandtime'] = dateandtime[0].strip()

	#print("\n\ndateandtime: ", dateandtime)

	counter = 0
	data = data.strip()
	for i in data:
		if i == ':':
			counter += 1
		else:
			break

	json['depth'] = counter

	#p = re.compile("\[\[User:")
	iter_ = re.finditer(r"\[\[User:", data)
	indi = [m.start(0) for m in iter_][0]
	#print("indices: ", indices)
	textdata = data[:indi]
	textdata = textdata.strip(":")
	json['textdata'] = textdata
	return json


def extractInformation(data):
	#print(data)
	p = re.compile('==.*==')
	hd = p.findall(data)[0]
	header = (hd[2:-2]).strip(" =[]")
	#print(header)
	data = data[len(hd):]
	data = data.split("\n")

	finalDataPoints = []

	dummy = ''

	for item in data:
		if item == '':
			pass
		elif "[[User" not in item:
			dummy += item
		else:
			dummy += item
			finalDataPoints.append(dummy)
			dummy = ''

	jsonOutputArray = []

	for item in finalDataPoints:
		jsonOutput = jsonify(item)
		if jsonOutput is None:
			pass
		else:
			jsonOutput['header'] = header
			#print(jsonOutput)
			jsonOutputArray.append(jsonOutput)

	return jsonOutputArray, header



def parentify(jsonOutputArray, start_id):
	#print(jsonOutputArray[0])
	id_ = jsonOutputArray[0]['id']
	jsonOutputArray[0]['parent_id'] = 0
	for i in range(1, len(jsonOutputArray)):
		if jsonOutputArray[i]['depth'] > 0:
			jsonOutputArray[i]['parent_id'] = id_
			id_ = jsonOutputArray[i]['id']
		else:
			jsonOutputArray[i]['parent_id'] = 0
			id_ = jsonOutputArray[i]['id']


def giveIds(jsonOutputArray, start):
	for item in jsonOutputArray:
		item['id'] = start
		start += 1




if __name__ == "__main__":
	list_of_files = glob.glob("*.xml")
	#print(list_of_files)


	for file in list_of_files:
		dataPoints = getDataInstances(file)
		topic = file.split('.')[0]
		name = 'output/' + topic + '_output.json'
		print(name)
		f = open(name, 'a')
		for data in dataPoints:
			#print(data)
			jsonOutputArray, header = extractInformation(data)
			if len(jsonOutputArray) >= 1:
				giveIds(jsonOutputArray, 100)
				parentify(jsonOutputArray, 0)
				#print(header)
				for json_ in jsonOutputArray:
					#print(json_)
					print(json.dumps(json_), file = f)
					#print("\n\n")
					#x = 5
				#break
				#print("\n\n\n\n\n\n\n")

		
		
		#break

		insert.insert_into_database(name, topic)
	print("cmd: ", cmd)
	os.system(cmd)




