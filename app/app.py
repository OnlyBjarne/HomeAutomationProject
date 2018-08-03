from flask import Flask, render_template, jsonify, request, redirect
from flask.ext.login import LoginManager, UserMixin, login_required, login_user, logout_user 
import yaml
from pubsubConnection import pubsubConnection
from schedules import schedules
import json
import datetime
from weather import weather

APP = Flask(__name__)

with open("config.yml", 'r') as ymlfile:
    cfg = yaml.load(ymlfile)

try:
    login_manager = LoginManager()
    mqtt = pubsubConnection(cfg['MQTT_USER'], cfg['MQTT_PASS'], cfg['MQTT_BROKER'])
    schedule = schedules()
    yr = weather()
    
    pass
except (RuntimeError,TypeError):
    print("Oops! Something went horribly wrong! Bjarne did something bad!")
    pass


@APP.route("/")
def main():
    return render_template('layout.html', views=cfg['PAGE']['HOME'], weather=yr.weatherNow(),color=colorPicker())


@APP.route("/color/picker", methods=['GET', 'POST'])
def colorPicker():
    color = {"mode": "Solid",
                   "rgb": "rgb(40, 255, 100)",
                   "speed": "10"}
    if request.method == 'POST':
        color['mode'] = request.form.get('mode')
        color['rgb'] = request.form.get('color')
        color['speed'] = request.form.get('speed')
    print(str(color['mode']) + "\n" + str(color['rgb']) + "\n" + str(color['speed']))
    return jsonify(color)

@APP.route("/forecast", methods=['GET'])
def forecast():
    return render_template('layout.html', views=cfg['PAGE']['FORECAST'], forecast=yr.weatherForcast())


@APP.route("/alarm", methods=['GET', 'POST'])
@login_requred
def alarm():
    if request.method == 'POST':
        schedule.addJob('alarm', "2018-06-25" +
                        request.form.get('time'), "echo woho")
        return redirect("/alarm")
    else:
        return render_template('layout.html', views=cfg['PAGE']['ALARM'], schedules=schedule.getSchedules())


if __name__ == "__main__":
    APP.run(host="0.0.0.0", debug=True)
