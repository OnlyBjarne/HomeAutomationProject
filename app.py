from flask import Flask, render_template, jsonify,request,redirect
from yr.libyr import Yr
import yaml
from pubsubConnection import pubsubConnection
from schedules import schedules
import json
import datetime

APP = Flask(__name__)

with open("config.yml", 'r') as ymlfile:
    cfg = yaml.load(ymlfile)

schedule = schedules()

try:
    weather = Yr(location_name='Norge/Sør-Trøndelag/Trondheim/Trondheim')
except RuntimeWarning:
    print("Whoops, something went wrong with fetching your weather!")
    pass

mode = "Solid"
rgb = "rgb(100, 100, 100)"
speed = "10"

@APP.route("/")
def main():
    return render_template('layout.html',views=['currentWeather.html','color.html'],weather=weatherNow())

@APP.route("/color/picker",methods=['GET','POST'])
def colorPicker():
    if request.method == 'POST':
        global mode
        global rgb
        global speed
        mode = request.form.get('mode')
        rgb =  request.form.get('color')
        speed =  request.form.get('speed')
    print(str(mode) + "\n" + str(rgb) + "\n" + str(speed))
    return jsonify(mode=mode,rgb=rgb,speed=speed)

@APP.route("/weather/now",methods=['GET'])
def weatherNow():
    now = weather.now(as_json=False)
    print("getting current weather")
    weatherJson = { "temp":now['temperature']['@value'],
                    "precipitation":now['precipitation']['@value'],
                    "windDir":now['windDirection']['@code'],
                    "windSpeed":now['windSpeed']['@mps'],
                    "symbol":now['symbol']['@var']}
                
    return weatherJson

@APP.route("/weather/forecast",methods=['GET'])
def weatherForcast():
    forecastArray = []
    #date,symbol,temp,precipitation,winddir,windspeed,
    for forecast in weather.forecast():
        time = datetime.datetime.strptime(forecast['@from'],"%Y-%m-%dT%H:%M:%S")
        dayName = ["Man", "Tir", "Ons", "Tor", "Fre", "Lør","Søn"]
        forecastArray.append({
            "time":"{} {:%H:%M}".format(str(dayName[time.weekday()-1]),time),#readable datetime
            "symbol":forecast['symbol']['@var'],
            "temp":forecast['temperature']['@value'],
            "precipitation":forecast['precipitation']['@value'],
            "windDir":forecast['windDirection']['@code'],
            "windSpeed":forecast['windSpeed']['@mps']
        })
        
    return forecastArray

@APP.route("/forecast",methods=['GET'])
def forecast():
    return render_template('layout.html',views=['forecast.html'],forecast=weatherForcast())

@APP.route("/alarm",methods=['GET','POST'])
def alarm():
    if request.method == 'POST':
        schedule.addJob('alarm',"2018-06-25 "+request.form.get('time'),"echo woho")
        return redirect("/alarm")
    else:
        return render_template('layout.html',views=['alarm.html'],schedules=schedule.getSchedules())


if __name__ == "__main__":
    mqtt = pubsubConnection(cfg['MQTT_USER'],cfg['MQTT_PASS'],cfg['MQTT_BROKER'])
    APP.run(host="0.0.0.0", debug=True)
