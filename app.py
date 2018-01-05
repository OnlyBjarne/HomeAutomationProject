from flask import Flask, render_template, jsonify,request
from yr.libyr import Yr
import paho.mqtt.client as mqtt

APP = Flask(__name__)

try:
    weather = Yr(location_name='Norge/Sør-Trøndelag/Trondheim/Trondheim')
except Exception as identifier:
    print(identifier)

def on_connect(client, userdata, flags,rc):
    print("connected with result code "+str(rc))

def on_message(client,userdata,msg):
    print(msg.topic+" "+str(msg.payload))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.username_pw_set("username","password")
client.connect_async("mqtt_broker_ip")
client.loop_start()

mode = 'Solid'
rgb = 'rgb(100, 100, 100)'
speed = '10'

@APP.route("/")
def main():
    return render_template('index.html')

@APP.route("/color")
def color():
    return render_template('color.html')


@APP.route("/color/picker",methods=['GET','POST'])
def colorPicker():
    if request.method == 'POST':
        global mode
        global rgb
        global speed
        mode = request.form.get('mode')
        rgb =  request.form.get('rgb')
        speed =  request.form.get('speed')
    print(mode + "\n" + rgb + "\n" + speed)
    return jsonify(mode=mode,rgb=rgb,speed=speed)

@APP.route("/weather/now",methods=['GET'])
def weatherNow():
    now = weather.now()
    #print("getting current weather")
    return jsonify(now)

@APP.route("/weather/forcast",methods=['GET'])
def weatherForcast():
    output = []
    for forecast in weather.forecast():
        output.append(forecast)
    #print("getting forecast weather")
    return jsonify(items=output)


@APP.route("/weather",methods=['GET'])
def forecast():
    return render_template('forecast.html')

client.loop_stop()

if  __name__ == "__main__":
    APP.run(host="0.0.0.0", debug=True)
