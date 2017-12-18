from flask import Flask, render_template
import paho.mqtt.client as mqtt
APP = Flask(__name__)

def on_connect(client, userdata, flags,rc):
    print("connected with result code "+str(rc))

def on_message(client,userdata,msg):
    print(msg.topic+" "+str(msg.payload))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.username_pw_set("OnlyBjarne","Pingvin1")
client.connect_async("wilbur.local")
client.loop_start()

@APP.route("/")
def main():
    text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam et arcu a quam interdum luctus sed vitae nisi. Nunc id pretium ex. Vivamus congue gravida metus ut iaculis. Fusce pharetra dolor sed odio blandit porta. Maecenas vitae blandit tellus. Integer nisi erat, hendrerit sed lacinia sit amet, luctus id sapien. Donec nec mi a nulla finibus volutpat rhoncus at elit."
    return render_template('index.html')

@APP.route("/cards")
def cards():
    text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam et arcu a quam interdum luctus sed vitae nisi. Nunc id pretium ex. Vivamus congue gravida metus ut iaculis. Fusce pharetra dolor sed odio blandit porta. Maecenas vitae blandit tellus. Integer nisi erat, hendrerit sed lacinia sit amet, luctus id sapien. Donec nec mi a nulla finibus volutpat rhoncus at elit."
    return render_template('cards.html')

@APP.route("/light/mode/<string:mode>",methods=['POST'])
def lamp(mode):
    json = "{\"mode\" : \"" + mode + "\"}"
    client.publish("soverom/Alarm",payload=json)
    print("done")
    return json
@APP.route("/light/color/<int:r>+<int:g>+<int:b>",methods=['POST'])
def color(r,g,b):
    json = "{\"mode\":\"solid\",\"color\":["+r+","+g+","+b+"]}"
    return json

@APP.route("/thermostat/<int:day>/<int:night>",methods=['POST'])
def termostat(day,night):
    return


client.loop_stop()

if  __name__ == "__main__":
    APP.run(host="0.0.0.0", debug=True)
