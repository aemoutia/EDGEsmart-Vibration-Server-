from vibgatewaymodule import whitelistfunc as wl
#import whitelistfunc as wl

import json

#params_list = []
params_dict = {'mode':'None', 'sample_rate':'None', 'trace_len':'None', 'wakeup_level':'None',
               'wakeup_interval':'None', 'trigger_delay':'None', 'wakeup_time':'None', 'time':'None'}


ThreadID = 'None'

def readFromParamsFile(uuid):
	params_path = wl.getDeviceParamsPath(uuid)
	with open(params_path+'/'+'params.txt', 'r') as f:
		dict_obj = {}
		for line in f:
			if line.strip():
				key, val = line.split()
				dict_obj[key] = val
			else:
				f.close()
				break
		f.close()
	return dict_obj    


def readFromDataFile(uuid):
	data_path = wl.getDeviceDataPath(uuid)
	with open(data_path+'/'+'data.json', 'r') as f:
		content = f.read()
		f.close()
	return content


def writeToFile(params_path, dict_obj):
	with open(params_path+'/'+'params.txt', 'w') as f:
		for key, val in dict_obj.items():
			#f.write('%s %s\n' % (key, val))
			f.write('{} {}\n'.format(key, val))
		f.close()
	return True



def configureDevice(uuid, dict_params):
	params_path = wl.getDeviceParamsPath(uuid)
	writeToFile(params_path, dict_params)
	content = {'success':True,'code':200,'type':'info','message':'Scheduled to commit configuration update '+uuid}
	return json.dumps(content)

def getDeviceParameter(uuid, param_name):
	dict_obj = readFromParamsFile(uuid)
	value =  dict_obj[param_name]
	content = {param_name:value}
	return json.dumps(content)

def setDeviceParameter(uuid, param_name, value):
	dict_obj = readFromParamsFile(uuid)
	dict_obj[param_name] = value
	params_path = wl.getDeviceParamsPath(uuid)
	writeToFile(params_path, dict_obj)
	content = {"success":True, "code":202}
	return json.dumps(content)

def GetDevicePARAMS(uuid, param_name):
	dict_obj = readFromParamsFile(uuid)
	value = dict_obj[param_name]
	return value


def getLatestDeviceReading(uuid):
	return readFromDataFile(uuid)


def runThreadID(uuid):
	global ThreadID
	ThreadID = uuid
	content = {'success':True,'code':200,'type':'info','message':'Sent Command ['+uuid+'] : Release'}
	return json.dumps(content)

def getThreadID():
	global ThreadID
	return ThreadID

if __name__ == '__main__':
	uuid = 'aa:bb:cc:00:00:11'
	param_name = 'mode'
	#print(getDeviceParameter(uuid, param_name))
	#print(readFromFile())
	#print(getDeviceParam())
	#configureDevice(uuid, params_dict)
	#print(getDeviceParam('aa:bb:cc:00:11:20', 'mode'))
	#setDeviceParam('aa:bb:cc:00:11:20', 'mode', 'manual')
	#print(readFromFile(uuid))
	print(readFromDataFile(uuid))
