import sys,json,os

try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib

url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=" + sys.argv[1] + \
    "&VehicleMonitoringDetailLevel=calls&LineRef=" + sys.argv[2]


response = urllib.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)

if len(sys.argv) <> 3:
    print ("Invalid number of arguments.")
    sys.exit()

num=data["Siri"]["ServiceDelivery"]["VehicleMonitoringDelivery"][0]["VehicleActivity"]

longitude = data["Siri"]["ServiceDelivery"]["VehicleMonitoringDelivery"][0]["VehicleActivity"][0]["MonitoredVehicleJourney"]["VehicleLocation"]["Longitude"]
latitude = data["Siri"]["ServiceDelivery"]["VehicleMonitoringDelivery"][0]["VehicleActivity"][0]["MonitoredVehicleJourney"]["VehicleLocation"]["Latitude"]

print ("Bus Line:",sys.argv[2])
print ("Number of Active Buses:", len(data["Siri"]["ServiceDelivery"]["VehicleMonitoringDelivery"][0]["VehicleActivity"]))
for i in range(len(num)):
    print ("Bus"+ str(i) +"is at longitude:" + str(longitude) + "and latitude:" + str(latitude))