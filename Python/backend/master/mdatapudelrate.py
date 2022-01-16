false=False
true=True
null=None

########################################################################################################
########################################################################################################
########################################################################################################
########################################################################################################
bigJSON=[
  {
    "puName": "HEBRON, KY",
    "puRad": 100,
    "puLon": -84.709031,
    "puLat": 39.062615,
    "delName": "SAN BERNARDINO, CA",
    "delRad": 1500,
    "delLon": -116.178456,
    "delLat": 34.841435,
    "payOut": 0,
    "perMile": 2
  },
  {
    "puName": "AURORA, CO",
    "puRad": 75,
    "puLon": -104.72721,
    "puLat": 39.708755,
    "delName": "SAN BERNARDINO, CA",
    "delRad": 1500,
    "delLon": -116.178456,
    "delLat": 34.841435,
    "payOut": 0,
    "perMile": 2
  },{"puLon":-88.101989,"puLat":41.630418,"puTime":0,"delLon":-122.031167,"delLat":37.520408,"delTime":0,"trlStat":"0","tripType":"0","isTeam":"0","stopsCount":2,"nyIchi":0,"puName":"ROMEOVILLE, IL","delName":"NEWARK, CA","payOut":0,"perMile":2,"minDis":10,"maxDis":9999,"puRad":50,"delRad":20,"pickLabels":["MDW2","MDW5","0-159900741","0-79861891","0-140736041","MDW7","KORD","395790-114611","MDW6","DCH4","MDW9","MDW8","0-122664901"],"delLabels":["SJC7","OAK5","OAK4","OAK3","SCF-USFC","0-153567971","KSFO","DSF6","DSF4"],"book":1},
  {"puLon":0,"puLat":0,"puTime":0,"delLon":-75.972387,"delLat":40.950425,"delTime":0,"trlStat":"0","tripType":"0","isTeam":"0","stopsCount":2,"nyIchi":0,"puName":0,"delName":"HAZLETON, PA","payOut":0,"perMile":2,"minDis":10,"maxDis":9999,"puRad":50,"delRad":50,"pickLabels":false,"delLabels":["AVP3","ABE2","AVP1","ABE3","WMAC___M_18031_1538_572","0-97681281","AVP8","P_AND_G__186570001_109","KCDC_EAS_18640_6138_462","ABE4","AVP2","KABE"],"book":1}
]
ADDITION = "del" # pu del pudel pudelrate purate delrate
STRINGTOPRINT='HEBRON, KY | AURORA, CO | 10.4 12300 '+ADDITION

url="https://relay.amazon.com/api/tours/loadboard?sortByField=startTime&sortOrder=asc&endCityLatitude=37.353115&endCityLongitude=-77.434203&endCityRadius=100&endCityName=CHESTER&endCityStateCode=VA&endCityDisplayValue=CHESTER,%20VA&isDestinationCityLive=false&destinationCity=[object%20Object]&maxPayout=750&maxPricePerDistance=1.4&trailerStatusFilters=REQUIRED&trailerStatus=REQUIRED&nextItemToken=0&resultSize=100&searchURL=&savedSearchId=&isAutoRefreshCall=false&notificationId=&auditContextMap={%22rlbChannel%22:%22EXACT_MATCH%22,%22isOriginCityLive%22:%22false%22,%22isDestinationCityLive%22:%22false%22}"
# url='https://relay.amazon.com/api/tours/loadboard?sortByField=startTime&sortOrder=asc&startCityLatitude=39.123462&startCityLongitude=-94.744192&startCityRadius=10&startCityName=KANSAS%20CITY&startCityStateCode=KS&startCityDisplayValue=KANSAS%20CITY,%20KS&isOriginCityLive=false&originCity=[object%20Object]&endCityLatitude=34.841435&endCityLongitude=-116.178456&endCityRadius=13&endCityName=SAN%20BERNARDINO&endCityStateCode=CA&endCityDisplayValue=SAN%20BERNARDINO,%20CA&isDestinationCityLive=false&destinationCity=[object%20Object]&minPayout=12900&maxPayout=12000&minPricePerDistance=10.4&maxPricePerDistance=30&nextItemToken=0&resultSize=100&searchURL=&savedSearchId=&isAutoRefreshCall=false&notificationId=&auditContextMap={%22rlbChannel%22:%22EXACT_MATCH%22,%22isOriginCityLive%22:%22false%22,%22isDestinationCityLive%22:%22false%22}'########################################################################################################
########################################################################################################
########################################################################################################
########################################################################################################
# # QIDIRLVOTGAN YUK HAQIDA MA'LUMOT
# STRINGTOPRINT = " CO, OR, VA, VA "

# # NETWORK TABDAN LINK
# url="https://relay.amazon.com/api/tours/loadboard?sortByField=creationTime&sortOrder=desc&minPayout=1200&maxPayout=12000&minPricePerDistance=1.8&maxPricePerDistance=30&trailerStatusFilters=PROVIDED&trailerStatus=PROVIDED&equipmentTypeFilters=FIFTY_THREE_FOOT_TRUCK,SKIRTED_FIFTY_THREE_FOOT_TRUCK,FIFTY_THREE_FOOT_DRY_VAN&equipmentTypes=FIFTY_THREE_FOOT_TRUCK,SKIRTED_FIFTY_THREE_FOOT_TRUCK,FIFTY_THREE_FOOT_DRY_VAN&nextItemToken=0&resultSize=100&searchURL=&savedSearchId=&isAutoRefreshCall=false&notificationId=&auditContextMap={%22rlbChannel%22:%22EXACT_MATCH%22,%22isOriginCityLive%22:%22false%22,%22isDestinationCityLive%22:%22false%22}"

#  # web saytan olingan ma'lumot 
# bigJSON = [{
#     "puLon": -104.72721,
#     "puLat": 39.708755,
#     "puTime": 0,
#     "delLon": -119.649321,
#     "delLat": 36.75818,
#     "delTime": 0,
#     "trlStat": "0",
#     "tripType": "0",
#     "isTeam": "0",
#     "stopsCount": 2,
#     "nyIchi": 0,
#     "puName": "AURORA, CO",
#     "delName": "FRESNO, CA",
#     "payOut": 0,
#     "perMile": 2,
#     "minDis": 10,
#     "maxDis": 9999,
#     "puRad": 50,
#     "delRad": 800,
#     "pickLabels": ["DEN3", "DEN5", "DEN2"],
#     "delLabels": ["LAS7", "SMF5", "SJC7", "BFI5", "SLC1", "SLC2", "PDX7", "BFI3", "PDX6", "HBF2", "OAK5", "LAS2", "LAX9", "PDX9", "RNO4", "ONT5", "PDX5", "SMF1", "OAK4", "TUS1", "0-92733441", "0-92617131", "0-22895351", "SMF3", "427470-187821", "474310-382201", "0-20065011", "SLC3", "LGB6", "0-3599711", "0-120661971", "0-70532181", "0-3477081", "434750-1261", "0-165565711", "0-124987841", "KONT", "0-56700751", "FAT1", "BFI4", "DID2", "ONT8", "LAS5", "OAK3", "DUT1", "KPDX", "PHX7", "AZA5", "SCF-USFC", "BFI7", "JW-WALWA", "PHX6", "KPHX", "LAX5", "KRIV", "LGB5", "LGB3", "PHX5", "KSEA", "MTS-KONT", "LGB7", "HBI1", "ONT2", "2666270-23231", "0-74525631", "LGB8", "DCA2", "SWA1", "SZ24736", "S013427", "DLV1", "HTC1", "LAS6", "DAX7", "BFI1", "DPD1", "UPS-REDWA", "UPS-SEAWA", "PHX3", "0-147396191", "0-90138271", "0-153567971", "XUSD", "JW-HELMT", "KSFO", "DSM1", "DPS3", "DSF6", "DLA4", "SNA4", "DSE7", "DSE4", "DSF4", "ONT6", "JW-SPOWA", "SCF-USTW", "DSE2", "UWA4", "0-149712751", "XIX7"],
#     "book": 1
# }, {
#     "puLon": -122.650038,
#     "puLat": 45.537178,
#     "puTime": 0,
#     "delLon": 0,
#     "delLat": 0,
#     "delTime": 0,
#     "trlStat": "0",
#     "tripType": "0",
#     "isTeam": "0",
#     "stopsCount": 2,
#     "nyIchi": 0,
#     "puName": "PORTLAND, OR",
#     "delName": 0,
#     "payOut": 0,
#     "perMile": 2,
#     "minDis": 10,
#     "maxDis": 9999,
#     "puRad": 50,
#     "delRad": 50,
#     "pickLabels": ["PDX7", "PDX6", "PDX9", "PDX5", "KPDX", "DPD1"],
#     "delLabels": false,
#     "book": 1
# }, {
#     "puLon": -77.471483,
#     "puLat": 37.759744,
#     "puTime": 0,
#     "delLon": -84.709031,
#     "delLat": 39.062615,
#     "delTime": 0,
#     "trlStat": "0",
#     "tripType": "0",
#     "isTeam": "0",
#     "stopsCount": 2,
#     "nyIchi": 0,
#     "puName": "ASHLAND, VA",
#     "delName": "HEBRON, KY",
#     "payOut": 0,
#     "perMile": 2,
#     "minDis": 10,
#     "maxDis": 9999,
#     "puRad": 50,
#     "delRad": 750,
#     "pickLabels": ["RIC5", "RIC2", "RIC3"],
#     "delLabels": ["IND4", "MDT2", "0-109334481", "IND9", "STL5", "512620-82641", "CLT2", "CVG9", "EWR8", "MSP1", "BUF5", "429430-22271", "MDW2", "BDL5", "MCI5", "MOB5", "0-580311", "XIX4", "CLT3", "RDU5", "GRR1", "MSP5", "EWR4", "US63_COL_08691_827", "DOLLAR_G_12010_433", "BDL2", "LEX1", "DCA1", "STL4", "MSP9", "MDW5", "ACY5", "CHA2", "RIC5", "HMB1", "MEM1", "IND2", "EWR9", "BNA2", "PENNINGTON", "MCI7", "0-159900741", "CLE3", "AVP3", "STL8", "JAX2", "CVG1", "ABE2", "571640-99021", "PNE5", "AVP1", "SDF8", "BOS5", "CAE1", "0-82958791", "ABE3", "WMAC___M_18031_1538_572", "CONSOLID_24401_9699_425", "0-74539431", "MKC4", "MEM5", "CHA1", "CVG2", "PHL7", "0-82892861", "940840-153761", "CMH4", "0-154775551", "356270-296101", "0-79861891", "IND1", "1963870-329451", "0-140736041", "0-21063441", "0-80997361", "MGE5", "432650-242661", "JAX3", "CMH2", "US88_NFI_43762_128", "DOLLAR_G_42164_1670_482", "0-82901481", "CMH1", "BWI5", "0-133345551", "0-143358171", "MDW7", "0-2547011", "0-130275571", "SAV3", "0-57948961", "P_AND_G__637550001_967", "SHIPPENS_172570001_323", "MDT1", "PET PROC", "G-WOOD-PLANT", "ABE8", "BWI2", "SAZERAC", "474310-382221", "0-155677211", "0-95353431", "0-141461861", "356880-70811", "DET1", "BNA5", "0-1415561", "0-165263471", "0-97681281", "ATL6", "US67_APL_30122_681", "DOLLAR_G_32615_8141_774", "JAX5", "V15286", "GSP1", "DAT3", "AVP8", "P_AND_G__186570001_109", "BOS7", "KJFK", "DNY4", "CMH6", "CVG5", "KCVG", "KCDC_EAS_18640_6138_462", "AT-SIOSD", "DTW1", "ACY2", "3M_TONAW_14150_7718_314", "3M_MECHA_17404_712", "DTW5", "RIC2", "KCLT", "LA-BRKNY", "KORD", "395790-114611", "ABE4", "PIT5", "DPP1", "CLT4", "MGE1", "KATL", "3179860-288301", "DMC1", "MKE5", "CMH3", "SDF1", "DCN1", "KSTL", "0-147109971", "PA-KNXTN", "PV13440", "PV14065", "PV15629", "3M_CYNTH_41031_235", "0-5912171", "0-147387751", "MKE1", "PV11932", "PV11861", "PV13523", "PV16012", "PV14011", "PV16574", "MDW6", "0-3344511", "PENGUIN__47933_402", "BDL3", "EWR5", "KILN", "DRO1", "DOR1", "JFK8", "DEW1", "ACY1", "LGA9", "PY21891", "BY22480", "DOK2", "DSC4", "PA-WILNC", "DDC4", "JW-BTRLA", "JW-SPRMO", "SDF4", "UPS-GAIGA", "DFL1", "DBO7", "DSC3", "UPS-SYRNY-P", "DIA3", "WESTROCK_53224_241", "MERCHANT_50313_885", "WESTROCK_50313_493", "DIA4", "DLB1", "DLR1", "KBDL", "DNH2", "DIL1", "MKC6", "DOM1", "BNA3", "PA-GRAMI", "STL7", "STL6", "DDT4", "DKY1", "DGE2", "DBO2", "DNO1", "SCF-UGRM", "PX14494", "PX14886", "PX15118", "PV15377", "PV16836", "PV13178", "PV11986", "LG_HAUSY_30701_290", "608860-194641", "0-156177621", "RIC3", "0-98627431", "0-81006631", "0-60296281", "AVP2", "DCH4", "DDT3", "SX11815", "UPS-GRAMI", "IND5", "MDW9", "DGR1", "DCL3", "DBL1", "KRFD", "MDW8", "ATL8", "XBHM", "BHM1", "DBM2", "DBO6", "DIN3", "DEW4", "KABE", "DCM2", "EXLA-CBS087", "DKY4", "PV25749", "4V25402", "PV25497", "PV25621", "CLE5", "BX23351", "PX21051", "PX20453", "PX24982", "PX25658", "PX25689", "DLT1", "708340-228541", "AXIUM_PL_43054_6651_994", "PG_C_O_N_45804_3928_693", "XALB", "EXLA-DAY067", "US40_GRE_29611_522", "US36_ALL_27105_236", "SCF-UCCO", "PHL6", "SCF-UAAG", "PRC_INDU_28777_6403_786", "LSI_WILK_28659_450", "DISCOUNT_40069_1595_691", "WESTROCK_37921_389", "WESTROCK_35772_636", "SDF9", "CAPITAL__43217_536", "RB_LC_SA_63376_408", "WALGREEN_53598_9621_111", "2539810-150841", "671290-86091", "CLE2", "0-122664901", "0-95073341", "0-142924351", "PX21014", "PX21791"],
#     "book": 1
# }, {
#     "puLon": -77.471483,
#     "puLat": 37.759744,
#     "puTime": 0,
#     "delLon": -116.178456,
#     "delLat": 34.841435,
#     "delTime": 0,
#     "trlStat": "0",
#     "tripType": "0",
#     "isTeam": "0",
#     "stopsCount": 2,
#     "nyIchi": 0,
#     "puName": "ASHLAND, VA",
#     "delName": "SAN BERNARDINO, CA",
#     "payOut": 0,
#     "perMile": 2,
#     "minDis": 10,
#     "maxDis": 9999,
#     "puRad": 50,
#     "delRad": 1500,
#     "pickLabels": ["RIC5", "RIC2", "RIC3"],
#     "delLabels": ["LAS7", "SMF5", "SJC7", "BFI5", "SLC1", "SLC2", "DCS3", "PDX7", "DEN3", "STL5", "BFI3", "PDX6", "HBF2", "512620-82641", "FTW1", "MSP1", "OAK5", "429430-22271", "HOU2", "SAT2", "MCI5", "HOU3", "DFW7", "0-580311", "LAS2", "FTW6", "DEN5", "XIX4", "OKC5", "MSP5", "STL4", "MSP9", "LAX9", "PDX9", "OKC1", "FTW2", "MEM1", "RNO4", "ONT5", "MCI7", "STL8", "PDX5", "SMF1", "OAK4", "0-82958791", "DEN2", "MKC4", "MEM5", "940840-153761", "356270-296101", "TUS1", "0-21063441", "0-92733441", "0-92617131", "0-22895351", "0-57948961", "P_AND_G__637550001_967", "SMF3", "427470-187821", "474310-382201", "0-20065011", "SLC3", "474310-382221", "LGB6", "0-3599711", "0-120661971", "0-70532181", "0-3477081", "434750-1261", "0-165565711", "0-124987841", "KONT", "DAL9", "356880-70811", "0-56700751", "0-70605011", "FAT1", "0-1415561", "FTW9", "0-165263471", "BFI4", "DID2", "ONT8", "LAS5", "OAK3", "DUT1", "KPDX", "SAT5", "JW-BROTX", "PHX7", "AZA5", "SCF-USFC", "AT-SIOSD", "BFI7", "JW-WALWA", "JW-DOUWY", "KAFW", "HOU1", "KSKF", "DMC1", "PHX6", "KPHX", "LAX5", "KRIV", "LGB5", "LGB3", "PHX5", "KSEA", "MTS-KONT", "LGB7", "KSTL", "0-147109971", "HBI1", "ONT2", "SAT1", "2666270-23231", "0-74525631", "LGB8", "DCA2", "SWA1", "SZ24736", "S013427", "DOK2", "DLV1", "JW-BTRLA", "JW-SPRMO", "HTC1", "LAS6", "DIA3", "DAX7", "MERCHANT_50313_885", "WESTROCK_50313_493", "DIA4", "DLB1", "DLR1", "BFI1", "DPD1", "MKC6", "DOM1", "STL7", "STL6", "UPS-REDWA", "UPS-SEAWA", "PHX3", "AT-FARND", "TX_RDC___75028_220", "FTW3", "0-147396191", "0-90138271", "0-153567971", "0-98627431", "XUSD", "JW-HELMT", "DAU2", "KIAH", "KSFO", "DSM1", "DPS3", "DSF6", "DLA4", "SNA4", "DSE7", "DSE4", "DSF4", "ONT6", "JW-SPOWA", "SCF-USTW", "DSE2", "UWA4", "RB_LC_SA_63376_408", "1447590-41671", "0-95073341", "0-142924351", "0-149712751", "XIX7"],
#     "book": 1
# }]



