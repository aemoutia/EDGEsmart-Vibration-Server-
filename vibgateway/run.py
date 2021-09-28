
from vibgatewaymodule import app, whitelistfunc as wl, sensornode as sns, paramsfunc as pr
import threading
import time

def runApp():
	app.run(debug=True, use_reloader=False, port=5000, host='0.0.0.0')


def runMain(sensor):
	sensor.main()

if __name__ == "__main__":
	t = threading.Thread(target=runApp).start()
	Thread_ID = 'None'
	UUID_list = wl.GetWhiteLIST()
	print(UUID_list)
	counter = 8

	while counter != 0 :
		time.sleep(1)
		Thread_ID = pr.getThreadID()

		if Thread_ID == UUID_list[0]:
			sensor01 = sns.SensorNode(Thread_ID)
			t01 = threading.Thread(target=runMain, args=(sensor01,), daemon=True).start()
			Thread_ID = 'None'
			counter = counter - 1

		elif Thread_ID == UUID_list[1]:
			sensor02 = sns.SensorNode(Thread_ID)
			t02 = threading.Thread(target=runMain, args=(sensor02,), daemon=True).start()
			Thread_ID = 'None'
			counter = counter - 1

		elif Thread_ID == UUID_list[2]:
			sensor03 = sns.SensorNode(Thread_ID)
			t03 = threading.Thread(target=runMain, args=(sensor03,), daemon=True).start()
			Thread_ID = 'None'
			counter = counter - 1

		elif Thread_ID == UUID_list[3]:
			sensor04 = sns.SensorNode(Thread_ID)
			t04 = threading.Thread(target=runMain, args=(sensor04,), daemon=True).start()
			Thread_ID = 'None'
			counter = counter - 1

		elif Thread_ID == UUID_list[4]:
			sensor05 = sns.SensorNode(Thread_ID)
			t05 = threading.Thread(target=runMain, args=(sensor05,), daemon=True).start()
			Thread_ID = 'None'
			counter = counter - 1

		elif Thread_ID == UUID_list[5]:
			sensor06 = sns.SensorNode(Thread_ID)
			t06 = threading.Thread(target=runMain, args=(sensor06,), daemon=True).start()
			Thread_ID = 'None'
			counter = counter - 1

		elif Thread_ID == UUID_list[6]:
			sensor07 = sns.SensorNode(Thread_ID)
			t07 = threading.Thread(target=runMain, args=(sensor07,), daemon=True).start()
			Thread_ID = 'None'
			counter = counter - 1

		elif Thread_ID == UUID_list[7]:
			sensor08 = sns.SensorNode(Thread_ID)
			t08 = threading.Thread(target=runMain, args=(sensor08,), daemon=True).start()
			Thread_ID = 'None'
			counter = counter - 1

		else:
			pass



















'''
sensor0022 = sns.SensorNode('aa:bb:cc:00:00:22')
sensor0033 = sns.SensorNode('aa:bb:cc:00:00:33')
sensor0044 = sns.SensorNode('aa:bb:cc:00:00:44')
#sensor0055 = sns.SensorNode('aa:bb:cc:00:00:55')
#sensor0066 = sns.SensorNode('aa:bb:cc:00:00:66')
#sensor0077 = sns.SensorNode('aa:bb:cc:00:00:77')
#sensor0088 = sns.SensorNode('aa:bb:cc:00:00:88')


t0011 = threading.Thread(target=runMain, args=(sensor0011,), daemon=True).start()
t0022 = threading.Thread(target=runMain, args=(sensor0022,), daemon=True).start()
t0033 = threading.Thread(target=runMain, args=(sensor0033,), daemon=True).start()
t0044 = threading.Thread(target=runMain, args=(sensor0044,), daemon=True).start()
#t0055 = threading.Thread(target=runMain, args=(sensor0055,), daemon=True).start()
#t0066 = threading.Thread(target=runMain, args=(sensor0066,), daemon=True).start()
#t0077 = threading.Thread(target=runMain, args=(sensor0077,), daemon=True).start()
#t0088 = threading.Thread(target=runMain, args=(sensor0088,), daemon=True).start()
'''

