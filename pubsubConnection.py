import paho.mqtt.client as mqtt

class pubsubConnection:

    def __init__(self,username,password,broker):
        client = mqtt.Client()
        client.username_pw_set(username,password)
        client.connect_async(broker)
        client.loop_start()

        def on_connect(client, userdata, flags,rc):
            client.subscribe("hello/world")
            print("connected with result code "+str(rc))

        def on_message(client,userdata,msg):
            print(msg.topic+" "+str(msg.payload))
        
        client.on_connect = on_connect
        client.on_message = on_message
        

    def publishMessage(self,message,topic):
        self.client.publish()

    def subscripe(self,topic):
        self.topic