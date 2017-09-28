import json,urllib2,os,sys

if len(sys.argv) <> 4:  
    print("Invalid number of arguments.")  
    sys.exit()  

key = sys.argv[1]
busline = sys.argv[2]
openfile = open(sys.argv[3],"w")

url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=" + key + "&VehicleMonitoringDetailLevel=calls&LineRef="+busline

response = urllib2.urlopen(url)
d = response.read().decode("utf-8")  

data = json.loads(d)  
data = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
bus_len = len(data)

openfile.write("Latitude,Longitude,Stop Name,Stop Status\n")
for i in range(bus_len):
    lon = data[i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
    lat = data[i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
    if data[i]['MonitoredVehicleJourney']['OnwardCalls'] == []:
        sn = 'N/A'
        ss = 'N/A'
    else:
        sn = data[i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['StopPointName']
        ss = data[i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]\
        ['Extensions']['Distances']['PresentableDistance']
    openfile.write("%f,%f,%s,%s\n"%(lat, lon, sn, ss))
    
openfile.close()

