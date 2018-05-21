import paho.mqtt.client as mqtt

class pubsubConnection:
    
    def __init__(self,username,password,broker):
        self.client = mqtt.Client()
        self.client.username_pw_set(username,password)
        self.client.connect_async(broker)
        self.client.loop_start()

        def on_connect(client, userdata, flags,rc):
            client.subscribe("hello/world")
            print("connected with result code "+str(rc))

        def on_message(client,userdata,msg):
            print(msg.topic+" "+str(msg.payload))
        
        self.client.on_connect = on_connect
        self.client.on_message = on_message
        

    def publishMessage(self,message,topic):
        self.client.publish(str(topic),payload=str(message))

    def subscribe(self,topic):
        self.client.subscribe(str(topic))