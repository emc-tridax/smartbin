import simplejson, urllib
import connectSmartDB
from googlemaps import convert
from geopy.distance import vincenty

GEOCODE_BASE_URL = 'https://maps.googleapis.com/maps/api/geocode/json'
DIRECTION_BASE_URL = "https://maps.googleapis.com/maps/api/directions/json"

def geocode(latitude,longitude):
    location = str(latitude)+","+str(longitude)
    geo_args = {'latlng' : location}

    url = GEOCODE_BASE_URL + '?' + urllib.urlencode(geo_args)
    print url
    result = simplejson.load(urllib.urlopen(url))
#    print simplejson.dumps(result, indent=2)
    
    i=0
    area=""
    city=""
    for s in result['results']:
        if s['address_components'][i]['types'][0] == 'sublocality_level_1':
            area = simplejson.dumps(s['address_components'][i]['long_name'], indent=2)
            print area
            continue
        
        if s['address_components'][i]['types'][0] == 'locality':
            city = simplejson.dumps(s['address_components'][i]['long_name'], indent=2)
            print city
            
        if len(area) > 0 & len(city) > 0:
            break
        
    return city,area

def getDestination(latitude, longitude, myList):
    destLatitude=0
    destLongitude=0
    distance=0.0000
    origin=(latitude,longitude)
    element=-1
    
#   myList = connectSmartDB.getLatLongHighFilllevelAtCityArea("Bengaluru", "Bommanahalli")
    
    for i in range(len(myList)):
        tempDest = (myList[i]['Latitude'],myList[i]['Longitude'])
        tempDistance = vincenty(origin, tempDest).miles
        #print tempDistance
        if distance == 0 or tempDistance > distance:
            #print "1."+str(distance)
            distance = tempDistance
            destLatitude,destLongitude = tempDest
            element = i
            #print "2."+str(distance)+str(tempDest)
    if element != -1:
        myList.pop(element) 
    
    print myList
        
    print destLatitude,destLongitude
    return destLatitude,destLongitude
    
def getRoute(latitude,longitude):
    city=""
    area=""
    city,area=geocode(latitude,longitude)
    print city,area
    
    city.rstrip()
    area.rstrip()
    city.lstrip()
    area.lstrip()
    
    geo_args={}

    myList = connectSmartDB.getLatLongHighFilllevelAtCityArea("Bengaluru","bommanahalli")
    print myList
    
    destLat,destLong = getDestination(latitude, longitude, myList)
    destination = str(destLat)+","+str(destLong)
    waypoints = getWayPoints(myList)
  #  waypoints = convert.components(myList)
    location = str(latitude)+","+str(longitude)
    geo_args = {'origin':location, 'waypoints':waypoints, 'destination':destination} 
    
    print waypoints
        
    url = DIRECTION_BASE_URL + '?' + urllib.urlencode(geo_args)
    print url
    result = simplejson.load(urllib.urlopen(url))
    print simplejson.dumps(result, indent=2)
    return result

def getWayPoints(myList):
    waypoints=""
    for i in myList:
         waypoints = waypoints+str(myList[i]['Latitude'])+","+str(myList[i]['Longitude'])+"|"  
         
    print waypoints
    return waypoints

if __name__ == '__main__':
    latitude,longitude=12.910673,77.623541

    getRoute(latitude,longitude)
    
    """
    city,area=geocode(location)
    #city,area = geocode()
    #myList = connectSmartDB.getHighFilllevelAtCityArea(city, area)
    geo_args={}
    myList = connectSmartDB.getLatLongHighFilllevelAtCityArea("Bengaluru", "Bommanahalli")
    destLat,destLong = getDestination(latitude, longitude, myList)
    destination = (destLat,destLong)
    
    waypoints = getWayPoints(myList)
  #  waypoints = convert.components(myList)
    
    geo_args = {'origin':location, 'waypoints':waypoints, 'destination':destination} 
    
    print waypoints
        
    url = DIRECTION_BASE_URL + '?' + urllib.urlencode(geo_args)
    print url
    result = simplejson.load(urllib.urlopen(url))
    print simplejson.dumps(result, indent=2)
    """
    #geocode(address="Laa+Heritage+Apartments")
    
