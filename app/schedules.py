from crontab import CronTab
from datetime import datetime as datetime

class schedules:
    scheduler = CronTab(user=True)

    def addJob(self, name, time, function):
        job = self.scheduler.new(command=str(function),comment=str(name))
        job.setall(datetime.strptime(time,"%Y-%m-%d %H:%M"))
        if job.is_valid:
            print("job added!")
            job.enable()
        else:
            print("Oops, something went wrong with adding this job! :(")
            job.enable(False)

    def removeJob(self,comment):
        self.scheduler.remove_all(comment=comment)

    def removeAll(self):
        self.scheduler.remove_all()

    def getSchedules(self):
        joblist = []
        for job in self.scheduler:
            joblist.append(job)
        return joblist