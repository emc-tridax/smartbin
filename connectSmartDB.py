import MySQLdb


def connectBinDb():
    hostname = "127.0.0.1"
    username = "root"
    password = ""
    dbName = "smartbin_db1"
    
    db = MySQLdb.connect(hostname,username,password, dbName)
    
    return db

def closeBinDb(db):
    db.close()

def getLatLongHighFilllevelAtCityArea(city,area):
    binList = {}
    
    db = connectBinDb()
    
    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    
    # Execute the query
    sqlQuery = "select s.Longitude,s.Latitude from smartbin s inner Join wards p on p.WardId = s.WardId inner Join area a on a.areaId = p.AreaId inner join city c on c.cityId = a.CityId inner join smartbinfilllevel f  on f.BinId = s.BinId where c.Name = '"+city+"' AND f.filllevel > 20 "
     
    try:
        cursor.execute(sqlQuery);
        results = cursor.fetchall();

    except:
        print "Error: Unable to fetch data"
    
    i=0
    for row in results:
        longitude = row[0]
        latitude = row[1]
        binList[i] = {"Latitude": latitude, "Longitude": longitude}
        i = i + 1
      
    print binList
    # disconnect from server
    closeBinDb(db)
    
    return binList

def getHighFilllevelAtCityArea(city,area):
    binList = []
    
    db = connectBinDb()
    
    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    
    # Execute the query
    sqlQuery = "select s.Longitude,s.Latitude,s.Address,p.WardName,a.AreaName,c.Name,f.fillLevel from smartbin s inner Join wards p on p.WardId = s.WardId inner Join area a on a.areaId = p.AreaId inner join city c on c.cityId = a.CityId inner join smartbinfilllevel f  on f.BinId = s.BinId where c.Name = '"+city+"' AND f.filllevel > 20 "
     
    try:
        cursor.execute(sqlQuery);
        results = cursor.fetchall();
        for row in results:
            longitude = row[0]
            latitude = row[1]
            address = row[2]
            wardName = row[3]
            areaName = row[4]
            cityName = row[5]
            filllevel = row[6]
            print latitude,longitude,address,filllevel,wardName,areaName,cityName
            binList.append([latitude,longitude,address,filllevel,wardName,areaName,cityName])
            
    except:
        print "Error: Unable to fetch data"
    
    # disconnect from server
    closeBinDb(db)
    
    return binList
def getFilllevelAtCity(city):
    binList = []
    
    db = connectBinDb()
    
    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    
    # Execute the query
    sqlQuery = "select s.Longitude,s.Latitude,s.Address,p.WardName,a.AreaName,c.Name,f.fillLevel from smartbin s inner Join wards p on p.WardId = s.WardId inner Join area a on a.areaId = p.AreaId inner join city c on c.cityId = a.CityId inner join smartbinfilllevel f  on f.BinId = s.BinId where c.Name = '"+city+"'"
     
    try:
        cursor.execute(sqlQuery);
        results = cursor.fetchall();
        for row in results:
            longitude = row[0]
            latitude = row[1]
            address = row[2]
            wardName = row[3]
            areaName = row[4]
            cityName = row[5]
            filllevel = row[6]
            print latitude,longitude,address,filllevel,wardName,areaName,cityName
            binList.append([latitude,longitude,address,filllevel,wardName,areaName,cityName])
            
    except:
        print "Error: Unable to fetch data"
    
    # disconnect from server
    closeBinDb(db)
    
    return binList

def getFilllevelAtCityArea(city,area):
    binList = []
    
    db = connectBinDb()
    
    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    
    # Execute the query
    sqlQuery = "select s.Longitude,s.Latitude,s.Address,p.WardName,a.AreaName,c.Name,f.fillLevel from smartbin s inner Join wards p on p.WardId = s.WardId inner Join area a on a.areaId = p.AreaId inner join city c on c.cityId = a.CityId inner join smartbinfilllevel f  on f.BinId = s.BinId where c.Name = '"+city+"' AND a.AreaName = '"+area+"'"
     
    try:
        cursor.execute(sqlQuery);
        results = cursor.fetchall();
        for row in results:
            longitude = row[0]
            latitude = row[1]
            address = row[2]
            wardName = row[3]
            areaName = row[4]
            cityName = row[5]
            filllevel = row[6]
            print latitude,longitude,address,filllevel,wardName,areaName,cityName
            binList.append([latitude,longitude,address,filllevel,wardName,areaName,cityName])
            
    except:
        print "Error: Unable to fetch data"
    
    # disconnect from server
    closeBinDb(db)
    
    return binList

def getBinsAtCityArea(city,area):
    binList = []
    
    db = connectBinDb()
    
    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    
    # Execute the query
    sqlQuery = "select s.Longitude,s.Latitude,s.Address,p.WardName,a.AreaName,c.Name from smartbin s inner Join wards p on p.WardId = s.WardId inner Join area a on a.areaId = p.AreaId inner join city c on c.cityId = a.CityId where a.AreaName = '"+area+"' AND c.Name = '"+city+"'"
     
    try:
        cursor.execute(sqlQuery);
        results = cursor.fetchall();
        for row in results:
            longitude = row[0]
            latitude = row[1]
            address = row[2]
            wardName = row[3]
            areaName = row[4]
            cityName = row[5]
            print latitude,longitude,address,wardName,areaName,cityName
            binList.append([latitude,longitude,address,wardName,areaName,cityName])
            
    except:
        print "Error: Unable to fetch data"
    
    # disconnect from server
    closeBinDb(db)
    
    return binList
    
def getBinsAtCity(city):
    binList = []
    
    db = connectBinDb()
    
    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    
    # Execute the query
    sqlQuery = "select s.Longitude,s.Latitude,s.Address,p.WardName,a.AreaName,c.Name from smartbin s inner Join wards p on p.WardId = s.WardId inner Join area a on a.areaId = p.AreaId inner join city c on c.cityId = a.CityId where c.Name = '"+city+"'"
     
    try:
        cursor.execute(sqlQuery);
        results = cursor.fetchall();
        for row in results:
            longitude = row[0]
            latitude = row[1]
            address = row[2]
            wardName = row[3]
            areaName = row[4]
            cityName = row[5]
            print latitude,longitude,address,wardName,areaName,cityName
            binList.append([latitude,longitude,address,wardName,areaName,cityName])
            
    except:
        print "Error: Unable to fetch data"
    
    # disconnect from server
    closeBinDb(db)
    
    return binList

def getBinsAtArea(area):
    binList = []
    
    db = connectBinDb()
    
    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    
    # Execute the query
    sqlQuery = "select s.Longitude,s.Latitude,s.Address,p.WardName,a.AreaName from smartbin s inner Join wards p on p.WardId = s.WardId inner Join area a on a.areaId = p.AreaId where a.AreaName = '"+area+"'"
     
    try:
        cursor.execute(sqlQuery);
        results = cursor.fetchall();
        for row in results:
            longitude = row[0]
            latitude = row[1]
            address = row[2]
            wardName = row[3]
            areaName = row[4]
            print latitude,longitude,address,wardName,areaName
            binList.append([latitude,longitude,address,wardName,areaName])
            
    except:
        print "Error: Unable to fetch data"
    
    # disconnect from server
    closeBinDb(db)
    
    return binList

def getBinsAtWard(ward):
    binList = []
    
    db = connectBinDb()
    
    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    
    # Execute the query
    sqlQuery = "select s.Longitude,s.Latitude,s.Address,p.WardName from smartbin s inner Join wards p on p.WardId = s.WardId where p.WardName = '"+ward+"'"
    
    try:
        cursor.execute(sqlQuery);
        results = cursor.fetchall();
        for row in results:
            longitude = row[0]
            latitude = row[1]
            address = row[2]
            wardName = row[3]
            print latitude,longitude,address,wardName
            binList.append([latitude,longitude,address,wardName])
            
    except:
        print "Error: Unable to fetch data"
    
    # disconnect from server
    closeBinDb(db)
    
    return binList
    
def getBinsAtAreaLocationCity(ward, area, city):
    binList = []
    
    db = connectBinDb()
    
    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    
    # Execute the query
    sqlQuery = "select s.Longitude,s.Latitude,s.Address,p.WardName, a.AreaName,c.Name from smartbin s inner Join wards p on p.WardId = s.WardId inner Join area a on a.areaId = p.AreaId inner Join city c on c.CityId = a.cityId where c.Name = '"+city+"' AND p.WardName = '"+ward+"' AND a.AreaName = '"+area+"'"

    try:
        cursor.execute(sqlQuery);
        results = cursor.fetchall();
        for row in results:
            longitude = row[0]
            latitude = row[1]
            address = row[2]
            wardName = row[3]
            areaName = row[4]
            cityName = row[5]
            print latitude,longitude,address,wardName,areaName,cityName
            binList.append([latitude,longitude,address,wardName,areaName,cityName])
            
    except:
        print "Error: Unable to fetch data"
    
    # disconnect from server
    closeBinDb(db)
    
    return binList

def createState (db, state):
    cursor = db.cursor()
    sqlQuery = "SELECT stateId from state where state LIKE '"+state+"'"
    cursor.execute(sqlQuery)
    results = cursor.fetchall()
    
    if(len(results) == 0):
        sqlQuery = "INSERT INTO `smartbin_db1`.`state` (`stateId`, `state`) VALUES (NULL, '"+state+"')"
        cursor.execute(sqlQuery);
        db.commit()
        
def createCity(db, state, city):
    cursor = db.cursor()
    sqlQuery = "SELECT c.CityId from city c inner join state s on s.stateId = c.stateId where c.Name LIKE '"+city+"' AND s.state LIKE '"+state+"'"
    cursor.execute(sqlQuery)
    results = cursor.fetchall()
    
    if(len(results) == 0):
        cursor.execute("INSERT INTO city (`CityId`, `Name`, `stateId`)  SELECT NULL, '%s', state.stateId from state where state.`state`='%s'",city.state)
        db.commit()
           
def insertSmartBin(state, city, area, ward, latitude, longitude, address):
    db = connectBinDb()
    
    # prepare a cursor object using cursor() method
    cursor = db.cursor()
          
    sqlQuery = "SELECT w.WardId from wards w inner Join area a on a.AreaId = w.AreaId inner Join city c on c.cityId = a.CityId inner Join state s on s.stateId = c.stateId where w.WardName = '"+ward+"' AND a.AreaName = '"+area+"' AND c.Name = '"+city+"' AND s.state = '"+state+"'"
               
    cursor.execute(sqlQuery)
    results = cursor.fetchone()
    
    print results[0]
    
    if (len(results) > 0):
        cursor.execute("INSERT into `smartbin_db1`.`smartbin` (`BinId`, `WardId`, `Longitude`, `Latitude`, `Address`) VALUES (NULL, %s, %s, %s, %s)",(results[0],longitude,latitude,address))
        db.commit(); 
    
    elif (len(results) == 0):
            createState(db, state)
            createCity(db, state, city)
       #     createArea(db, state, city, area)
       #     createWard(db, state, city, area, ward)
       #     createBin(db, state, city, area, ward, latitude, longitude, address)
               
    closeBinDb(db)
        
#myList = getBinsAtAreaLocationCity("Hongasandra", "Bommanahalli", "Bangalore")
#myList = getFilllevelAtCity("Bangalore")
#for bins in range(len(myList)):
#    for j in range(len(myList[bins])):
#        print myList[bins][j]

#myList = getBinsAtWard("Hongasandra")
#for bins in range(len(myList)):
#    for j in range(len(myList[bins])):
#        print myList[bins][j]
       
#insertSmartBin("Karnataka", "Bangalore", "Bommanahalli", "Bommanahalli", 1.12345, 2.123455, "testAddress") 
       
#myList = getBinsAtCityArea("Bangalore","Hongasandra")
#for bins in range(len(myList)):
#    for j in range(len(myList[bins])):
#        print myList[bins][j]
        
getLatLongHighFilllevelAtCityArea("Bengaluru","Bommanahalli")