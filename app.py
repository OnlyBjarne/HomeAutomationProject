from flask import Flask, render_template, jsonify,request
from yr.libyr import Yr
import yaml
from pubsubConnection import pubsubConnection
#from scheduler import scheduler

APP = Flask(__name__)

with open("config.yml", 'r') as ymlfile:
    cfg = yaml.load(ymlfile)

try:
    weather = Yr(location_name='Norge/Sør-Trøndelag/Trondheim/Trondheim')
except e:
    print("Whoops, something went wrong with fetching your weather! :/ " + e)

mode = "Solid"
rgb = "rgb(100, 100, 100)"
speed = "10"

@APP.route("/")
def main():
    return render_template('layout.html',views=['currentWeather.html','color.html'])

@APP.route("/color")
def color():
    return render_template('layout.html',views=['color.html'])


@APP.route("/color/picker",methods=['GET','POST'])
def colorPicker():
    if request.method == 'POST':
        global mode
        global color
        global speed
        mode = request.form.get('mode')
        rgb =  request.form.get('color')
        speed =  request.form.get('speed')
    print(str(mode) + "\n" + str(rgb) + "\n" + str(speed))
    return jsonify(mode=mode,rgb=rgb,speed=speed)

@APP.route("/weather/now",methods=['GET'])
def weatherNow():
    now = weather.now()
    #print("getting current weather")
    return jsonify(now)

@APP.route("/weather/forecast",methods=['GET'])
def weatherForcast():
    output = []
    for forecast in weather.forecast():
        output.append(forecast)
    #print("getting forecast weather")
    return jsonify(items=output)


@APP.route("/forecast",methods=['GET'])
def forecast():
    return render_template('layout.html',views=['forecast.html'])

@APP.route("/alarm",methods=['GET','POST'])
def alarm():
    return render_template('alarm.html',schedules=schedule.getSchedules())

if  __name__ == "__main__":

    mqtt = pubsubConnection(cfg['MQTT_USER'],cfg['MQTT_PASS'],cfg['MQTT_BROKER'])
    APP.run(host="0.0.0.0", debug=True)
