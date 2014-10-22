try:
	import androidhelper as android
except:
	import android
import datetime
import time
import json
import os.path

iLoggingInterval=15
fLog=file("/sdcard/sensorlog.txt","w")
fLog2=file("/sdcard/sensorlog2.txt","w")
dSensorReadings={}

myDevice=android.Android()
#myDevice.startSensingThreshold(1,4,7)
#myDevice.startSensingThreshold(2,4,7)
#myDevice.startSensingThreshold(3,4,7)
#print datetime.datetime.utcnow()
myDevice.startSensingTimed(1,iLoggingInterval*1000)
#fLog.write("Test")
#print dir(myDevice.readSensors())
#print "readsensors"
#print myDevice.readSensors()

#for i in range(10):
while not os.path.exists ("/sdcard/stop.txt"):
	'''
	print "sensorsGetAccuracy"
	print myDevice.sensorsGetAccuracy()
	print "sensorsReadAccelerometer"
	print myDevice.sensorsReadAccelerometer()
	print "sensorsReadMagnetometer"
	print myDevice.sensorsReadMagnetometer()
	print "sensorsReadOrientation"
	print myDevice.sensorsReadOrientation()
	'''
	oSensorAccur= myDevice.sensorsGetAccuracy()
	oSensorAccel=myDevice.sensorsReadAccelerometer()
	oSensorMag=myDevice.sensorsReadMagnetometer()
	oSensorOrient = myDevice.sensorsReadOrientation()
	dSensorReadings.update(SampleTime=datetime.datetime.now().isoformat(),Accuracy=oSensorAccur.result,Accelerometer=oSensorAccel.result,Magnetometer=oSensorMag.result,Orientation=oSensorOrient.result)
	jSensors=json.dumps(dSensorReadings)
	json.dumps(dSensorReadings,fLog)
	fLog.flush()
	#print jSensors
	fLog2.write(jSensors)
	fLog2.flush()
	time.sleep(iLoggingInterval)

	
myDevice.stopSensing()	
fLog.close()
fLog2.close()
print "Done"