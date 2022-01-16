import threading 
import os
import sys 
import signal
import requests
import json
import time
from ddata import *
from cookies import *

sampleLoad='{"workOpportunities":[{"id":"55ecc6d4-a17f-4ee2-a7d6-9a9072e143b9","version":2,"entityType":null,"operatorIds":null,"startTime":"2020-04-22T16:45:00Z","endTime":"2020-04-24T00:27:00Z","expirationTime":null,"stopCount":2,"isRetendered":false,"isUnaccepted":false,"payout":{"value":3704.488633600000,"unit":"USD"},"transitOperatorType":"SINGLE_DRIVER","tourState":"work-opportunity","firstPickupTime":"2020-04-22T16:45:00Z","lastDeliveryTime":"2020-04-24T00:27:00Z","totalDistance":{"value":993.034,"unit":"miles"},"loads":[{"versionedLoadId":{"id":"tr-225013d5-a7ce-4316-9d21-8aca6d8a480f","version":null},"stops":[{"stopId":null,"stopType":"PICKUP","stopSequenceNumber":1,"location":{"label":"SAT2","line1":"1401 E McCarty Lane","line2":null,"line3":null,"city":"SAN MARCOS","state":"TX","country":"US","postalCode":"78666-8969","latitude":29.837260061445246,"longitude":-97.96348929405212,"timeZone":"America/Chicago","vendorCodes":null},"locationCode":"SAT2","weight":{"value":10000.0,"unit":"pounds"},"actions":[{"type":"CHECKIN","plannedTime":"2020-04-22T16:45:00Z","actualTime":null,"actualTimeSource":null,"delayReport":null,"yardEvents":null},{"type":"CHECKOUT","plannedTime":"2020-04-22T17:00:00Z","actualTime":null,"actualTimeSource":null,"delayReport":null,"yardEvents":null}],"trailerDetails":[{"assetId":null,"assetSource":null,"assetOwner":"AZNG","assetType":null,"trailerLoadingStatus":null,"dropTrailerETA":null}],"loadingType":"PRELOADED","unloadingType":null,"pickupInstructions":null,"deliveryInstructions":null,"pickupNumbers":null,"deliveryNumbers":null,"contacts":null,"isVendorLocation":null,"dropTrailerTime":null},{"stopId":null,"stopType":"DROPOFF","stopSequenceNumber":2,"location":{"label":"DEN5","line1":"19799 E 36th Drive","line2":null,"line3":null,"city":"AURORA","state":"CO","country":"US","postalCode":"80011","latitude":39.7665397,"longitude":-104.756452,"timeZone":"America/Denver","vendorCodes":null},"locationCode":"DEN5","weight":null,"actions":[{"type":"CHECKIN","plannedTime":"2020-04-24T00:27:00Z","actualTime":null,"actualTimeSource":null,"delayReport":null,"yardEvents":null},{"type":"CHECKOUT","plannedTime":"2020-04-24T01:27:00Z","actualTime":null,"actualTimeSource":null,"delayReport":null,"yardEvents":null}],"trailerDetails":[],"loadingType":null,"unloadingType":"DROP","pickupInstructions":null,"deliveryInstructions":null,"pickupNumbers":null,"deliveryNumbers":null,"contacts":null,"isVendorLocation":null,"dropTrailerTime":null}],"loadType":"LOADED","equipmentType":"FIFTY_THREE_FOOT_TRUCK","weight":null,"distance":{"value":993.034,"unit":"miles"},"payout":{"value":3704.488633600000,"unit":"USD"},"costItems":[{"name":"Fuel Surcharge","monetaryAmount":{"value":198.6814000000000,"unit":"USD"}},{"name":"Base Rate","monetaryAmount":{"value":3505.807233600000,"unit":"USD"}}],"specialServices":[],"shipperReferenceNumbers":null,"purchaseOrders":null,"isExternalLoad":false,"workOpportunityId":"55ecc6d4-a17f-4ee2-a7d6-9a9072e143b9","loadfreightType":"TRUCKLOAD"}],"aggregatedCostItems":[{"name":"Fuel Surcharge","monetaryAmount":{"value":198.6814000000000,"unit":"USD"}},{"name":"Base Rate","monetaryAmount":{"value":3505.807233600000,"unit":"USD"}}],"workType":"SPOT","workOpportunityOptionId":"1","workOpportunityType":"ONE_WAY","deadhead":null,"createdAtTime":"2020-04-22T15:58:02.099Z","endPriorityTime":"2020-04-22T16:01:02.099Z","shouldShowPriorityBadge":true,"workOpportunityArrivalWindows":[],"matchDeviationDetails":null,"adHocLoad":false}],"carrierDetails":{"carrierPerformanceScore":98.1,"carrierEngagementScore":496,"carrierPerformanceCategory":"HIGH","carrierEngagementCategory":"HIGH"},"nextItemToken":null,"totalResultsSize":1}'
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
loads =  json.loads(sampleLoad) #) sampleLoad)# askLoadRequest.text #TESTTESTTES
ll2 = loads["workOpportunities"][0]     
lnk = "https://relay.amazon.com/api/tours/loadboard/%s/%s/option/%s" % (ll2["id"], ll2["version"], ll2["workOpportunityOptionId"])
auditContextMap={"rlbChannel":"EXACT_MATCH","searchResultIndex":"0","workOpportunityId":"%s" % ll2["id"],"time":"%s" % (int(time.time()*1000)),"carrierPerformanceCategory":"HIGH","isPriorityAccessEnabled":"true","isPickupTimeChanged":"false","originalPickupTime":"%s" % ll2["startTime"],"newPickupTime":"%s" % ll2["startTime"],"truckCapacityOrderVersion":"","carrierType":"BROKERAGE","searchSource":""}
js = {"totalCost":{"value": ll2["payout"]["value"],"unit":"USD"},"auditContextMap":"%s" % json.dumps(auditContextMap),"searchURL":""} 
json_mylist = json.dumps(js, separators=(',', ':')) 
r = requests.post(lnk, data=json_mylist, headers=getLoadHeader)
if r.status_code==200:
    rslt = 1
    print("111111111111111")
else:
    print("TEST ")
    rslt = 0
print(str(r.status_code)+" "+r.text)
