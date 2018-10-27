from threading import Thread
import time
class Task:
    def __init__(self, remind_interval, completion_date, next_remind, description):
        self.remind_interval = remind_interval
        self.completion_date = completion_date
        self.next_remind = next_remind
        self.description = description

    def next_alert(self):
        ct = time.time()
        if ct<=self.next_remind:
            return self.next_remind - ct
        else:
            if self.completion_date-self.remind_interval < ct:
                return 0
            else:
                return (self.completion_date - ct)%self.remind_interval

    def show_reminders(self):
        if time.time()>=self.completion_date:
            print("event finished")
            return
        elif self.remind_interval <=0:
            print("invalid interval")
            return
        else:
            print(self.description)
            self.next_remind += self.remind_interval
            time.sleep(self.remind_interval)
            self.show_reminders()
            return
        
    def start_reminder(self):
        time.sleep(self.next_alert())
        self.show_reminders()
        return
        
    def start_alerts(self):
        thread = Thread(target = self.start_reminder)
        thread.start()
        return
