from flask import Flask, render_template, jsonify, request, redirect
import yaml
from pubsubConnection import pubsubConnection
from schedules import schedules
import json
import datetime
from weather import weather

APP = Flask(__name__)

with open("config.yml", 'r') as ymlfile:
    cfg = yaml.load(ymlfile)

schedule = schedules()
weather = weather()

colorpicker = {"mode": "Solid",
               "rgb": "rgb(100, 100, 100)",
               "speed": "10"}


@APP.route("/")
def main():
    return render_template('layout.html', views=['currentWeather.html', 'color.html'], weather=weather.weatherNow())


@APP.route("/color/picker", methods=['GET', 'POST'])
def colorPicker():
    if request.method == 'POST':
        global mode
        global rgb
        global speed
        mode = request.form.get('mode')
        rgb = request.form.get('color')
        speed = request.form.get('speed')
    print(str(mode) + "\n" + str(rgb) + "\n" + str(speed))
    return jsonify(mode=mode, rgb=rgb, speed=speed)


@APP.route("/forecast", methods=['GET'])
def forecast():
    return render_template('layout.html', views=['forecast.html'], forecast=weather.weatherForcast())


@APP.route("/alarm", methods=['GET', 'POST'])
def alarm():
    if request.method == 'POST':
        schedule.addJob('alarm', "2018-06-25 " +
                        request.form.get('time'), "echo woho")
        return redirect("/alarm")
    else:
        return render_template('layout.html', views=['alarm.html'], schedules=schedule.getSchedules())


if __name__ == "__main__":
    mqtt = pubsubConnection(
        cfg['MQTT_USER'], cfg['MQTT_PASS'], cfg['MQTT_BROKER'])
    APP.run(host="0.0.0.0", debug=True)
