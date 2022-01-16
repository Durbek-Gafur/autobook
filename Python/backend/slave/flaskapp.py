from flask import Flask, request, jsonify
import pip
import requests
import time
import math
import json
import datetime
# __import__(math)
# from pytz import timezone
def import_or_install(requests):
	try:
		__import__(package)
	except ImportError:
		pip.main(['install', package]) 
		__import__(package) 
# import requests
# import datetime

app = Flask(__name__)
SES=requests.Session()
counter =0 
###### GLOABLAL LL2
bigJSON=[]
NEWLOADOBJ={}
returnJsonMany={}
returnJson={}
null=None
false=False
true=True

# def timeZoneConvert(tm, tmzn):
#	 fmt = "%b %d %H:%M"
#	 datetime_obj_naive = datetime.datetime.strptime(tm, "%Y-%m-%dT%H:%M:%SZ")
#	 datetime_obj_proper = timezone('UTC').localize(datetime_obj_naive).astimezone(tz=None)
#	 datetime_obj_proper = datetime_obj_proper.astimezone(timezone(tmzn))
#	 return str(datetime_obj_proper.strftime(fmt))

def jsonToText(ll2):
	firstLoad=ll2["loads"][0]
	firstPU=firstLoad["stops"][0]
	firstPULoc=firstPU["location"]
	l1=(len(ll2["loads"])-1)
	lastLoad=ll2["loads"][l1]
	l2=(len(lastLoad["stops"])- 1)
	lastLoadDel=lastLoad["stops"][l2];
	lastLoadDelLoc=lastLoadDel["location"] 
	singlepayout=round(ll2["payout"]["value"],2)
	f1puname="%s, %s" %(firstPULoc["city"],firstPULoc["state"])
	fp1Time =  firstPU["actions"][0]["plannedTime"] #timeZoneConvert(firstPU["actions"][0]["plannedTime"], firstPULoc["timeZone"])
	ldelname="%s, %s"%(lastLoadDelLoc["city"],lastLoadDelLoc["state"])   
	ldelTime = lastLoadDel["actions"][0]["plannedTime"] #timeZoneConvert(lastLoadDel["actions"][0]["plannedTime"], lastLoadDelLoc["timeZone"]) 
	stopCount = ll2["stopCount"]
	totalDistance = ll2["totalDistance"]["value"]	
	permile=round((singlepayout/totalDistance),2)
	trlStat = firstPU["trailerDetails"][0]["assetOwner"]
	if trlStat:
		trlStat="PO"
	else:
		trlStat="Required"

	return (f1puname+" ("+fp1Time+") - "+str(stopCount)+" - "+ldelname+" ("+ldelTime+") $"+str(singlepayout)+" $"+str(permile)+"/mi "+trlStat)

def goodzone(zipcode):
	zipcode=int(zipcode[:5])
	for zpcs in blackList:
		if zipcode>=zpcs[0] and zipcode<=zpcs[1]: #if zipcode>=32000 and zipcode<=34999: #floarid  floarid
			return False
	return True

# CHECK NEW LOAD THERE OR NOT ?????

def distance(lat1, lon1, lat2, lon2):
	if lat1 == lat2 and lon1 == lon2:
		return 0
	else:
		radlat1 = 0.01745329251 * lat1 
		radlat2 = 0.01745329251 * lat2 
		theta = lon1 - lon2
		radtheta = 0.01745329251 * theta 
		dist = math.sin(radlat1) * math.sin(radlat2) + math.cos(radlat1) * math.cos(radlat2) * math.cos(radtheta)
		if (dist > 1):
			dist = 1
		
		dist = math.acos(dist)
		# dist = dist * 180 / math.pi
		dist = dist * 3958.56540656
		return dist

def smallValidate(bigJSONvalue,f1Lat,f1Lon,lLat, lLon,singlepayout,loadPerMile,trlStatPO,  loadStops): #should book itself
	global returnJsonMany
	###############################################################################################
	################################## P I C K	U P #############################################
	###############################################################################################
	# global _STRTM
	plat = bigJSONvalue["puLat"]
	plon = bigJSONvalue["puLon"]
	prad = bigJSONvalue["puRad"]
	# checking pick up location  
	if not (prad >= distance(float(f1Lat), float(f1Lon), float(plat), float(plon))) :
		returnJsonMany["details"]=returnJsonMany["details"]+"\t-bad pick up\n"
		return False
	###############################################################################################
	###############################################################################################
	###############################################################################################


	###############################################################################################
	################################## D E L I V E R Y ############################################
	###############################################################################################
	dlat = bigJSONvalue["delLat"]
	dlon = bigJSONvalue["delLon"]
	drad = bigJSONvalue["delRad"]

	if not (drad >= distance(float(lLat), float(lLon), float(dlat), float(dlon))):
		returnJsonMany["details"]=returnJsonMany["details"]+"\t-bad delivery"
		return False
	###############################################################################################
	###############################################################################################
	###############################################################################################


	###############################################################################################
	##################################### P A Y O U T #############################################
	###############################################################################################
	# payOut = bigJSONvalue["payOut"]
	# if not (singlepayout >= payOut):
	#	 returnJsonMany["details"]=returnJsonMany["details"]+"\t-bad payout"
	#	 return False
	###############################################################################################
	###############################################################################################
	###############################################################################################


	###############################################################################################
	##################################### P E R / M I L E #########################################
	###############################################################################################
	# perMile = bigJSONvalue["perMile"]
	# if not (loadPerMile>=perMile):
	#	 returnJsonMany["details"]=returnJsonMany["details"]+"\t-bad perMile"
	#	 return False
	###############################################################################################
	###############################################################################################
	###############################################################################################


	###############################################################################################
	##################################### N E W - Y O R K #########################################
	###############################################################################################
	# if bigJSONvalue["nyIchi"]==1:
	#	 if not nyichimas(loadStops):
	#		 return False
	###############################################################################################
	###############################################################################################
	###############################################################################################


	###############################################################################################
	##################################### T R A I L E R ###########################################
	###############################################################################################
	# needTrl = bigJSONvalue["trlStat"];
	# if not needTrl == "0":  
	#	 if not ((needTrl == "REQUIRED" and trlStatPO == False) or (needTrl == "PROVIDED" and trlStatPO)):
	#		 print("bad trailer status , we need " + needTrl + " the load is PO=="+str(trlStatPO))
	#		 return False
	###############################################################################################
	###############################################################################################
	###############################################################################################
		
	
	
	
	##############################
	# print("WE WILL BOOK THIS LOAD")
	# time.sleep(1)
	# print(time.time()-_STRTM)
	return True

def smallValidatePU(bigJSONvalue,f1Lat,f1Lon): #should book itself
	global returnJsonMany
	###############################################################################################
	################################## P I C K	U P #############################################
	###############################################################################################
	# global _STRTM
	plat = bigJSONvalue["puLat"]
	plon = bigJSONvalue["puLon"]
	prad = bigJSONvalue["puRad"]
	# checking pick up location  
	if not (prad >= distance(float(f1Lat), float(f1Lon), float(plat), float(plon))) :
		returnJsonMany["details"]=returnJsonMany["details"]+"\t-bad pick up\n"
		return False
	###############################################################################################
	###############################################################################################
	###############################################################################################

	return True

def smallValidateDEL(bigJSONvalue,lLat, lLon): #should book itself
	global returnJsonMany

	###############################################################################################
	################################## D E L I V E R Y ############################################
	###############################################################################################
	dlat = bigJSONvalue["delLat"]
	dlon = bigJSONvalue["delLon"]
	drad = bigJSONvalue["delRad"]
	if not (drad >= distance(float(lLat), float(lLon), float(dlat), float(dlon))):
		returnJsonMany["details"]=returnJsonMany["details"]+"\t-bad delivery"
		return False
	###############################################################################################
	###############################################################################################
	###############################################################################################

	return True

def smallValidatePUDEL(bigJSONvalue,f1Lat,f1Lon,lLat, lLon): #should book itself
	global returnJsonMany
	###############################################################################################
	################################## P I C K	U P #############################################
	###############################################################################################
	# global _STRTM
	plat = bigJSONvalue["puLat"]
	plon = bigJSONvalue["puLon"]
	prad = bigJSONvalue["puRad"]
	# checking pick up location  
	if not (prad >= distance(float(f1Lat), float(f1Lon), float(plat), float(plon))) :
		returnJsonMany["details"]=returnJsonMany["details"]+"\t-bad pick up\n"
		return False
	###############################################################################################
	###############################################################################################
	###############################################################################################


	###############################################################################################
	################################## D E L I V E R Y ############################################
	###############################################################################################
	dlat = bigJSONvalue["delLat"]
	dlon = bigJSONvalue["delLon"]
	drad = bigJSONvalue["delRad"]

	if not (drad >= distance(float(lLat), float(lLon), float(dlat), float(dlon))):
		returnJsonMany["details"]=returnJsonMany["details"]+"\t-bad delivery"
		return False
	###############################################################################################
	###############################################################################################
	###############################################################################################

	return True

def smallValidatePURATE(bigJSONvalue,f1Lat,f1Lon,singlepayout,loadPerMile): #should book itself
	global returnJsonMany
	###############################################################################################
	################################## P I C K	U P #############################################
	###############################################################################################
	# global _STRTM
	plat = bigJSONvalue["puLat"]
	plon = bigJSONvalue["puLon"]
	prad = bigJSONvalue["puRad"]
	# checking pick up location  
	if not (prad >= distance(float(f1Lat), float(f1Lon), float(plat), float(plon))) :
		returnJsonMany["details"]=returnJsonMany["details"]+"\t-bad pick up\n"
		return False
	###############################################################################################
	###############################################################################################
	###############################################################################################


	###############################################################################################
	##################################### P A Y O U T #############################################
	###############################################################################################
	payOut = bigJSONvalue["payOut"]
	if not (singlepayout >= payOut):
		 returnJsonMany["details"]=returnJsonMany["details"]+"\t-bad payout"
		 return False
	###############################################################################################
	###############################################################################################
	###############################################################################################


	###############################################################################################
	##################################### P E R / M I L E #########################################
	###############################################################################################
	perMile = bigJSONvalue["perMile"]
	if not (loadPerMile>=perMile):
		 returnJsonMany["details"]=returnJsonMany["details"]+"\t-bad perMile"
		 return False
	###############################################################################################
	###############################################################################################
	###############################################################################################

		
	
	
	
	##############################
	# print("WE WILL BOOK THIS LOAD")
	# time.sleep(1)
	# print(time.time()-_STRTM)
	return True

def smallValidatePUDELRATE(bigJSONvalue,f1Lat,f1Lon,lLat, lLon,singlepayout,loadPerMile): #should book itself
	global returnJsonMany
	###############################################################################################
	################################## P I C K	U P #############################################
	###############################################################################################
	# global _STRTM
	plat = bigJSONvalue["puLat"]
	plon = bigJSONvalue["puLon"]
	prad = bigJSONvalue["puRad"]
	# checking pick up location  
	if not (prad >= distance(float(f1Lat), float(f1Lon), float(plat), float(plon))) :
		returnJsonMany["details"]=returnJsonMany["details"]+"\t-bad pick up\n"
		return False
	###############################################################################################
	###############################################################################################
	###############################################################################################


	###############################################################################################
	################################## D E L I V E R Y ############################################
	###############################################################################################
	dlat = bigJSONvalue["delLat"]
	dlon = bigJSONvalue["delLon"]
	drad = bigJSONvalue["delRad"]

	if not (drad >= distance(float(lLat), float(lLon), float(dlat), float(dlon))):
		returnJsonMany["details"]=returnJsonMany["details"]+"\t-bad delivery"
		return False
	###############################################################################################
	###############################################################################################
	###############################################################################################


	###############################################################################################
	##################################### P A Y O U T #############################################
	###############################################################################################
	payOut = bigJSONvalue["payOut"]
	if not (singlepayout >= payOut):
		 returnJsonMany["details"]=returnJsonMany["details"]+"\t-bad payout"
		 return False
	###############################################################################################
	###############################################################################################
	###############################################################################################


	###############################################################################################
	##################################### P E R / M I L E #########################################
	###############################################################################################
	perMile = bigJSONvalue["perMile"]
	if not (loadPerMile>=perMile):
		 returnJsonMany["details"]=returnJsonMany["details"]+"\t-bad perMile"
		 return False
	###############################################################################################
	###############################################################################################
	###############################################################################################

	return True

def smallValidateDELRATE(bigJSONvalue,lLat, lLon,singlepayout,loadPerMile): #should book itself
	global returnJsonMany

	###############################################################################################
	################################## D E L I V E R Y ############################################
	###############################################################################################
	dlat = bigJSONvalue["delLat"]
	dlon = bigJSONvalue["delLon"]
	drad = bigJSONvalue["delRad"]

	if not (drad >= distance(float(lLat), float(lLon), float(dlat), float(dlon))):
		returnJsonMany["details"]=returnJsonMany["details"]+"\t-bad delivery"
		return False
	###############################################################################################
	###############################################################################################
	###############################################################################################


	###############################################################################################
	##################################### P A Y O U T #############################################
	###############################################################################################
	payOut = bigJSONvalue["payOut"]
	if not (singlepayout >= payOut):
		 returnJsonMany["details"]=returnJsonMany["details"]+"\t-bad payout"
		 return False
	###############################################################################################
	###############################################################################################
	###############################################################################################


	###############################################################################################
	##################################### P E R / M I L E #########################################
	###############################################################################################
	perMile = bigJSONvalue["perMile"]
	if not (loadPerMile>=perMile):
		 returnJsonMany["details"]=returnJsonMany["details"]+"\t-bad perMile"
		 return False
	###############################################################################################
	###############################################################################################
	###############################################################################################

	return True


def validate(singleLoad,lnk,json_mylist,getLoadHeader):
	global FINISH
	global returnJsonMany
	global bigJSON
	global SES


	null=None
	true=True
	false=False
	firstLoad=singleLoad["loads"][0]
	firstPU=firstLoad["stops"][0]
	firstPULoc=firstPU["location"]
	# f1Lat = firstPULoc["latitude"] #location pick up
	# f1Lon = firstPULoc["longitude"] #location pick up
	# f1Time = singleLoad["startTime"]

	# singleLoad=singleLoad
	l1=(len(singleLoad["loads"])-1)   
	lastLoad=singleLoad["loads"][l1]

	l2=(len(lastLoad["stops"])- 1)
	lastLoadDel=lastLoad["stops"][l2];
	lastLoadDelLoc=lastLoadDel["location"]
	# lLat = lastLoadDelLoc["latitude"] #location delivery
	# lLon = lastLoadDelLoc["longitude"] #location delivery
	deliveryZipcode = lastLoadDelLoc["postalCode"]
	# lTime = singleLoad["endTime"]

	singlepayout=round(singleLoad["payout"]["value"],2)
	# f1puname="%s, %s" %(firstPULoc["city"],firstPULoc["state"])
	# fp1Time =  timeZoneConvert(firstPU["actions"][0]["plannedTime"], firstPULoc["timeZone"])
	# ldelname="%s, %s"%(lastLoadDelLoc["city"],lastLoadDelLoc["state"])   
	# ldelTime = timeZoneConvert(lastLoadDel["actions"][0]["plannedTime"], lastLoadDelLoc["timeZone"]) 
	stopCount = singleLoad["stopCount"]
	totalDistance = singleLoad["totalDistance"]["value"]	
	# permile=(singlepayout/totalDistance)
	# trlStat = firstPU["trailerDetails"][0]["assetOwner"]


	trlStatPO="NAN" 
	# print(trlStat)
	# if firstPU["trailerDetails"][0]["assetOwner"]:
	#	 trlStatPO=True
	# else:
	#	 trlStatPO=False 
	# print(trlStatPO)
	# threadPool=[]

	###############################################################################################
	########################## D E L I V E R Y   G O O D - Z O N E ################################
	###############################################################################################
	# if not goodzone(deliveryZipcode):
	#	 print("Not goodzone")
	#	 return
	###############################################################################################
	###############################################################################################
	###############################################################################################


	###############################################################################################
	##################################### S T O P  C O U N T ######################################
	###############################################################################################
	# if stopCount>5:
		# return
	###############################################################################################
	###############################################################################################
	###############################################################################################

	
	for bigJSONvalue in bigJSON:
		# t = threading.Thread(target=smallValidate, args=[bigJSONvalue,f1Lat,f1Lon,lLat,lLon,singlepayout,permile,trlStatPO] ) 
		# t.start()
		# threadPool.append(t)
		if smallValidate(bigJSONvalue,firstPULoc["latitude"],firstPULoc["longitude"],lastLoadDelLoc["latitude"],lastLoadDelLoc["longitude"],round(singleLoad["payout"]["value"],2),(singlepayout/totalDistance),trlStatPO, singleLoad["loads"]) : #should become thread
			#book it

			r = SES.post(lnk, data=json_mylist, headers=getLoadHeader)
			FINISH=True
			bigJSON.remove(bigJSONvalue)
			if r.status_code==200:
				 rslt = "Alhamdulillah"
			else:
				 rslt = "Olloh bizga kifoya"
			returnJsonMany["booked"]=returnJsonMany["booked"]+" "+str(r.status_code) +" "+rslt #r.status_code
			loadjsonToText= jsonToText(singleLoad) #f1puname+" - "+ldelname+" - "+ str(singlepayout)		 
			url_l = "https://api.telegram.org/bot1211014469:AAE7PKOFEd1gfBW3HO10E5zFS7GbmDNAIbA/sendMessage?chat_id=971769511&text="+str(rslt)+" "+str(r.status_code)+" "+loadjsonToText
			resres = requests.get(url_l)
			break

	# for t in threadPool:
		# t.join()

	return

def validatePU(singleLoad,lnk,json_mylist,getLoadHeader):
	global FINISH
	global returnJsonMany
	global bigJSON
	global SES

	null=None
	true=True
	false=False
	firstLoad=singleLoad["loads"][0]
	firstPU=firstLoad["stops"][0]
	firstPULoc=firstPU["location"]
	

	
	for bigJSONvalue in bigJSON:
		if smallValidatePU(bigJSONvalue,firstPULoc["latitude"],firstPULoc["longitude"]) : #should become thread
			#book it

			r = SES.post(lnk, data=json_mylist, headers=getLoadHeader)
			FINISH=True
			bigJSON.remove(bigJSONvalue)
			if r.status_code==200:
				 rslt = "Alhamdulillah"
			else:
				 rslt = "Olloh bizga kifoya"
			returnJsonMany["booked"]=returnJsonMany["booked"]+" "+str(r.status_code) +" "+rslt #r.status_code
			loadjsonToText= jsonToText(singleLoad) #f1puname+" - "+ldelname+" - "+ str(singlepayout)		 
			url_l = "https://api.telegram.org/bot1211014469:AAE7PKOFEd1gfBW3HO10E5zFS7GbmDNAIbA/sendMessage?chat_id=971769511&text="+str(rslt)+" "+str(r.status_code)+" "+loadjsonToText
			resres = requests.get(url_l)
			break
	return

def validateDEL(singleLoad,lnk,json_mylist,getLoadHeader):
	global FINISH
	global returnJsonMany
	global bigJSON
	global SES

	null=None
	true=True
	false=False

	l1=(len(singleLoad["loads"])-1)   
	lastLoad=singleLoad["loads"][l1]

	l2=(len(lastLoad["stops"])- 1)
	lastLoadDel=lastLoad["stops"][l2];
	lastLoadDelLoc=lastLoadDel["location"]

	
	for bigJSONvalue in bigJSON:
		if smallValidateDEL(bigJSONvalue,lastLoadDelLoc["latitude"],lastLoadDelLoc["longitude"]) : #should become thread
			#book it

			r = SES.post(lnk, data=json_mylist, headers=getLoadHeader)
			FINISH=True
			bigJSON.remove(bigJSONvalue)
			if r.status_code==200:
				 rslt = "Alhamdulillah"
			else:
				 rslt = "Olloh bizga kifoya"
			returnJsonMany["booked"]=returnJsonMany["booked"]+" "+str(r.status_code) +" "+rslt #r.status_code
			loadjsonToText= jsonToText(singleLoad) #f1puname+" - "+ldelname+" - "+ str(singlepayout)		 
			url_l = "https://api.telegram.org/bot1211014469:AAE7PKOFEd1gfBW3HO10E5zFS7GbmDNAIbA/sendMessage?chat_id=971769511&text="+str(rslt)+" "+str(r.status_code)+" "+loadjsonToText
			resres = requests.get(url_l)
			break
	return

def validatePUDEL(singleLoad,lnk,json_mylist,getLoadHeader):
	global FINISH
	global returnJsonMany
	global bigJSON
	global SES

	null=None
	true=True
	false=False
	firstLoad=singleLoad["loads"][0]
	firstPU=firstLoad["stops"][0]
	firstPULoc=firstPU["location"]
	l1=(len(singleLoad["loads"])-1)   
	lastLoad=singleLoad["loads"][l1]

	l2=(len(lastLoad["stops"])- 1)
	lastLoadDel=lastLoad["stops"][l2];
	lastLoadDelLoc=lastLoadDel["location"]

	
	for bigJSONvalue in bigJSON:
		if smallValidatePUDEL(bigJSONvalue,firstPULoc["latitude"],firstPULoc["longitude"],lastLoadDelLoc["latitude"],lastLoadDelLoc["longitude"]) : #should become thread
			#book it

			r = SES.post(lnk, data=json_mylist, headers=getLoadHeader)
			FINISH=True
			bigJSON.remove(bigJSONvalue)
			if r.status_code==200:
				 rslt = "Alhamdulillah"
			else:
				 rslt = "Olloh bizga kifoya"
			returnJsonMany["booked"]=returnJsonMany["booked"]+" "+str(r.status_code) +" "+rslt #r.status_code
			loadjsonToText= jsonToText(singleLoad) #f1puname+" - "+ldelname+" - "+ str(singlepayout)		 
			url_l = "https://api.telegram.org/bot1211014469:AAE7PKOFEd1gfBW3HO10E5zFS7GbmDNAIbA/sendMessage?chat_id=971769511&text="+str(rslt)+" "+str(r.status_code)+" "+loadjsonToText
			resres = requests.get(url_l)
			break
	return

def validatePURATE(singleLoad,lnk,json_mylist,getLoadHeader):
	global FINISH
	global returnJsonMany
	global bigJSON
	global SES

	null=None
	true=True
	false=False
	firstLoad=singleLoad["loads"][0]
	firstPU=firstLoad["stops"][0]
	firstPULoc=firstPU["location"]
	
	singlepayout=round(singleLoad["payout"]["value"],2)
	stopCount = singleLoad["stopCount"]
	totalDistance = singleLoad["totalDistance"]["value"]	
	
	for bigJSONvalue in bigJSON:
		if smallValidatePURATE(bigJSONvalue,firstPULoc["latitude"],firstPULoc["longitude"],round(singleLoad["payout"]["value"],2),(singlepayout/totalDistance)) : #should become thread
			#book it

			r = SES.post(lnk, data=json_mylist, headers=getLoadHeader)
			FINISH=True
			bigJSON.remove(bigJSONvalue)
			if r.status_code==200:
				 rslt = "Alhamdulillah"
			else:
				 rslt = "Olloh bizga kifoya"
			returnJsonMany["booked"]=returnJsonMany["booked"]+" "+str(r.status_code) +" "+rslt #r.status_code
			loadjsonToText= jsonToText(singleLoad) #f1puname+" - "+ldelname+" - "+ str(singlepayout)		 
			url_l = "https://api.telegram.org/bot1211014469:AAE7PKOFEd1gfBW3HO10E5zFS7GbmDNAIbA/sendMessage?chat_id=971769511&text="+str(rslt)+" "+str(r.status_code)+" "+loadjsonToText
			resres = requests.get(url_l)
			break
	return

def validatePUDELRATE(singleLoad,lnk,json_mylist,getLoadHeader):
	global FINISH
	global returnJsonMany
	global bigJSON
	global SES

	null=None
	true=True
	false=False
	firstLoad=singleLoad["loads"][0]
	firstPU=firstLoad["stops"][0]
	firstPULoc=firstPU["location"]
	l1=(len(singleLoad["loads"])-1)   
	lastLoad=singleLoad["loads"][l1]

	l2=(len(lastLoad["stops"])- 1)
	lastLoadDel=lastLoad["stops"][l2];
	lastLoadDelLoc=lastLoadDel["location"]
	deliveryZipcode = lastLoadDelLoc["postalCode"]

	singlepayout=round(singleLoad["payout"]["value"],2)
	stopCount = singleLoad["stopCount"]
	totalDistance = singleLoad["totalDistance"]["value"]	
	
	for bigJSONvalue in bigJSON:
		if smallValidatePUDELRATE(bigJSONvalue,firstPULoc["latitude"],firstPULoc["longitude"],lastLoadDelLoc["latitude"],lastLoadDelLoc["longitude"],round(singleLoad["payout"]["value"],2),(singlepayout/totalDistance)) : #should become thread
			#book it

			r = SES.post(lnk, data=json_mylist, headers=getLoadHeader)
			FINISH=True
			bigJSON.remove(bigJSONvalue)
			if r.status_code==200:
				 rslt = "Alhamdulillah"
			else:
				 rslt = "Olloh bizga kifoya"
			returnJsonMany["booked"]=returnJsonMany["booked"]+" "+str(r.status_code) +" "+rslt #r.status_code
			loadjsonToText= jsonToText(singleLoad) #f1puname+" - "+ldelname+" - "+ str(singlepayout)		 
			url_l = "https://api.telegram.org/bot1211014469:AAE7PKOFEd1gfBW3HO10E5zFS7GbmDNAIbA/sendMessage?chat_id=971769511&text="+str(rslt)+" "+str(r.status_code)+" "+loadjsonToText
			resres = requests.get(url_l)
			break
	return

def validateDELRATE(singleLoad,lnk,json_mylist,getLoadHeader):
	global FINISH
	global returnJsonMany
	global bigJSON
	global SES

	null=None
	true=True
	false=False

	l1=(len(singleLoad["loads"])-1)   
	lastLoad=singleLoad["loads"][l1]

	l2=(len(lastLoad["stops"])- 1)
	lastLoadDel=lastLoad["stops"][l2];
	lastLoadDelLoc=lastLoadDel["location"]
	deliveryZipcode = lastLoadDelLoc["postalCode"]

	singlepayout=round(singleLoad["payout"]["value"],2)
	stopCount = singleLoad["stopCount"]
	totalDistance = singleLoad["totalDistance"]["value"]	
	
	for bigJSONvalue in bigJSON:
		if smallValidateDELRATE(bigJSONvalue,lastLoadDelLoc["latitude"],lastLoadDelLoc["longitude"],round(singleLoad["payout"]["value"],2),(singlepayout/totalDistance)) : #should become thread
			#book it

			r = SES.post(lnk, data=json_mylist, headers=getLoadHeader)
			FINISH=True
			bigJSON.remove(bigJSONvalue)
			if r.status_code==200:
				 rslt = "Alhamdulillah"
			else:
				 rslt = "Olloh bizga kifoya"
			returnJsonMany["booked"]=returnJsonMany["booked"]+" "+str(r.status_code) +" "+rslt #r.status_code
			loadjsonToText= jsonToText(singleLoad) #f1puname+" - "+ldelname+" - "+ str(singlepayout)		 
			url_l = "https://api.telegram.org/bot1211014469:AAE7PKOFEd1gfBW3HO10E5zFS7GbmDNAIbA/sendMessage?chat_id=971769511&text="+str(rslt)+" "+str(r.status_code)+" "+loadjsonToText
			resres = requests.get(url_l)
			break
	return


def newLoadCheck(allLoads,carrierPerformanceCategory,priorityAccessVersion,getLoadHeader):
	global returnJsonMany
	newLoad=False
	null=None
	true=True
	false=False
	
	newLoadList=[]
	newLoadCounter=0
	returnJsonMany["details"]="None"
  
	for val in allLoads:
		new_load_id = val["id"]+str(val["version"])+str(val["payout"]["value"])+str(val["workOpportunityOptionId"])
		
		if new_load_id not in NEWLOADOBJ:

			newLoad=True
			NEWLOADOBJ[new_load_id]=True
			# newLoadList.append(jsonToText(val))
			lnk = "https://relay.amazon.com/api/tours/loadboard/%s/%s/option/%s" % (val["id"], val["version"], val["workOpportunityOptionId"])
			auditContextMap={
				"rlbChannel": "EXACT_MATCH",
				"searchResultIndex": "0",
				"workOpportunityId": "%s" % val["id"],
				"time": "%s" % (int(time.time() * 1000) - 25),
				"carrierPerformanceCategory": carrierPerformanceCategory,
				"priorityAccessVersion": priorityAccessVersion,
				"isPriorityAccessEnabled": "true",
				"isPickupTimeChanged": "false",
				"originalPickupTime": "%s" % val["startTime"],
				"newPickupTime": "%s" % val["startTime"],
				"truckCapacityOrderVersion": "",
				"carrierType": "BROKERAGE",
				"searchSource": ""
			}

			js = {"totalCost":{"value": val["payout"]["value"],"unit":"USD"},"auditContextMap":"%s" % json.dumps(auditContextMap),"searchURL":""} 
			json_mylist = json.dumps(js, separators=(',', ':'))
			validate(val,lnk,json_mylist,getLoadHeader)
			returnJsonMany["details"]=returnJsonMany["details"]+"-"+jsonToText(val)+"\n"

def newLoadCheckPU(allLoads,carrierPerformanceCategory,priorityAccessVersion,getLoadHeader):
	global returnJsonMany
	newLoad=False
	null=None
	true=True
	false=False
	
	newLoadList=[]
	newLoadCounter=0
	returnJsonMany["details"]="None"
  
	for val in allLoads:
		new_load_id = val["id"]+str(val["version"])+str(val["payout"]["value"])+str(val["workOpportunityOptionId"])
		
		if new_load_id not in NEWLOADOBJ:

			newLoad=True
			NEWLOADOBJ[new_load_id]=True
			# newLoadList.append(jsonToText(val))
			lnk = "https://relay.amazon.com/api/tours/loadboard/%s/%s/option/%s" % (val["id"], val["version"], val["workOpportunityOptionId"])
			auditContextMap={
				"rlbChannel": "EXACT_MATCH",
				"searchResultIndex": "0",
				"workOpportunityId": "%s" % val["id"],
				"time": "%s" % (int(time.time() * 1000) - 25),
				"carrierPerformanceCategory": carrierPerformanceCategory,
				"priorityAccessVersion": priorityAccessVersion,
				"isPriorityAccessEnabled": "true",
				"isPickupTimeChanged": "false",
				"originalPickupTime": "%s" % val["startTime"],
				"newPickupTime": "%s" % val["startTime"],
				"truckCapacityOrderVersion": "",
				"carrierType": "BROKERAGE",
				"searchSource": ""
			}

			js = {"totalCost":{"value": val["payout"]["value"],"unit":"USD"},"auditContextMap":"%s" % json.dumps(auditContextMap),"searchURL":""} 
			json_mylist = json.dumps(js, separators=(',', ':'))
			validatePU(val,lnk,json_mylist,getLoadHeader)
			returnJsonMany["details"]=returnJsonMany["details"]+"-"+jsonToText(val)+"\n"

def newLoadCheckDEL(allLoads,carrierPerformanceCategory,priorityAccessVersion,getLoadHeader):
	global returnJsonMany
	newLoad=False
	null=None
	true=True
	false=False
	
	newLoadList=[]
	newLoadCounter=0
	returnJsonMany["details"]="None"
  
	for val in allLoads:
		new_load_id = val["id"]+str(val["version"])+str(val["payout"]["value"])+str(val["workOpportunityOptionId"])
		
		if new_load_id not in NEWLOADOBJ:

			newLoad=True
			NEWLOADOBJ[new_load_id]=True
			# newLoadList.append(jsonToText(val))
			lnk = "https://relay.amazon.com/api/tours/loadboard/%s/%s/option/%s" % (val["id"], val["version"], val["workOpportunityOptionId"])
			auditContextMap={
				"rlbChannel": "EXACT_MATCH",
				"searchResultIndex": "0",
				"workOpportunityId": "%s" % val["id"],
				"time": "%s" % (int(time.time() * 1000) - 25),
				"carrierPerformanceCategory": carrierPerformanceCategory,
				"priorityAccessVersion": priorityAccessVersion,
				"isPriorityAccessEnabled": "true",
				"isPickupTimeChanged": "false",
				"originalPickupTime": "%s" % val["startTime"],
				"newPickupTime": "%s" % val["startTime"],
				"truckCapacityOrderVersion": "",
				"carrierType": "BROKERAGE",
				"searchSource": ""
			}

			js = {"totalCost":{"value": val["payout"]["value"],"unit":"USD"},"auditContextMap":"%s" % json.dumps(auditContextMap),"searchURL":""} 
			json_mylist = json.dumps(js, separators=(',', ':'))
			validateDEL(val,lnk,json_mylist,getLoadHeader)
			returnJsonMany["details"]=returnJsonMany["details"]+"-"+jsonToText(val)+"\n"

def newLoadCheckPUDEL(allLoads,carrierPerformanceCategory,priorityAccessVersion,getLoadHeader):
	global returnJsonMany
	newLoad=False
	null=None
	true=True
	false=False
	
	newLoadList=[]
	newLoadCounter=0
	returnJsonMany["details"]="None"
  
	for val in allLoads:
		new_load_id = val["id"]+str(val["version"])+str(val["payout"]["value"])+str(val["workOpportunityOptionId"])
		
		if new_load_id not in NEWLOADOBJ:

			newLoad=True
			NEWLOADOBJ[new_load_id]=True
			# newLoadList.append(jsonToText(val))
			lnk = "https://relay.amazon.com/api/tours/loadboard/%s/%s/option/%s" % (val["id"], val["version"], val["workOpportunityOptionId"])
			auditContextMap={
				"rlbChannel": "EXACT_MATCH",
				"searchResultIndex": "0",
				"workOpportunityId": "%s" % val["id"],
				"time": "%s" % (int(time.time() * 1000) - 25),
				"carrierPerformanceCategory": carrierPerformanceCategory,
				"priorityAccessVersion": priorityAccessVersion,
				"isPriorityAccessEnabled": "true",
				"isPickupTimeChanged": "false",
				"originalPickupTime": "%s" % val["startTime"],
				"newPickupTime": "%s" % val["startTime"],
				"truckCapacityOrderVersion": "",
				"carrierType": "BROKERAGE",
				"searchSource": ""
			}

			js = {"totalCost":{"value": val["payout"]["value"],"unit":"USD"},"auditContextMap":"%s" % json.dumps(auditContextMap),"searchURL":""} 
			json_mylist = json.dumps(js, separators=(',', ':'))
			validatePUDEL(val,lnk,json_mylist,getLoadHeader)
			returnJsonMany["details"]=returnJsonMany["details"]+"-"+jsonToText(val)+"\n"

def newLoadCheckPURATE(allLoads,carrierPerformanceCategory,priorityAccessVersion,getLoadHeader):
	global returnJsonMany
	newLoad=False
	null=None
	true=True
	false=False
	
	newLoadList=[]
	newLoadCounter=0
	returnJsonMany["details"]="None"
  
	for val in allLoads:
		new_load_id = val["id"]+str(val["version"])+str(val["payout"]["value"])+str(val["workOpportunityOptionId"])
		
		if new_load_id not in NEWLOADOBJ:

			newLoad=True
			NEWLOADOBJ[new_load_id]=True
			# newLoadList.append(jsonToText(val))
			lnk = "https://relay.amazon.com/api/tours/loadboard/%s/%s/option/%s" % (val["id"], val["version"], val["workOpportunityOptionId"])
			auditContextMap={
				"rlbChannel": "EXACT_MATCH",
				"searchResultIndex": "0",
				"workOpportunityId": "%s" % val["id"],
				"time": "%s" % (int(time.time() * 1000) - 25),
				"carrierPerformanceCategory": carrierPerformanceCategory,
				"priorityAccessVersion": priorityAccessVersion,
				"isPriorityAccessEnabled": "true",
				"isPickupTimeChanged": "false",
				"originalPickupTime": "%s" % val["startTime"],
				"newPickupTime": "%s" % val["startTime"],
				"truckCapacityOrderVersion": "",
				"carrierType": "BROKERAGE",
				"searchSource": ""
			}

			js = {"totalCost":{"value": val["payout"]["value"],"unit":"USD"},"auditContextMap":"%s" % json.dumps(auditContextMap),"searchURL":""} 
			json_mylist = json.dumps(js, separators=(',', ':'))
			validatePURATE(val,lnk,json_mylist,getLoadHeader)
			returnJsonMany["details"]=returnJsonMany["details"]+"-"+jsonToText(val)+"\n"

def newLoadCheckPUDELRATE(allLoads,carrierPerformanceCategory,priorityAccessVersion,getLoadHeader):
	global returnJsonMany
	newLoad=False
	null=None
	true=True
	false=False
	
	newLoadList=[]
	newLoadCounter=0
	returnJsonMany["details"]="None"
  
	for val in allLoads:
		new_load_id = val["id"]+str(val["version"])+str(val["payout"]["value"])+str(val["workOpportunityOptionId"])
		
		if new_load_id not in NEWLOADOBJ:

			newLoad=True
			NEWLOADOBJ[new_load_id]=True
			# newLoadList.append(jsonToText(val))
			lnk = "https://relay.amazon.com/api/tours/loadboard/%s/%s/option/%s" % (val["id"], val["version"], val["workOpportunityOptionId"])
			auditContextMap={
				"rlbChannel": "EXACT_MATCH",
				"searchResultIndex": "0",
				"workOpportunityId": "%s" % val["id"],
				"time": "%s" % (int(time.time() * 1000) - 25),
				"carrierPerformanceCategory": carrierPerformanceCategory,
				"priorityAccessVersion": priorityAccessVersion,
				"isPriorityAccessEnabled": "true",
				"isPickupTimeChanged": "false",
				"originalPickupTime": "%s" % val["startTime"],
				"newPickupTime": "%s" % val["startTime"],
				"truckCapacityOrderVersion": "",
				"carrierType": "BROKERAGE",
				"searchSource": ""
			}

			js = {"totalCost":{"value": val["payout"]["value"],"unit":"USD"},"auditContextMap":"%s" % json.dumps(auditContextMap),"searchURL":""} 
			json_mylist = json.dumps(js, separators=(',', ':'))
			validatePUDELRATE(val,lnk,json_mylist,getLoadHeader)
			returnJsonMany["details"]=returnJsonMany["details"]+"-"+jsonToText(val)+"\n"

def newLoadCheckDELRATE(allLoads,carrierPerformanceCategory,priorityAccessVersion,getLoadHeader):
	global returnJsonMany
	newLoad=False
	null=None
	true=True
	false=False
	
	newLoadList=[]
	newLoadCounter=0
	returnJsonMany["details"]="None"
  
	for val in allLoads:
		new_load_id = val["id"]+str(val["version"])+str(val["payout"]["value"])+str(val["workOpportunityOptionId"])
		
		if new_load_id not in NEWLOADOBJ:

			newLoad=True
			NEWLOADOBJ[new_load_id]=True
			# newLoadList.append(jsonToText(val))
			lnk = "https://relay.amazon.com/api/tours/loadboard/%s/%s/option/%s" % (val["id"], val["version"], val["workOpportunityOptionId"])
			auditContextMap={
				"rlbChannel": "EXACT_MATCH",
				"searchResultIndex": "0",
				"workOpportunityId": "%s" % val["id"],
				"time": "%s" % (int(time.time() * 1000) - 25),
				"carrierPerformanceCategory": carrierPerformanceCategory,
				"priorityAccessVersion": priorityAccessVersion,
				"isPriorityAccessEnabled": "true",
				"isPickupTimeChanged": "false",
				"originalPickupTime": "%s" % val["startTime"],
				"newPickupTime": "%s" % val["startTime"],
				"truckCapacityOrderVersion": "",
				"carrierType": "BROKERAGE",
				"searchSource": ""
			}

			js = {"totalCost":{"value": val["payout"]["value"],"unit":"USD"},"auditContextMap":"%s" % json.dumps(auditContextMap),"searchURL":""} 
			json_mylist = json.dumps(js, separators=(',', ':'))
			validateDELRATE(val,lnk,json_mylist,getLoadHeader)
			returnJsonMany["details"]=returnJsonMany["details"]+"-"+jsonToText(val)+"\n"

@app.route('/')
def hello_world():
	global SES

	url="https://relay.amazon.com/api/tours/loadboard?sortByField=startTime&sortOrder=asc&workOpportunityType=ROUND_TRIP&startCityLatitude=38.449373&startCityLongitude=-121.34428&startCityRadius=25&startCityName=SACRAMENTO&startCityStateCode=CA&startCityDisplayValue=SACRAMENTO,%20CA&isOriginCityLive=false&originCity=[object%20Object]&endCityLatitude=38.449373&endCityLongitude=-121.34428&endCityRadius=25&endCityName=SACRAMENTO&endCityStateCode=CA&endCityDisplayValue=SACRAMENTO,%20CA&isDestinationCityLive=false&destinationCity=[object%20Object]&minPayout=1800&maxPayout=12000&minPricePerDistance=2&maxPricePerDistance=30&trailerStatusFilters=PROVIDED&trailerStatus=PROVIDED&equipmentTypeFilters=FIFTY_THREE_FOOT_TRUCK,SKIRTED_FIFTY_THREE_FOOT_TRUCK,FIFTY_THREE_FOOT_DRY_VAN&equipmentTypes=FIFTY_THREE_FOOT_TRUCK,SKIRTED_FIFTY_THREE_FOOT_TRUCK,FIFTY_THREE_FOOT_DRY_VAN&nextItemToken=0&resultSize=100&searchURL=&savedSearchId=&isAutoRefreshCall=false&notificationId=&auditContextMap={%22rlbChannel%22:%22EXACT_MATCH%22,%22isOriginCityLive%22:%22false%22,%22isDestinationCityLive%22:%22false%22}"

	timeBeforeAskLoad=time.time()
	askLoadRequest = SES.get(url, headers=request.headers)  #verify=False   
	timeAfterAskLoad=time.time()
	return "lalal "+str(timeAfterAskLoad-timeBeforeAskLoad)+" "+askLoadRequest.text #+"\n"+ jsonify()
if __name__ == '__main__':
	import_or_install(requests)
	import_or_install(time)
	import_or_install(json)
	# import_or_install(math)
	import_or_install(datetime)
	import_or_install(pytz)

	# import requests
	# import datetime
	app.run()


@app.route('/one', methods=['POST'])
def one():
	global SES
	global counter
	global returnJson
	
	returnJson={
		"isbot": False,
		"carrierEngagementCategory":"None",
		"askSentAt":0,
		"askStatus":0,
		"askDur":0.0,
		"booked":"None",
		"counter": counter
	}
	counter=counter+1

	url = request.form['url']
	carrierPerformanceCategory=request.form['carrierPerformanceCategory']
	priorityAccessVersion=request.form['priorityAccessVersion']
	headers=json.loads(request.form['header'])
	getLoadHeader=json.loads(request.form['getLoadHeader'])
	timeBeforeAskLoad=time.time()
	askLoadRequest = SES.get(url, headers=headers)  #verify=False   
	timeAfterAskLoad=time.time()
	newLoadInfo="-"
	if askLoadRequest.status_code!=200 :
		returnJson["askStatus"]=askLoadRequest.status_code
		return returnJson
			# 111
	else :
		loads =  json.loads(askLoadRequest.text) #) sampleLoad)# askLoadRequest.text #TESTTESTTES
		if loads["totalResultsSize"] > 0:
			firstLoad = loads["workOpportunities"][0]	 
			link = "https://relay.amazon.com/api/tours/loadboard/%s/%s/option/%s" % (firstLoad["id"], firstLoad["version"], firstLoad["workOpportunityOptionId"])
			auditContextMap={
				"rlbChannel": "EXACT_MATCH",
				"searchResultIndex": "0",
				"workOpportunityId": "%s" % firstLoad["id"],
				"time": "%s" % (int(time.time() * 1000) - 25),
				"carrierPerformanceCategory": carrierPerformanceCategory,
				"priorityAccessVersion": priorityAccessVersion, #"priorityAccessVersion2",
				"isPriorityAccessEnabled": "true",
				"isPickupTimeChanged": "false",
				"originalPickupTime": "%s" % firstLoad["startTime"],
				"newPickupTime": "%s" % firstLoad["startTime"],
				"truckCapacityOrderVersion": "",
				"carrierType": "BROKERAGE",
				"searchSource": ""
			}
			js = {"totalCost":{"value": firstLoad["payout"]["value"],"unit":"USD"},"auditContextMap":"%s" % json.dumps(auditContextMap),"searchURL":""} 
			json_mylist = json.dumps(js, separators=(',', ':')) 

			r = SES.post(link, data=json_mylist, headers=getLoadHeader)
			FINISH = True
			if r.status_code==200:
				weGotTheLoad = "Alhamdulillah "
				errorTextCode="Alhamdulillah "
			else:
				weGotTheLoad = "Hasbunallah Wa Nimal-Wakil "
				errorTextCode=json.loads(r.text) 
				errorTextCode=errorTextCode["errorCode"]
			# tmpR=str(r.status_code) #+" "+weGotTheLoad
			# returnJson["booked"]=tmpR
			loadDetails=jsonToText(firstLoad)
			returnJson["booked"]=str(r.status_code) +" "+weGotTheLoad
			url_l = "https://api.telegram.org/bot1211014469:AAE7PKOFEd1gfBW3HO10E5zFS7GbmDNAIbA/sendMessage?chat_id=971769511&text="+weGotTheLoad+str(r.status_code)+" "+loadDetails
			resres = requests.get(url_l)
			   
			newLoadInfo=" ".join(["\n",loadDetails,"\n", str(r.status_code), errorTextCode])
		null=None
		isBot=str(loads["isBotRequest"])+"\t"+ loads["carrierDetails"]["carrierEngagementCategory"]
	duration= int(1000*(timeAfterAskLoad-timeBeforeAskLoad))
	timeAskLoadSummary=str(duration)
	# TRANSMISSIONTOTAL[carrierNumber]=TRANSMISSIONTOTAL[carrierNumber]+(timeAfterAskLoad-timeBeforeAskLoad)
	# transmissionAverage = str(int(1000*(TRANSMISSIONTOTAL[carrierNumber]/(nameOfThread+1)*NUMBER_OF_CAR)))
	
	# timeLastPretty=""
	timeBeforeAskLoad=str(round(timeBeforeAskLoad,4))
	timeBeforeAskLoad=timeBeforeAskLoad[6:]
	timeLast=str(round(time.time(),3))
	timeLast=timeLast[6:]
	timeAskLoadSummary=timeBeforeAskLoad+"\t"+timeAskLoadSummary #+" avr " + transmissionAverage
			# name timeBormi timeBer timeOdamtili bormiStatus error loadInfo oldikmiStatus
	# st= STRINGTOPRINT+" "+str(nameOfThread)+" "+str(carrierNumber)+"\t"+timeAskLoadSummary+"\t"+timeLast+"\t"+timeLastPretty+"\t"++"\t"+str(errorPercentage)+"\t"+newLoadInfo
	st= "\t".join([isBot, timeAskLoadSummary ])
	# st= " ".join([isBot, timeAskLoadSummary, newLoadInfo ])

	returnJson["askStatus"]=askLoadRequest.status_code
	returnJson["isbot"]=loads["isBotRequest"]
	returnJson["carrierEngagementCategory"]=loads["carrierDetails"]["carrierEngagementCategory"]
	returnJson["askSentAt"]=timeBeforeAskLoad
	returnJson["askStatus"]=askLoadRequest.status_code
	returnJson["askDur"]=duration


	return returnJson #jsonify(returnJson)
	# return st #"lalal "+str(timeAfterAskLoad-timeBeforeAskLoad)+" "+askLoadRequest.text #+"\n"+ jsonify()


@app.route('/test', methods=['POST'])
def test():
	global SES
	url = request.form['url']
	carrierPerformanceCategory=request.form['carrierPerformanceCategory']
	priorityAccessVersion=request.form['priorityAccessVersion']
	headers=json.loads(request.form['header'])
	getLoadHeader=json.loads(request.form['getLoadHeader'])
	timeBeforeAskLoad=time.time()
	askLoadRequest = SES.get(url, headers=headers)  #verify=False   
	timeAfterAskLoad=time.time()
	newLoadInfo="-"
	if askLoadRequest.status_code!=200 :
		return str(askLoadRequest.status_code)
			# 111
	else :
		sampleLoad='{"workOpportunities":[{"id":"55ecc6d4-a17f-4ee2-a7d6-9a9072e143b9","version":2,"entityType":null,"operatorIds":null,"startTime":"2020-04-22T16:45:00Z","endTime":"2020-04-24T00:27:00Z","expirationTime":null,"stopCount":2,"isRetendered":false,"isUnaccepted":false,"payout":{"value":3704.488633600000,"unit":"USD"},"transitOperatorType":"SINGLE_DRIVER","tourState":"work-opportunity","firstPickupTime":"2020-04-22T16:45:00Z","lastDeliveryTime":"2020-04-24T00:27:00Z","totalDistance":{"value":993.034,"unit":"miles"},"loads":[{"versionedLoadId":{"id":"tr-225013d5-a7ce-4316-9d21-8aca6d8a480f","version":null},"stops":[{"stopId":null,"stopType":"PICKUP","stopSequenceNumber":1,"location":{"label":"SAT2","line1":"1401 E McCarty Lane","line2":null,"line3":null,"city":"SAN MARCOS","state":"TX","country":"US","postalCode":"78666-8969","latitude":29.837260061445246,"longitude":-97.96348929405212,"timeZone":"America/Chicago","vendorCodes":null},"locationCode":"SAT2","weight":{"value":10000.0,"unit":"pounds"},"actions":[{"type":"CHECKIN","plannedTime":"2020-04-22T16:45:00Z","actualTime":null,"actualTimeSource":null,"delayReport":null,"yardEvents":null},{"type":"CHECKOUT","plannedTime":"2020-04-22T17:00:00Z","actualTime":null,"actualTimeSource":null,"delayReport":null,"yardEvents":null}],"trailerDetails":[{"assetId":null,"assetSource":null,"assetOwner":"AZNG","assetType":null,"trailerLoadingStatus":null,"dropTrailerETA":null}],"loadingType":"PRELOADED","unloadingType":null,"pickupInstructions":null,"deliveryInstructions":null,"pickupNumbers":null,"deliveryNumbers":null,"contacts":null,"isVendorLocation":null,"dropTrailerTime":null},{"stopId":null,"stopType":"DROPOFF","stopSequenceNumber":2,"location":{"label":"DEN5","line1":"19799 E 36th Drive","line2":null,"line3":null,"city":"AURORA","state":"CO","country":"US","postalCode":"80011","latitude":39.7665397,"longitude":-104.756452,"timeZone":"America/Denver","vendorCodes":null},"locationCode":"DEN5","weight":null,"actions":[{"type":"CHECKIN","plannedTime":"2020-04-24T00:27:00Z","actualTime":null,"actualTimeSource":null,"delayReport":null,"yardEvents":null},{"type":"CHECKOUT","plannedTime":"2020-04-24T01:27:00Z","actualTime":null,"actualTimeSource":null,"delayReport":null,"yardEvents":null}],"trailerDetails":[],"loadingType":null,"unloadingType":"DROP","pickupInstructions":null,"deliveryInstructions":null,"pickupNumbers":null,"deliveryNumbers":null,"contacts":null,"isVendorLocation":null,"dropTrailerTime":null}],"loadType":"LOADED","equipmentType":"FIFTY_THREE_FOOT_TRUCK","weight":null,"distance":{"value":993.034,"unit":"miles"},"payout":{"value":3704.488633600000,"unit":"USD"},"costItems":[{"name":"Fuel Surcharge","monetaryAmount":{"value":198.6814000000000,"unit":"USD"}},{"name":"Base Rate","monetaryAmount":{"value":3505.807233600000,"unit":"USD"}}],"specialServices":[],"shipperReferenceNumbers":null,"purchaseOrders":null,"isExternalLoad":false,"workOpportunityId":"55ecc6d4-a17f-4ee2-a7d6-9a9072e143b9","loadfreightType":"TRUCKLOAD"}],"aggregatedCostItems":[{"name":"Fuel Surcharge","monetaryAmount":{"value":198.6814000000000,"unit":"USD"}},{"name":"Base Rate","monetaryAmount":{"value":3505.807233600000,"unit":"USD"}}],"workType":"SPOT","workOpportunityOptionId":"1","workOpportunityType":"ONE_WAY","deadhead":null,"createdAtTime":"2020-04-22T15:58:02.099Z","endPriorityTime":"2020-04-22T16:01:02.099Z","shouldShowPriorityBadge":true,"workOpportunityArrivalWindows":[],"matchDeviationDetails":null,"adHocLoad":false}],"carrierDetails":{"carrierPerformanceScore":98.1,"carrierEngagementScore":496,"carrierPerformanceCategory":"HIGH","carrierEngagementCategory":"HIGH"},"nextItemToken":null,"totalResultsSize":1}'
		loads =  json.loads(sampleLoad) #) sampleLoad)# askLoadRequest.text #TESTTESTTES
		if loads["totalResultsSize"] > 0:
			firstLoad = loads["workOpportunities"][0]	 
			link = "https://relay.amazon.com/api/tours/loadboard/%s/%s/option/%s" % (firstLoad["id"], firstLoad["version"], firstLoad["workOpportunityOptionId"])
			auditContextMap={
				"rlbChannel": "EXACT_MATCH",
				"searchResultIndex": "0",
				"workOpportunityId": "%s" % firstLoad["id"],
				"time": "%s" % (int(time.time() * 1000) - 25),
				"carrierPerformanceCategory": carrierPerformanceCategory,
				"priorityAccessVersion": priorityAccessVersion, #"priorityAccessVersion2",
				"isPriorityAccessEnabled": "true",
				"isPickupTimeChanged": "false",
				"originalPickupTime": "%s" % firstLoad["startTime"],
				"newPickupTime": "%s" % firstLoad["startTime"],
				"truckCapacityOrderVersion": "",
				"carrierType": "BROKERAGE",
				"searchSource": ""
			}
			js = {"totalCost":{"value": firstLoad["payout"]["value"],"unit":"USD"},"auditContextMap":"%s" % json.dumps(auditContextMap),"searchURL":""} 
			json_mylist = json.dumps(js, separators=(',', ':')) 

			r = SES.post(link, data=json_mylist, headers=getLoadHeader)
			FINISH = True
			if r.status_code==200:
				weGotTheLoad = "Alhamdulillah "
				errorTextCode="Alhamdulillah "
			else:
				weGotTheLoad = "Hasbunallah Wa Nimal-Wakil "
				errorTextCode=json.loads(r.text) 
				errorTextCode=errorTextCode["errorCode"]
				return errorTextCode
			# print(weGotTheLoad)

	return "wrong"


@app.route('/many', methods=['POST'])
def many():
	global SES
	global returnJsonMany
	global bigJSON
	global counter
	returnJsonMany={
		"isbot": False,
		"carrierEngagementCategory":"None",
		"askSentAt":0,
		"askStatus":0,
		"askDur":0.0,
		"booked":"None",
		"details":"None",
		"counter": counter
	}
	counter=counter+1

	url = request.form['url']
	carrierPerformanceCategory=request.form['carrierPerformanceCategory']
	priorityAccessVersion=request.form['priorityAccessVersion']
	headers=json.loads(request.form['header'])
	getLoadHeader=json.loads(request.form['getLoadHeader'])
	bigJSON=json.loads(request.form['bigJSON'])
	timeBeforeAskLoad=time.time()
	askLoadRequest = SES.get(url, headers=headers)  #verify=False   
	timeAfterAskLoad=time.time()
	newLoadInfo="-"
	if askLoadRequest.status_code!=200 :
		returnJson["askStatus"]=askLoadRequest.status_code
		return returnJsonMany
			# 111
	else :

		loads =  json.loads(askLoadRequest.text) #) sampleLoad)# askLoadRequest.text #TESTTESTTES
		if loads["totalResultsSize"] > 0:
			# firstLoad = loads["workOpportunities"]  
			ll2 = loads["workOpportunities"][0]  
			newLoadCheck(loads["workOpportunities"],carrierPerformanceCategory,priorityAccessVersion,getLoadHeader)

		null=None
		isBot=str(loads["isBotRequest"])+"\t"+ loads["carrierDetails"]["carrierEngagementCategory"]
	duration= int(1000*(timeAfterAskLoad-timeBeforeAskLoad))
	timeAskLoadSummary=str(duration)
	# TRANSMISSIONTOTAL[carrierNumber]=TRANSMISSIONTOTAL[carrierNumber]+(timeAfterAskLoad-timeBeforeAskLoad)
	# transmissionAverage = str(int(1000*(TRANSMISSIONTOTAL[carrierNumber]/(nameOfThread+1)*NUMBER_OF_CAR)))
	
	# timeLastPretty=""
	timeBeforeAskLoad=str(round(timeBeforeAskLoad,4))
	timeBeforeAskLoad=timeBeforeAskLoad[6:]
	timeLast=str(round(time.time(),3))
	timeLast=timeLast[6:]
	timeAskLoadSummary=timeBeforeAskLoad+"\t"+timeAskLoadSummary #+" avr " + transmissionAverage
			# name timeBormi timeBer timeOdamtili bormiStatus error loadInfo oldikmiStatus
	# st= STRINGTOPRINT+" "+str(nameOfThread)+" "+str(carrierNumber)+"\t"+timeAskLoadSummary+"\t"+timeLast+"\t"+timeLastPretty+"\t"++"\t"+str(errorPercentage)+"\t"+newLoadInfo
	st= "\t".join([isBot, timeAskLoadSummary ])
	# st= " ".join([isBot, timeAskLoadSummary, newLoadInfo ])

	returnJsonMany["askStatus"]=askLoadRequest.status_code
	returnJsonMany["isbot"]=loads["isBotRequest"]
	returnJsonMany["carrierEngagementCategory"]=loads["carrierDetails"]["carrierEngagementCategory"]
	returnJsonMany["askSentAt"]=timeBeforeAskLoad
	returnJsonMany["askStatus"]=askLoadRequest.status_code
	returnJsonMany["askDur"]=duration

	return returnJsonMany #jsonify(returnJson)
	# return st #"lalal "+str(timeAfterAskLoad-timeBeforeAskLoad)+" "+askLoadRequest.text #+"\n"+ jsonify()

############################################################################
##############################	PICK UP ONLY  ##############################
############################################################################
@app.route('/manypu', methods=['POST'])
def manypu():
	global SES
	global returnJsonMany
	global bigJSON
	global counter
	returnJsonMany={
		"isbot": False,
		"carrierEngagementCategory":"None",
		"askSentAt":0,
		"askStatus":0,
		"askDur":0.0,
		"booked":"None",
		"details":"None",
		"counter": counter
	}
	counter=counter+1

	url = request.form['url']
	carrierPerformanceCategory=request.form['carrierPerformanceCategory']
	priorityAccessVersion=request.form['priorityAccessVersion']
	headers=json.loads(request.form['header'])
	getLoadHeader=json.loads(request.form['getLoadHeader'])
	bigJSON=json.loads(request.form['bigJSON'])
	timeBeforeAskLoad=time.time()
	askLoadRequest = SES.get(url, headers=headers)  #verify=False   
	timeAfterAskLoad=time.time()
	newLoadInfo="-"
	if askLoadRequest.status_code!=200 :
		returnJson["askStatus"]=askLoadRequest.status_code
		return returnJsonMany
			# 111
	else :

		loads =  json.loads(askLoadRequest.text) #) sampleLoad)# askLoadRequest.text #TESTTESTTES
		if loads["totalResultsSize"] > 0:
			# firstLoad = loads["workOpportunities"]  
			ll2 = loads["workOpportunities"][0]  
			newLoadCheckPU(loads["workOpportunities"],carrierPerformanceCategory,priorityAccessVersion,getLoadHeader)

		null=None
		isBot=str(loads["isBotRequest"])+"\t"+ loads["carrierDetails"]["carrierEngagementCategory"]
	duration= int(1000*(timeAfterAskLoad-timeBeforeAskLoad))
	timeAskLoadSummary=str(duration)
	# TRANSMISSIONTOTAL[carrierNumber]=TRANSMISSIONTOTAL[carrierNumber]+(timeAfterAskLoad-timeBeforeAskLoad)
	# transmissionAverage = str(int(1000*(TRANSMISSIONTOTAL[carrierNumber]/(nameOfThread+1)*NUMBER_OF_CAR)))
	
	# timeLastPretty=""
	timeBeforeAskLoad=str(round(timeBeforeAskLoad,4))
	timeBeforeAskLoad=timeBeforeAskLoad[6:]
	timeLast=str(round(time.time(),3))
	timeLast=timeLast[6:]
	timeAskLoadSummary=timeBeforeAskLoad+"\t"+timeAskLoadSummary #+" avr " + transmissionAverage
			# name timeBormi timeBer timeOdamtili bormiStatus error loadInfo oldikmiStatus
	# st= STRINGTOPRINT+" "+str(nameOfThread)+" "+str(carrierNumber)+"\t"+timeAskLoadSummary+"\t"+timeLast+"\t"+timeLastPretty+"\t"++"\t"+str(errorPercentage)+"\t"+newLoadInfo
	st= "\t".join([isBot, timeAskLoadSummary ])
	# st= " ".join([isBot, timeAskLoadSummary, newLoadInfo ])

	returnJsonMany["askStatus"]=askLoadRequest.status_code
	returnJsonMany["isbot"]=loads["isBotRequest"]
	returnJsonMany["carrierEngagementCategory"]=loads["carrierDetails"]["carrierEngagementCategory"]
	returnJsonMany["askSentAt"]=timeBeforeAskLoad
	returnJsonMany["askStatus"]=askLoadRequest.status_code
	returnJsonMany["askDur"]=duration

	return returnJsonMany #jsonify(returnJson)
	# return st #"lalal "+str(timeAfterAskLoad-timeBeforeAskLoad)+" "+askLoadRequest.text #+"\n"+ jsonify()

@app.route('/manydel', methods=['POST'])
def manydel():
	global SES
	global returnJsonMany
	global bigJSON
	global counter
	returnJsonMany={
		"isbot": False,
		"carrierEngagementCategory":"None",
		"askSentAt":0,
		"askStatus":0,
		"askDur":0.0,
		"booked":"None",
		"details":"None",
		"counter": counter
	}
	counter=counter+1

	url = request.form['url']
	carrierPerformanceCategory=request.form['carrierPerformanceCategory']
	priorityAccessVersion=request.form['priorityAccessVersion']
	headers=json.loads(request.form['header'])
	getLoadHeader=json.loads(request.form['getLoadHeader'])
	bigJSON=json.loads(request.form['bigJSON'])
	timeBeforeAskLoad=time.time()
	askLoadRequest = SES.get(url, headers=headers)  #verify=False   
	timeAfterAskLoad=time.time()
	newLoadInfo="-"
	if askLoadRequest.status_code!=200 :
		returnJson["askStatus"]=askLoadRequest.status_code
		return returnJsonMany
			# 111
	else :

		loads =  json.loads(askLoadRequest.text) #) sampleLoad)# askLoadRequest.text #TESTTESTTES
		if loads["totalResultsSize"] > 0:
			# firstLoad = loads["workOpportunities"]  
			ll2 = loads["workOpportunities"][0]  
			newLoadCheckDEL(loads["workOpportunities"],carrierPerformanceCategory,priorityAccessVersion,getLoadHeader)

		null=None
		isBot=str(loads["isBotRequest"])+"\t"+ loads["carrierDetails"]["carrierEngagementCategory"]
	duration= int(1000*(timeAfterAskLoad-timeBeforeAskLoad))
	timeAskLoadSummary=str(duration)
	# TRANSMISSIONTOTAL[carrierNumber]=TRANSMISSIONTOTAL[carrierNumber]+(timeAfterAskLoad-timeBeforeAskLoad)
	# transmissionAverage = str(int(1000*(TRANSMISSIONTOTAL[carrierNumber]/(nameOfThread+1)*NUMBER_OF_CAR)))
	
	# timeLastPretty=""
	timeBeforeAskLoad=str(round(timeBeforeAskLoad,4))
	timeBeforeAskLoad=timeBeforeAskLoad[6:]
	timeLast=str(round(time.time(),3))
	timeLast=timeLast[6:]
	timeAskLoadSummary=timeBeforeAskLoad+"\t"+timeAskLoadSummary #+" avr " + transmissionAverage
			# name timeBormi timeBer timeOdamtili bormiStatus error loadInfo oldikmiStatus
	# st= STRINGTOPRINT+" "+str(nameOfThread)+" "+str(carrierNumber)+"\t"+timeAskLoadSummary+"\t"+timeLast+"\t"+timeLastPretty+"\t"++"\t"+str(errorPercentage)+"\t"+newLoadInfo
	st= "\t".join([isBot, timeAskLoadSummary ])
	# st= " ".join([isBot, timeAskLoadSummary, newLoadInfo ])

	returnJsonMany["askStatus"]=askLoadRequest.status_code
	returnJsonMany["isbot"]=loads["isBotRequest"]
	returnJsonMany["carrierEngagementCategory"]=loads["carrierDetails"]["carrierEngagementCategory"]
	returnJsonMany["askSentAt"]=timeBeforeAskLoad
	returnJsonMany["askStatus"]=askLoadRequest.status_code
	returnJsonMany["askDur"]=duration

	return returnJsonMany #jsonify(returnJson)
	# return st #"lalal "+str(timeAfterAskLoad-timeBeforeAskLoad)+" "+askLoadRequest.text #+"\n"+ jsonify()

@app.route('/manypudel', methods=['POST'])
def manypudel():
	global SES
	global returnJsonMany
	global bigJSON
	global counter
	returnJsonMany={
		"isbot": False,
		"carrierEngagementCategory":"None",
		"askSentAt":0,
		"askStatus":0,
		"askDur":0.0,
		"booked":"None",
		"details":"None",
		"counter": counter
	}
	counter=counter+1

	url = request.form['url']
	carrierPerformanceCategory=request.form['carrierPerformanceCategory']
	priorityAccessVersion=request.form['priorityAccessVersion']
	headers=json.loads(request.form['header'])
	getLoadHeader=json.loads(request.form['getLoadHeader'])
	bigJSON=json.loads(request.form['bigJSON'])
	timeBeforeAskLoad=time.time()
	askLoadRequest = SES.get(url, headers=headers)  #verify=False   
	timeAfterAskLoad=time.time()
	newLoadInfo="-"
	if askLoadRequest.status_code!=200 :
		returnJson["askStatus"]=askLoadRequest.status_code
		return returnJsonMany
			# 111
	else :

		loads =  json.loads(askLoadRequest.text) #) sampleLoad)# askLoadRequest.text #TESTTESTTES
		if loads["totalResultsSize"] > 0:
			# firstLoad = loads["workOpportunities"]  
			ll2 = loads["workOpportunities"][0]  
			newLoadCheckPUDEL(loads["workOpportunities"],carrierPerformanceCategory,priorityAccessVersion,getLoadHeader)

		null=None
		isBot=str(loads["isBotRequest"])+"\t"+ loads["carrierDetails"]["carrierEngagementCategory"]
	duration= int(1000*(timeAfterAskLoad-timeBeforeAskLoad))
	timeAskLoadSummary=str(duration)
	# TRANSMISSIONTOTAL[carrierNumber]=TRANSMISSIONTOTAL[carrierNumber]+(timeAfterAskLoad-timeBeforeAskLoad)
	# transmissionAverage = str(int(1000*(TRANSMISSIONTOTAL[carrierNumber]/(nameOfThread+1)*NUMBER_OF_CAR)))
	
	# timeLastPretty=""
	timeBeforeAskLoad=str(round(timeBeforeAskLoad,4))
	timeBeforeAskLoad=timeBeforeAskLoad[6:]
	timeLast=str(round(time.time(),3))
	timeLast=timeLast[6:]
	timeAskLoadSummary=timeBeforeAskLoad+"\t"+timeAskLoadSummary #+" avr " + transmissionAverage
			# name timeBormi timeBer timeOdamtili bormiStatus error loadInfo oldikmiStatus
	# st= STRINGTOPRINT+" "+str(nameOfThread)+" "+str(carrierNumber)+"\t"+timeAskLoadSummary+"\t"+timeLast+"\t"+timeLastPretty+"\t"++"\t"+str(errorPercentage)+"\t"+newLoadInfo
	st= "\t".join([isBot, timeAskLoadSummary ])
	# st= " ".join([isBot, timeAskLoadSummary, newLoadInfo ])

	returnJsonMany["askStatus"]=askLoadRequest.status_code
	returnJsonMany["isbot"]=loads["isBotRequest"]
	returnJsonMany["carrierEngagementCategory"]=loads["carrierDetails"]["carrierEngagementCategory"]
	returnJsonMany["askSentAt"]=timeBeforeAskLoad
	returnJsonMany["askStatus"]=askLoadRequest.status_code
	returnJsonMany["askDur"]=duration

	return returnJsonMany #jsonify(returnJson)
	# return st #"lalal "+str(timeAfterAskLoad-timeBeforeAskLoad)+" "+askLoadRequest.text #+"\n"+ jsonify()

@app.route('/manypurate', methods=['POST'])
def manypurate():
	global SES
	global returnJsonMany
	global bigJSON
	global counter
	returnJsonMany={
		"isbot": False,
		"carrierEngagementCategory":"None",
		"askSentAt":0,
		"askStatus":0,
		"askDur":0.0,
		"booked":"None",
		"details":"None",
		"counter": counter
	}
	counter=counter+1

	url = request.form['url']
	carrierPerformanceCategory=request.form['carrierPerformanceCategory']
	priorityAccessVersion=request.form['priorityAccessVersion']
	headers=json.loads(request.form['header'])
	getLoadHeader=json.loads(request.form['getLoadHeader'])
	bigJSON=json.loads(request.form['bigJSON'])
	timeBeforeAskLoad=time.time()
	askLoadRequest = SES.get(url, headers=headers)  #verify=False   
	timeAfterAskLoad=time.time()
	newLoadInfo="-"
	if askLoadRequest.status_code!=200 :
		returnJson["askStatus"]=askLoadRequest.status_code
		return returnJsonMany
			# 111
	else :

		loads =  json.loads(askLoadRequest.text) #) sampleLoad)# askLoadRequest.text #TESTTESTTES
		if loads["totalResultsSize"] > 0:
			# firstLoad = loads["workOpportunities"]  
			ll2 = loads["workOpportunities"][0]  
			newLoadCheckPURATE(loads["workOpportunities"],carrierPerformanceCategory,priorityAccessVersion,getLoadHeader)

		null=None
		isBot=str(loads["isBotRequest"])+"\t"+ loads["carrierDetails"]["carrierEngagementCategory"]
	duration= int(1000*(timeAfterAskLoad-timeBeforeAskLoad))
	timeAskLoadSummary=str(duration)
	# TRANSMISSIONTOTAL[carrierNumber]=TRANSMISSIONTOTAL[carrierNumber]+(timeAfterAskLoad-timeBeforeAskLoad)
	# transmissionAverage = str(int(1000*(TRANSMISSIONTOTAL[carrierNumber]/(nameOfThread+1)*NUMBER_OF_CAR)))
	
	# timeLastPretty=""
	timeBeforeAskLoad=str(round(timeBeforeAskLoad,4))
	timeBeforeAskLoad=timeBeforeAskLoad[6:]
	timeLast=str(round(time.time(),3))
	timeLast=timeLast[6:]
	timeAskLoadSummary=timeBeforeAskLoad+"\t"+timeAskLoadSummary #+" avr " + transmissionAverage
			# name timeBormi timeBer timeOdamtili bormiStatus error loadInfo oldikmiStatus
	# st= STRINGTOPRINT+" "+str(nameOfThread)+" "+str(carrierNumber)+"\t"+timeAskLoadSummary+"\t"+timeLast+"\t"+timeLastPretty+"\t"++"\t"+str(errorPercentage)+"\t"+newLoadInfo
	st= "\t".join([isBot, timeAskLoadSummary ])
	# st= " ".join([isBot, timeAskLoadSummary, newLoadInfo ])

	returnJsonMany["askStatus"]=askLoadRequest.status_code
	returnJsonMany["isbot"]=loads["isBotRequest"]
	returnJsonMany["carrierEngagementCategory"]=loads["carrierDetails"]["carrierEngagementCategory"]
	returnJsonMany["askSentAt"]=timeBeforeAskLoad
	returnJsonMany["askStatus"]=askLoadRequest.status_code
	returnJsonMany["askDur"]=duration

	return returnJsonMany #jsonify(returnJson)
	# return st #"lalal "+str(timeAfterAskLoad-timeBeforeAskLoad)+" "+askLoadRequest.text #+"\n"+ jsonify()

@app.route('/manypudelrate', methods=['POST'])
def manypudelrate():
	global SES
	global returnJsonMany
	global bigJSON
	global counter
	returnJsonMany={
		"isbot": False,
		"carrierEngagementCategory":"None",
		"askSentAt":0,
		"askStatus":0,
		"askDur":0.0,
		"booked":"None",
		"details":"None",
		"counter": counter
	}
	counter=counter+1

	url = request.form['url']
	carrierPerformanceCategory=request.form['carrierPerformanceCategory']
	priorityAccessVersion=request.form['priorityAccessVersion']
	headers=json.loads(request.form['header'])
	getLoadHeader=json.loads(request.form['getLoadHeader'])
	bigJSON=json.loads(request.form['bigJSON'])
	timeBeforeAskLoad=time.time()
	askLoadRequest = SES.get(url, headers=headers)  #verify=False   
	timeAfterAskLoad=time.time()
	newLoadInfo="-"
	if askLoadRequest.status_code!=200 :
		returnJson["askStatus"]=askLoadRequest.status_code
		return returnJsonMany
			# 111
	else :

		loads =  json.loads(askLoadRequest.text) #) sampleLoad)# askLoadRequest.text #TESTTESTTES
		if loads["totalResultsSize"] > 0:
			# firstLoad = loads["workOpportunities"]  
			ll2 = loads["workOpportunities"][0]  
			newLoadCheckPUDELRATE(loads["workOpportunities"],carrierPerformanceCategory,priorityAccessVersion,getLoadHeader)

		null=None
		isBot=str(loads["isBotRequest"])+"\t"+ loads["carrierDetails"]["carrierEngagementCategory"]
	duration= int(1000*(timeAfterAskLoad-timeBeforeAskLoad))
	timeAskLoadSummary=str(duration)
	# TRANSMISSIONTOTAL[carrierNumber]=TRANSMISSIONTOTAL[carrierNumber]+(timeAfterAskLoad-timeBeforeAskLoad)
	# transmissionAverage = str(int(1000*(TRANSMISSIONTOTAL[carrierNumber]/(nameOfThread+1)*NUMBER_OF_CAR)))
	
	# timeLastPretty=""
	timeBeforeAskLoad=str(round(timeBeforeAskLoad,4))
	timeBeforeAskLoad=timeBeforeAskLoad[6:]
	timeLast=str(round(time.time(),3))
	timeLast=timeLast[6:]
	timeAskLoadSummary=timeBeforeAskLoad+"\t"+timeAskLoadSummary #+" avr " + transmissionAverage
			# name timeBormi timeBer timeOdamtili bormiStatus error loadInfo oldikmiStatus
	# st= STRINGTOPRINT+" "+str(nameOfThread)+" "+str(carrierNumber)+"\t"+timeAskLoadSummary+"\t"+timeLast+"\t"+timeLastPretty+"\t"++"\t"+str(errorPercentage)+"\t"+newLoadInfo
	st= "\t".join([isBot, timeAskLoadSummary ])
	# st= " ".join([isBot, timeAskLoadSummary, newLoadInfo ])

	returnJsonMany["askStatus"]=askLoadRequest.status_code
	returnJsonMany["isbot"]=loads["isBotRequest"]
	returnJsonMany["carrierEngagementCategory"]=loads["carrierDetails"]["carrierEngagementCategory"]
	returnJsonMany["askSentAt"]=timeBeforeAskLoad
	returnJsonMany["askStatus"]=askLoadRequest.status_code
	returnJsonMany["askDur"]=duration

	return returnJsonMany #jsonify(returnJson)
	# return st #"lalal "+str(timeAfterAskLoad-timeBeforeAskLoad)+" "+askLoadRequest.text #+"\n"+ jsonify()

@app.route('/manydelrate', methods=['POST'])
def manydelrate():
	global SES
	global returnJsonMany
	global bigJSON
	global counter
	returnJsonMany={
		"isbot": False,
		"carrierEngagementCategory":"None",
		"askSentAt":0,
		"askStatus":0,
		"askDur":0.0,
		"booked":"None",
		"details":"None",
		"counter": counter
	}
	counter=counter+1

	url = request.form['url']
	carrierPerformanceCategory=request.form['carrierPerformanceCategory']
	priorityAccessVersion=request.form['priorityAccessVersion']
	headers=json.loads(request.form['header'])
	getLoadHeader=json.loads(request.form['getLoadHeader'])
	bigJSON=json.loads(request.form['bigJSON'])
	timeBeforeAskLoad=time.time()
	askLoadRequest = SES.get(url, headers=headers)  #verify=False   
	timeAfterAskLoad=time.time()
	newLoadInfo="-"
	if askLoadRequest.status_code!=200 :
		returnJson["askStatus"]=askLoadRequest.status_code
		return returnJsonMany
			# 111
	else :

		loads =  json.loads(askLoadRequest.text) #) sampleLoad)# askLoadRequest.text #TESTTESTTES
		if loads["totalResultsSize"] > 0:
			# firstLoad = loads["workOpportunities"]  
			ll2 = loads["workOpportunities"][0]  
			newLoadCheckDELRATE(loads["workOpportunities"],carrierPerformanceCategory,priorityAccessVersion,getLoadHeader)

		null=None
		isBot=str(loads["isBotRequest"])+"\t"+ loads["carrierDetails"]["carrierEngagementCategory"]
	duration= int(1000*(timeAfterAskLoad-timeBeforeAskLoad))
	timeAskLoadSummary=str(duration)
	# TRANSMISSIONTOTAL[carrierNumber]=TRANSMISSIONTOTAL[carrierNumber]+(timeAfterAskLoad-timeBeforeAskLoad)
	# transmissionAverage = str(int(1000*(TRANSMISSIONTOTAL[carrierNumber]/(nameOfThread+1)*NUMBER_OF_CAR)))
	
	# timeLastPretty=""
	timeBeforeAskLoad=str(round(timeBeforeAskLoad,4))
	timeBeforeAskLoad=timeBeforeAskLoad[6:]
	timeLast=str(round(time.time(),3))
	timeLast=timeLast[6:]
	timeAskLoadSummary=timeBeforeAskLoad+"\t"+timeAskLoadSummary #+" avr " + transmissionAverage
			# name timeBormi timeBer timeOdamtili bormiStatus error loadInfo oldikmiStatus
	# st= STRINGTOPRINT+" "+str(nameOfThread)+" "+str(carrierNumber)+"\t"+timeAskLoadSummary+"\t"+timeLast+"\t"+timeLastPretty+"\t"++"\t"+str(errorPercentage)+"\t"+newLoadInfo
	st= "\t".join([isBot, timeAskLoadSummary ])
	# st= " ".join([isBot, timeAskLoadSummary, newLoadInfo ])

	returnJsonMany["askStatus"]=askLoadRequest.status_code
	returnJsonMany["isbot"]=loads["isBotRequest"]
	returnJsonMany["carrierEngagementCategory"]=loads["carrierDetails"]["carrierEngagementCategory"]
	returnJsonMany["askSentAt"]=timeBeforeAskLoad
	returnJsonMany["askStatus"]=askLoadRequest.status_code
	returnJsonMany["askDur"]=duration

	return returnJsonMany #jsonify(returnJson)
	# return st #"lalal "+str(timeAfterAskLoad-timeBeforeAskLoad)+" "+askLoadRequest.text #+"\n"+ jsonify()

	 
############################################################################
##############################	PICK UP ONLY  ##############################
############################################################################
