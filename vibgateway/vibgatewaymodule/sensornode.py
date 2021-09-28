import random
import uuid
import json
import numpy as np
import math
from vibgatewaymodule import paramsfunc as pr, whitelistfunc as wl
#import paramsfunc as pr
#import whitelistfunc as wl
from datetime import datetime, timedelta
import time
import threading

class SensorNode:
	def __init__(self,  UUID):
		self.UUID = UUID
		self.calibration = 0.00195325
		self.dataPath = wl.getDeviceDataPath(self.UUID)
		self.sample_rate = int(pr.GetDevicePARAMS(self.UUID, 'sample_rate'))
		self.trace_length = int(pr.GetDevicePARAMS(self.UUID, 'trace_len'))
		self.wakeup_time = pr.GetDevicePARAMS(self.UUID, 'wakeup_time')
		self.wakeup_interval = pr.GetDevicePARAMS(self.UUID, 'wakeup_interval')

	def timeToseconds(self, time_str):
		self.time_str = time_str
		self.time_str = datetime.strptime(self.time_str, '%H:%M:%S')
		self.delta_time = self.time_str - datetime(1900,1,1)
		self.delta_sec = self.delta_time.total_seconds()
		return int(self.delta_sec)

	def getBatteryLevel(self):
		self.battery_level = round(random.uniform(3.27,3.28), 3)
		return self.battery_level

	def getTempValue(self):
		self.temp_value = round(random.uniform(25.0,26.0), 2)
		return self.temp_value

	def Rand_id_generator(self):
		self.ID = uuid.uuid4().hex
		self.ID = '{}-{}-{}-{}-{}'.format(self.ID[0:8], self.ID[8:12], self.ID[12:16], self.ID[16:20], self.ID[20:32])
		return self.ID

	def Time_stamp_iso(self):
		self.timestamp = datetime.now().isoformat() # ISO 8601
		self.timestamp_utc = str(datetime.utcnow().isoformat())+'Z' # ISO 8601 UTC
		return str(self.timestamp_utc)

	def vibGenerator(self, f1=22, f2=60, f3=100, mag1=6, mag2=7, mag3=4):
		self.f1 = f1
		self.mag1 = mag1
		self.f2 = f2
		self.mag2 = mag2
		self.f3 = f3
		self.mag3 = mag3

		UPPERLIMIT = (1/self.sample_rate) * self.trace_length
		TIME = np.linspace(0, UPPERLIMIT, self.trace_length)
		twf1 = self.mag1 * np.sin (2 * math.pi * self.f1 * TIME)
		twf2 = self.mag2 * np.sin (2 * math.pi * self.f2 * TIME)
		twf3 = self.mag3 * np.sin (2 * math.pi * self.f3 * TIME)
		noise = np.random.normal (0, 3, self.trace_length)
		time_data = twf1 + twf2 + twf3 + noise
		self.value = [int(time_data[i]/self.calibration) for i in range(0, self.trace_length)]
		return self.value

	def dataMeas(self):
		self.vibsensor = {'uuid': self.UUID,
				'name':'',
				'id': self.Rand_id_generator(),
				'time': datetime.now().isoformat(), #self.Time_stamp_iso(),
				'value' : self.vibGenerator(),
				'rate': self.sample_rate,
				'trace': self.trace_length,
				'count': 1,
				'gain': 1,
				'calibration': self.calibration,
				'temperature': self.getTempValue(),
				'battery': self.getBatteryLevel(),
				'axes': 1
				}
		self.writeToFile(self.vibsensor)


	def writeToFile(self, Vibsensor):
		self.Vibsensor = Vibsensor
		with open(self.dataPath+'/'+'data.json', 'w') as f:
			#self.content = json.dumps(self.Vibsensor, indent=4, sort_keys=True)
			self.content = json.dumps(self.Vibsensor)
			f.write(self.content)
			f.close()
		return True


	def main(self):
		self.currentTime = datetime.now()
		self.currentTime_str ="{}:{}:{}".format(self.currentTime.hour, self.currentTime.minute, self.currentTime.second)
		self.currentTimeSec = self.timeToseconds(self.currentTime_str)
		self.wakeup_timeSec = self.timeToseconds(self.wakeup_time)
		self.wakeup_intervalSec = self.timeToseconds(self.wakeup_interval)
		self.deltaSec = abs(self.wakeup_timeSec - self.currentTimeSec)
		while True:
			time.sleep(self.deltaSec)
			while True:
				self.dataMeas()
				time.sleep(self.wakeup_intervalSec)
		'''
		while True:
			if self.deltaSec < 0:
				while True:
					#Timestamp and backoff time before taking measurement
					self.dataMeas()
					time.sleep(self.wakeup_interval)
			if self.deltaSec > 0:
				time.sleep(self.deltaSec)
				while True:
					#Timestamp and backoff time before taking measurement
					self.dataMeas()
					time.sleep(self.wakeup_interval)
		'''
if __name__ == '__main__':
	s1 = SensorNode('aa:bb:cc:00:00:11')
	s1.main()
