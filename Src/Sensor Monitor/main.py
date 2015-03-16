import androidhelper
import time
import json
import socket
import datetime

bOutputFile=False
bSendToServer=True
bOutputToScreen=False

ServerIP='10.101.1.246'
ServerPort=13373

if bOutputFile: outfile=open("sensors.log","wb")

ah= androidhelper.Android ()


while (True):
  SensorDict={}
  try:
    ah.startSensingTimed (1,250)
  except:
    print "StartSensing Exception. Sleeping 5 seconds"
    ah.stopSensing ()
    time.sleep(5)
    continue    
  
  SensorDict["ReadingTime"] = datetime.datetime.now().isoformat()
  SensorDict["accelerometer"] = ah.sensorsReadAccelerometer().result
  SensorDict["magnetometer"] = ah.sensorsReadMagnetometer().result
  SensorDict["orientation" ] = ah.sensorsReadOrientation().result
  
  for key in SensorDict:
    if bOutputToScreen: print key, SensorDict[key]
    if bOutputFile: outfile.write(json.dumps(SensorDict))
  
  if bSendToServer: 
    SensorDict["accelerometer"] = ah.sensorsReadAccelerometer().result
    SensorDict["magnetometer"] = ah.sensorsReadMagnetometer().result
    SensorDict["orientation" ] = ah.sensorsReadOrientation().result
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect((ServerIP, ServerPort))
      s.send(json.dumps(SensorDict))
      s.close()
    except:
      print "Send Failed"
      time.sleep(2)
    #result = s.recv(1024)
  
    #outfile.write(ah.sensorsGetAccuracy().result)
    #outfile.write(ah.sensorsReadAccelerometer().result)
    #outfile.write(ah.sensorsReadMagnetometer().result)
    #outfile.write(ah.sensorsReadOrientation().result)
    #outfile.write ("\n")
  
  #result = json.loads(s.recv(1024))
  ah.stopSensing ()
  #time.sleep (1)


if bOutputFile: outfile.close ()
s.close()



