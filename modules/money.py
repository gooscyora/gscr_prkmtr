import tkinter as tk
import tkinter.font as tkFont
from decimal import *

class Money:
    def __init__(self):
        self.money_sum = Decimal(0)
        self.max_coins = 0

    def addMoney(self, money):
        if round(money, 2) != 10 and round(money, 2) != 20 and round(money, 2) != 50 and self.max_coins < 200:
            self.money_sum = Decimal(round(money, 2) + self.money_sum)
            self.max_coins += 1
        elif round(money, 2) == 10 or round(money, 2) == 20 or round(money, 2) == 50:
            self.money_sum = Decimal(round(money, 2) + self.money_sum)


    def getMoney(self):
        return self.max_coins, Decimal(self.money_sum)





class Dispenser:
    i=0