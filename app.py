from flask import Flask, jsonify
from flask.globals import request
import json
import connectSmartDB
import Sessions

app = Flask(__name__)
#app.session_interface = Sessions.RedisSessionInterface()
@app.route("/")

def main():
    if request.method == 'POST':
        print "POST call"
        # json_data = json.loads(request.json)                   
    else:
        print "GET call"
    print "Hello world"
    return "Welcome!!"
    #test=request.form['text']
    #json_input = json.dumps(test)
    #print json_input
    #return render_template('index.html')


@app.route("/smartbins/<city>")
def jsonencodeBinsAtCity(city):
    print "In jsonencodeBinsAtCity"+city
    myList = connectSmartDB.getBinsAtCity(city)
    json_str = json.dumps(myList)
    return json_str

@app.route("/smartbins/<city>/<area>")
def jsonencodeBinsAtCityArea(city,area):
    print "cityArea"+city+area
    myList = connectSmartDB.getBinsAtCityArea(city, area)
    json_str = json.dumps(myList)
    return json_str

@app.route("/smartbins/<city>/<area>/<ward>")
def jsonencodeGetLAC(city,area,ward):
    print format(ward)
    #return " <html><head></head><body><b>Hello.</b> </body> </html>"
#    htmlStr  = "<html><head></head><body><table><tr> <td>latitude</td><td>longitude</td><td>address</td><td>wardName</td><td>areaName</td><td>cityName</td></tr>"
    myList = connectSmartDB.getBinsAtAreaLocationCity(ward,area,city)
    json_str = json.dumps(myList)
    return json_str

@app.route("/smartbins/filllevels/<city>")
def jsonencodeGetFillLevelsCity(city):   
    myList = connectSmartDB.getFilllevelAtCity(city)
    json_str = json.dumps(myList)
    return json_str

@app.route("/smartbins/filllevels/<city>/<area>")
def jsonencodeGetFillLevelsCityArea(city, area):   
    return 0

@app.route("/smartbins/filllevels/<city>/<area>/<ward>")
def jsonencodeGetFillLevelsCityAreaWard(city,area,ward):   
    return 0

@app.route("/smartbins/route/<city>/<area>/<ward>")
def jsonencodeGetRouteCityAreaWard(city,area,ward):   
    return 0

@app.route("/smartbins/route/<city>/<area>")
def jsonencodeGetRouteCityArea(city,area):   
    return 0

@app.route("/smartbins/route/<city>")
def jsonencodeGetRouteCity(city):   
    return 0
#    for bins in range(len(myList)):
#        data['row'] = rows
#        htmlStr = htmlStr+"<tr>"
#        for j in range(len(myList[bins])):
#            htmlStr = htmlStr+"<td>"+str(myList[bins][j])+"</td>"
#        htmlStr = htmlStr+"</tr>"
#        rows = rows+1
#    htmlStr = htmlStr+"</table></body></html>"   
#    return htmlStr
    
  

 
if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8080,debug=True)