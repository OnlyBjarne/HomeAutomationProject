from crontab import CronTab
import paho.mqtt 


class scheduler:
    cron = CronTab(user=True)

    def __init__(self,username,password):
        self.username = username
        self.password = password

    def newScedule(self,name,message,topic,time):
        job = self.cron.new(command="mosquitto_pub -m "+message+" -t "+topic+" -u "+self.username+" -P "+self.password,comment=name)
        