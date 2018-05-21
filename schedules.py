from apscheduler.schedulers.background import BackgroundScheduler
import datetime

class schedules:
    def __init__(self):
        self.scheduler = BackgroundScheduler()

    def addJob(self, name, time,function, type='date'):
        self.scheduler.add_job(str(function),type,time,id=str(name))

    def removeJob(self,id):
        self.scheduler.remove_job(id)

    def getScheduled(self):
        return self.scheduler.print_jobs()