import json
import os
whitelist_path = "/home/aemoutia/vibgateway"
data_path   = '/home/aemoutia/vibgateway/devicedata'
params_path = '/home/aemoutia/vibgateway/deviceparams'
suffix = '.json'


def createDataFolderUUID(uuid):
	last4digits = uuid.split(':')[4:]
	folder_name = 'device'+last4digits[0]+last4digits[1]
	dir_path = os.path.join(data_path , folder_name)
	#print(os.path.join(dir_path , file_name + suffix))
	if not os.path.exists(dir_path):
		os.makedirs(dir_path)
		return dir_path
	else:
		return dir_path


def createParamsFolderUUID(uuid):
	last4digits = uuid.split(':')[4:]
	folder_name = 'device'+last4digits[0]+last4digits[1]
	dir_path = os.path.join(params_path , folder_name)
	#print(os.path.join(dir_path , file_name + suffix))
	if not os.path.exists(dir_path):
		os.makedirs(dir_path)
		return dir_path
	else:
		return dir_path


#print(createDataFolderUUID('aa:bb:cc:00:00:11'))
#print(createParamsFolderUUID('aa:bb:cc:00:00:11'))

def readFromFile():
	dir_path = os.path.join(whitelist_path, 'whitelist.txt')
	with open(dir_path, 'r') as f:
		dict_obj = {}
		for line in f:
			line_text = line.split()
			if line_text:
				key = line_text[0]
				value = line_text[1:]
				dict_obj[int(key)] = value
			else:
				f.close()
				break
		f.close()
	return dict_obj


def writeToFile(dict_obj):
	with open(whitelist_path+'/'+'whitelist.txt', 'w') as f:
		for key, val in dict_obj.items():
			f.write('%s %s %s %s\n' % (key, val[0], val[1], val[2]))
		f.close()
	return True




def IsSensorInWhitelist(uuid):
	dict_obj = readFromFile()
	list_obj = list(dict_obj.values())
	print(list_obj)
	for i in list_obj:
		if uuid == i[0]:
			return True
			break
		else:
			continue
	return False


#print(IsSensorInWhitelist('aa:bb:cc:00:00:11'))


def addToWhitelist(uuid):
	content = {}
	data_dir_path = createDataFolderUUID(uuid)
	params_dir_path = createParamsFolderUUID(uuid)
	if(IsSensorInWhitelist(uuid) == False):
		dict_obj = readFromFile()
		for key, val in dict_obj.items():
			if val[0] == 'None':
				val = []
				val.append(uuid)
				val.append(data_dir_path)
				val.append(params_dir_path)
				dict_obj[key] = val
				writeToFile(dict_obj)
				content = {'success':True,'code':202,'type':'info','message':'Device Whitelist', 'Added': uuid}
				break
	else:
		pass
	return json.dumps(content)
	#return True


def getWhitelist():
	whitelist = []
	dict_obj = readFromFile()
	list_obj = list(dict_obj.values())
	for i in list_obj:
		whitelist.append(i[0])
	content = {'whitelist' : whitelist}
	return json.dumps(content)
	


def removeFromWhitelist(uuid):
	content = {}
	dict_obj = readFromFile()
	for key, val in dict_obj.items():
		if uuid == val:
			dict_obj[key] = 'None'
			writeToFile(dict_obj)
			list_obj = list(dict_obj.values())
			whitelist = list_obj
			content = {'success':True,'code':202,'type':'info','message':'Device Whitelist', 'Removed': uuid}
			break
	return json.dumps(content)


def GetWhiteLIST():
	whitelist = []
	dict_obj = readFromFile()
	list_obj = list(dict_obj.values())
	for i in list_obj:
		whitelist.append(i[0])
	return whitelist


def getDeviceDataPath(uuid):
	dict_obj = readFromFile()
	list_obj = list(dict_obj.values())
	for i in list_obj:
		if uuid == i[0]:
			return i[1]
		else:
			continue

def getDeviceParamsPath(uuid):
	dict_obj = readFromFile()
	list_obj = list(dict_obj.values())
	for i in list_obj:
		if uuid == i[0]:
			return i[2]
		else:
			continue

if __name__ == '__main__':
	#print(readFromFile())
	#print(getDeviceDataPath('aa:bb:cc:00:00:22'))
	#print(getDeviceParamsPath('aa:bb:cc:00:00:22'))
	print(getWhitelist())


