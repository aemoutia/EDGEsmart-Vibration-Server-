from vibgatewaymodule import app, whitelistfunc as wl, paramsfunc as pr, sensornode as sns
from flask import request
from datetime import datetime
import json

@app.route("/sys/time",methods=['GET'])
def GetTime():
	content = {'Content' : datetime.now().isoformat()}
	return json.dumps(content) 

@app.route("/whitelist",methods=['POST'])
def AddToWhitelist():
	data_in = request.data.decode("utf-8")
	return wl.addToWhitelist(data_in)

@app.route("/whitelist",methods=['GET'])
def GetWhitelist():
	return wl.getWhitelist()

@app.route("/device/<uuid>/configure",methods=['PUT'])
def configureDevice(uuid):
	data_in = request.form.to_dict()
	return pr.configureDevice(uuid, data_in)

@app.route("/device/<uuid>/commit",methods=['GET'])
def CommitChangesToDevie(uuid):
	return pr.runThreadID(uuid) 

@app.route("/device/<uuid>/parameter",methods=['GET'])
def GetDeviceParameter(uuid):
	data_in = request.data.decode("utf-8")
	return pr.getDeviceParameter(uuid, data_in)

@app.route("/device/<uuid>/parameter/<parameter_name>",methods=['PUT'])
def SetDeviceParameter(uuid, parameter_name):
	data_in = request.data.decode("utf-8")
	return pr.setDeviceParameter(uuid, parameter_name, data_in)

@app.route("/device/<uuid>/cache/latest",methods=['GET'])
def GetLatestDeviceReading(uuid):
	data_in = request.data.decode("utf-8")
	return pr.getLatestDeviceReading(uuid)
