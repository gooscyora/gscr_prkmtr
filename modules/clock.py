from datetime import datetime
from time import *
from modules import money
from decimal import *

class Timer():

    def getTime(self):
        return datetime.utcfromtimestamp(Decimal(time())).strftime('%Y-%m-%d %H:%M')

class Time():
    def __init__(self):
        self.initial_time = Decimal(time())
        self.calculatedTime = Decimal(0)
    def addTime(self,time_value):
        print("poczatkowa:", self.initial_time)
        self.initial_time = self.initial_time+Decimal(time_value)
        print("po dodaniu:", self.initial_time)
    def getTime(self):
        return datetime.utcfromtimestamp(self.initial_time).strftime('%Y-%m-%d %H:%M'), self.initial_time
    def calculateFinishTime(self,money):
        if money <= 200:
            self.calculatedTime=Decimal(money)*Decimal(18)
        elif 200 < money <= 400:
            money=money-2
            self.calculatedTime = 3600+Decimal(money)*Decimal(9)
        elif    money > 400:
            print(money)
            money=money-6*100
            print(money)
            self.calculatedTime = 7200+Decimal(money)*Decimal(7.2)

           # print(self.initial_time)
           # print(self.calculatedTime)
        print(datetime.utcfromtimestamp(self.initial_time+self.calculatedTime).strftime('%Y-%m-%d %H:%M'))




