from crontab import CronTab
import paho.mqtt
import datetime


class scheduler:
    

    def __init__(self,username,password):
        self.cron = CronTab(user=True)
        self.username = username
        self.password = password

    def newSchedule(self,name,message,topic,hour,minute):
        self.cron.remove_all(comment=name)
        job = self.cron.new(command="mosquitto_pub -m "+message+" -t "+topic+" -u "+self.username+" -P "+self.password,comment=name)
        scheduleTime = datetime.time(int(hour),int(minute)).strftime("%H:%M")
        hour,minute = scheduleTime.split(":")
        job.hour.on(hour)
        job.minute.on(minute)

        self.cron.write()

        return True

    def getSchedules(self):
        print("getting jobs")
        joblist = []
        for job in self.cron:
            print(job)
            joblist.append(job)
        return joblist

