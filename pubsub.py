
class pubsub:
    
    def __init__(self,username,password):
        self.username = username
        self.password = password

    def publishMessage(self,message,topic):
        "mosquitto_pub -m " + message + " -t " + topic + " -u " + self.username + " -P " + self.password

    def subscripe(self,topic):
        self.topic