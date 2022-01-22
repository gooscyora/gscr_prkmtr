import seconds as seconds
from dateutil.rrule import *
from datetime import datetime
from time import *
from decimal import *
from datetime import timedelta

class Timer():

    def getTime(self):
        return datetime.utcfromtimestamp(Decimal(time())+3600).strftime('%Y-%m-%d %H:%M')

class Time():
    def __init__(self):

        self.initial_time = Decimal(time())+3600 #adding 1h so itc local time
        self.calculatedTime = Decimal(0)

    def addTime(self,time_value):
        self.initial_time = self.initial_time+Decimal(time_value)

    def getTime(self):
        return datetime.utcfromtimestamp(self.initial_time).strftime('%Y-%m-%d %H:%M'), self.initial_time

    def calculateFinishTime(self,money):
        if money <= 200:
            self.calculatedTime = Decimal(money)*Decimal(18)
        elif 200 < money <= 600:
            money = money-2*100
            self.calculatedTime = 3600+Decimal(money)*Decimal(9)
        elif money > 600:
            money=money-6*100
            self.calculatedTime = 7200+Decimal(money)*Decimal(7.2)

        return self.departureTime()+timedelta(seconds=int(self.calculatedTime))

    def departureTime(self):
        departure = datetime.utcfromtimestamp(self.initial_time)
        rr = rrule(SECONDLY, byweekday=(MO, TU, WE, TH, FR), byhour=(8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19), dtstart=departure, interval=1)
        return rr.after(departure)