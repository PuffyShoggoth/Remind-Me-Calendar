import time
class Parser:
    def parseinput(self, s):
        description = s[s.index('"')+1: s.rindex('"')]
        remind_interval = 0
        next_remind = "" 
        for i in range (0, len(s)):
            #if s[i] == '"':
            #    for j in range (i+1, len(s)):
            #        if s[j] == '"':
            #            breaks
            #        else:
            #            description = description + s[j]
            if s[i-6:i] == "every ":
                for k in range (0,3):
                    if s[i+k] == "h":
                        remind_interval = float(s[i:i+k-1])*60**2
                    elif s[i+k:i+k+3] == "min":
                        remind_interval = float(s[i:i+k-1])*60
                    elif s[i+k:i+k+5] == "weeks":
                        remind_interval = float(s[i:i+k-1])*7*24*60**2
                    elif s[i+k:i+k+4] == "days":
                        remind_interval = float(s[i:i+k-1])*24*60**2
                    elif s[i+k:i+k+5] == "years":
                        remind_interval = float(s[i:i+k-1])*365*24*60**2
            if s[i-3:i] == "on ":
                remind_interval = time.mktime(time.strptime(s[i:i+24]))
            if s[i:i+13] == " hours before":
                next_remind = completion_date-(float(s[i-2:i]))*60**2
            if s[i:i+5] == "until":
                next_remind = remind_interval
        completion_date = time.mktime(time.strptime(s[len(s)-24:len(s)]))
        return [description, remind_interval, next_remind, completion_date]
