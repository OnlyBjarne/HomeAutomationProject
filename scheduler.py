from crontab import CronTab
import datetime
import sched, time

 TODO: Fix scheduler using python sched istead of crontab for cross platform support

"""class scheduler:
    def __init__(self):
        self.cron = CronTab(user=True)

    def newSchedule(self,name,command,hour,minute):
        self.cron.remove_all(comment=name)
        job = self.cron.new(command=command,comment=name)
        scheduleTime = datetime.time(int(hour),int(minute)).strftime("%H:%M")
        hour,minute = scheduleTime.split(":")
        job.hour.on(hour)
        job.minute.on(minute)
        self.cron.write()
        return True

  def getSchedules(self):
       
        return joblist

"""
