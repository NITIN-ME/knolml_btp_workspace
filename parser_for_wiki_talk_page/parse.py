import re


def readFile(filepath):
	with open(filepath, 'r') as content_file:
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
	
	p = re.compile("\[\[User:.*\]\]")
	user = p.findall(data)[0][7:-2].split("|")[0]
	#print("user: ", user)
	json['username'] = user
	#print(data)


	p = re.compile("\[\[User:.*")
	dateandtime = p.findall(data)[0].split("]")[2].strip()
	#print("dateandtime: ", dateandtime)
	json['dateandtime'] = dateandtime

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
	header = (hd[2:-2]).strip()
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
		jsonOutput['header'] = header
		#print(jsonOutput)
		jsonOutputArray.append(jsonOutput)

	return jsonOutputArray, header

def createXMLFromJson(data):
	stri = """
		<comment username = {} time = {} depth = {}>""".strip().format(data['username'], data['dateandtime'], data['depth'])+ "\n" +"""
		{}""".strip().format(data['textdata']) + "\n" + """
		</comment>
	""".strip()
	stri = stri.strip()
	return stri

def createXML(xmlArray, header):
	for item in xmlArray:
		print(item)
		print("\n\n")


def giveIds(jsonOutputArray, start):
	for item in jsonOutputArray:
		item['id'] = start
		start += 1


def parentify(jsonOutputArray, start_id):
	id_ = jsonOutputArray[0]['id']
	jsonOutputArray[0]['parent_id'] = 0
	for i in range(1, len(jsonOutputArray)):
		if jsonOutputArray[i]['depth'] > 0:
			jsonOutputArray[i]['parent_id'] = id_
			id_ = jsonOutputArray[i]['id']
		else:
			jsonOutputArray[i]['parent_id'] = 0
			id_ = jsonOutputArray[i]['id']



if __name__ == "__main__":
	
	dataPoints = getDataInstances("Talk_History_of_Greece.txt")

	"""
	for item in dataPoints:
		print(item)
		print("\n\n")
	"""

	data = dataPoints[100]
	jsonOutputArray, header = extractInformation(data)

	xmlArray = []
	for item in jsonOutputArray:
		xmlvalue = createXMLFromJson(item)
		#print(xmlvalue)
		xmlArray.append(xmlvalue)
		#print(item)
		#print("\n\n")

	#print("header: ", header)


	#for item in dataPoints:
	#	extractInformation(item)
	giveIds(jsonOutputArray, 100)
	parentify(jsonOutputArray,0)

	for item in jsonOutputArray:
		print(item)
		print("\n\n")
	


