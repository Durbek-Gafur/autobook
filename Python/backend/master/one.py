import threading 
import os
import sys 
import signal
import requests
import json
import time
import datetime
import ssl
from ddata import *
from cookies import *
# from datetime import datetime
from pytz import timezone


# from requests.packages.urllib3.exceptions import InsecureRequestWarning

# requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
un={ 
	'Accept' : 'application/json, text/*',
	'User-Agent' : 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Mobile Safari/537.36',
	'credentials' : 'same-origin',
	'Sec-Fetch-Site' : 'same-origin',
	'Sec-Fetch-Mode' : 'cors',
	'Referer' : 'https://relay.amazon.com/tours/loadboard?',
	'Accept-Encoding' : 'gzip, deflate, br',
	'Accept-Language' : 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,cy;q=0.6',
	'Cookie' : cookiesUpdate
	   }

getLoadHeader={ #abici 
		'x-csrf-token' : csrf, 
		'Content-Type' : 'application/json', 
		'Accept' : 'application/json, text/*',
		'User-Agent' : 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Mobile Safari/537.36',
		'credentials' : 'same-origin',
		'Sec-Fetch-Dest': 'empty',
		'Sec-Fetch-Site' : 'same-origin',		
		'Connection': 'keep-alive',
		'Sec-Fetch-Mode' : 'cors',
		'Referer' : 'https://relay.amazon.com/tours/loadboard?',
		'Accept-Encoding' : 'gzip, deflate, br',
		'Accept-Language' : 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,cy;q=0.6',
		'Cookie' : cookiesBook
	   }

# _ALL=111111111
ALLHEADERS=[un]
FINISH=False
NUM_MACHINES=1
# MACHINES=["U1"]
MACHINES=[
	{
		"name":"U1a",
		"ip":"http://ec2-34-229-50-189.compute-1.amazonaws.com",
		"errorCount": 0.0,
		"properCount": 0.000001,
		"ttt": 0,
		"averageDuration": 0.0
	}
	# ,
	# {
	# 	"name":"U2b",
	# 	"ip":"http://ec2-3-234-146-201.compute-1.amazonaws.com",
	# 	"errorCount": 0.0,
	# 	"properCount": 0.000001,
	# 	"ttt": 0,
	# 	"averageDuration": 0.0
	# },
	# {
	# 	"name":"U3c",
	# 	"ip":"http://ec2-54-147-130-1.compute-1.amazonaws.com",
	# 	"errorCount": 0.0,
	# 	"properCount": 0.000001,
	# 	"ttt": 0,
	# 	"averageDuration": 0.0
	# },
	# 	{
	# 	"name":"U4d",
	# 	"ip":"http://ec2-34-204-52-92.compute-1.amazonaws.com",
	# 	"errorCount": 0.0,
	# 	"properCount": 0.000001,
	# 	"ttt": 0,
	# 	"averageDuration": 0.0
	# },
	# {
	# 	"name":"U5e",
	# 	"ip":"http://ec2-34-224-63-125.compute-1.amazonaws.com",
	# 	"errorCount": 0.0,
	# 	"properCount": 0.000001,
	# 	"ttt": 0,
	# 	"averageDuration": 0.0
	# },
	# {
	# 	"name":"U6f",
	# 	"ip":"http://ec2-35-175-133-139.compute-1.amazonaws.com",
	# 	"errorCount": 0.0,
	# 	"properCount": 0.000001,
	# 	"ttt": 0,
	# 	"averageDuration": 0.0
	# }
	# ,
	# {
	# 	"name":"U3",
	# 	"ip":"http://ec2-34-229-50-189.compute-1.amazonaws.com",
	# 	"errorCount": 0.0,
		# "properCount": 0.0000001,
	# 	"averageDuration": 0.0
	# },
	# 	{
	# 	"name":"U4",
	# 	"ip":"http://ec2-34-229-50-189.compute-1.amazonaws.com",
	# 	"errorCount": 0.0,
		# "properCount": 0.0000001,
	# 	"averageDuration": 0.0
	# },
	# {
	# 	"name":"U5",
	# 	"ip":"http://ec2-34-229-50-189.compute-1.amazonaws.com",
	# 	"errorCount": 0.0,
		# "properCount": 0.0000001,
	# 	"averageDuration": 0.0
	# },
	# {
	# 	"name":"U6",
	# 	"ip":"http://ec2-34-229-50-189.compute-1.amazonaws.com",
	# 	"errorCount": 0.0,
		# "properCount": 0.0000001,
	# 	"averageDuration": 0.0
	# },
	# 	{
	# 	"name":"U7",
	# 	"ip":"http://ec2-34-229-50-189.compute-1.amazonaws.com",
	# 	"errorCount": 0.0,
		# "properCount": 0.0000001,
	# 	"averageDuration": 0.0
	# },
	# {
	# 	"name":"U8",
	# 	"ip":"http://ec2-34-229-50-189.compute-1.amazonaws.com",
	# 	"errorCount": 0.0,
		# "properCount": 0.0000001,
	# 	"averageDuration": 0.0
	# },
	# {
	# 	"name":"U9",
	# 	"ip":"http://ec2-34-229-50-189.compute-1.amazonaws.com",
	# 	"errorCount": 0.0,
		# "properCount": 0.0000001,
	# 	"averageDuration": 0.0
	# },
	# {
	# 	"name":"U10",
	# 	"ip":"http://ec2-34-229-50-189.compute-1.amazonaws.com",
	# 	"errorCount": 0.0,
		# "properCount": 0.0000001,
	# 	"averageDuration": 0.0
	# }
]
IPS=["http://ec2-34-229-50-189.compute-1.amazonaws.com"]
FREQUENCY=1
FINISH= False
carrierPerformanceCategory="HIGH"
priorityAccessVersion="priorityAccessVersion2"
SES=requests.Session() #NEED TO LOOP AND CREATE ARRAY OF SESSIONS LOOP ACCORDIN TO THE NUMBER OF MACHINES
data={
	"header": json.dumps(un),
	"url": url,
	"carrierPerformanceCategory":carrierPerformanceCategory,
	"priorityAccessVersion":priorityAccessVersion,
	"getLoadHeader":json.dumps(getLoadHeader)
}

def update(machineIndex,header):  
	global data
	global un
	global FINISH
	global MACHINES
	global STRINGTOPRINT

	thisMachine=MACHINES[machineIndex]
	r = thisMachine["session"].post((thisMachine["ip"]+"/one"), data=data, headers=header) #thisMachine["session"]
	returnJson=json.loads(r.text)
	# summary = "\t".join([thisMachine["name"],str(returnJson["counter"]),  str(returnJson["isbot"]), str(returnJson["carrierEngagementCategory"]), str(returnJson["askSentAt"]), str(returnJson["askDur"]), str(returnJson["askStatus"]), str(returnJson["booked"])])
	if returnJson["askStatus"] !=200:
		thisMachine["errorCount"]=thisMachine["errorCount"]+1
	else:
		thisMachine["properCount"]=thisMachine["properCount"]+1
		thisMachine["ttt"]=thisMachine["ttt"]+returnJson["askDur"]
		if returnJson["booked"]=="None":
			ll=1
		# print("None")
		else:
			print("There was new load")
			FINISH=True
	errorPercentage=round((thisMachine["errorCount"]/thisMachine["properCount"]*100),2)	
	averageDuration=int(thisMachine["ttt"]/thisMachine["properCount"])
	summary = "\t".join([thisMachine["name"],str(returnJson["counter"]),  str(returnJson["isbot"]), str(returnJson["carrierEngagementCategory"]), str(returnJson["askSentAt"]), str(returnJson["askDur"]), (str(averageDuration)+"-"+thisMachine["name"]), str(returnJson["askStatus"]), str(errorPercentage), str(returnJson["booked"])])
	print(summary+" "+STRINGTOPRINT)
	return



if __name__ == "__main__": 
	# global STRINGTOPRINT
	# global url
	SES=requests.Session()
	x=-1
	t1=time.time()
	delay = 1/FREQUENCY
	headersLen=len(ALLHEADERS)
	machineLen=len(MACHINES)

	######################################################################################
		######################################################################################
			######################################################################################
	# if len(sys.argv)>2:
	# 	url = sys.argv[1]
	# 	STRINGTOPRINT = sys.argv[2]
	# 	# print(STRINGTOPRINT)	
	# 	# print(url)
	# 	# sys.exit()
	# else:
	# 	print("right way is -> nameOfprogram.py url STRINGTOPRINT ")
	# 	sys.exit()


	######################################################################################
		######################################################################################
			######################################################################################

	for machine in MACHINES:
		machine["session"] = requests.Session()
	print("Accounts #: "+str(headersLen)+"\nMachine #:"+str(machineLen)+"\nLooking for:"+STRINGTOPRINT)
	time.sleep(5)
	while not FINISH :
		# if x>2:
			# break
		x=x+1
		headerIndex=x%(headersLen)
		machineIndex=x%(machineLen)
		t = threading.Thread(target=update, args=[machineIndex,ALLHEADERS[headerIndex]], name='%s' %(x)) 
		t.start()
		time.sleep(delay) 
		# x=x%100
		# break
	t.join()
	print(str(time.time()-t1))
	print(str(1/FREQUENCY))


