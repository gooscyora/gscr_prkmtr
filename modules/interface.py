import tkinter as tk
import tkinter.font as tkFont
from modules import money
from modules import time
from decimal import *

class Window:
    def createWindow(self, root):
        root.title("Parkomat")
        width=800
        height=700
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        self.moneys = money.Money()
        #self.clock = time.Time()

        label_podaj_nr=tk.Label(root)
        ft = tkFont.Font(family='Times',size=13)
        label_podaj_nr["font"] = ft
        label_podaj_nr["fg"] = "#333333"
        label_podaj_nr["justify"] = "center"
        label_podaj_nr["text"] = "Podaj numer rejestracyjny:"
        label_podaj_nr.place(x=50,y=20,width=197,height=30)

        labe_aktualny_czas=tk.Label(root)
        ft = tkFont.Font(family='Times',size=13)
        labe_aktualny_czas["font"] = ft
        labe_aktualny_czas["fg"] = "#333333"
        labe_aktualny_czas["justify"] = "center"
        labe_aktualny_czas["text"] = "Aktualny czas: "
        labe_aktualny_czas.place(x=140,y=60,width=100,height=30)

        pokaz_aktualny_czas=tk.Label(root)
        pokaz_aktualny_czas["bg"] = "#ffffff"
        ft = tkFont.Font(family='Times',size=13)
        pokaz_aktualny_czas["font"] = ft
        pokaz_aktualny_czas["fg"] = "#333333"
        pokaz_aktualny_czas["justify"] = "center"
        pokaz_aktualny_czas["text"] = "AKTUALNY_CZAS"
        pokaz_aktualny_czas.place(x=310,y=60,width=400,height=30)

        label_podaj_czas=tk.Label(root)
        ft = tkFont.Font(family='Times',size=13)
        label_podaj_czas["font"] = ft
        label_podaj_czas["fg"] = "#333333"
        label_podaj_czas["justify"] = "center"
        label_podaj_czas["text"] = "Podaj czas rozpoczęcia parkowania:"
        label_podaj_czas.place(x=0,y=100,width=260,height=33)

        b5gr=tk.Button(root)
        b5gr["bg"] = "#bcdfee"
        ft = tkFont.Font(family='Times',size=10)
        b5gr["font"] = ft
        b5gr["fg"] = "#000000"
        b5gr["justify"] = "center"
        b5gr["text"] = "5gr"
        b5gr.place(x=210,y=290,width=30,height=25)
        b5gr["command"] = self.b5gr_command

        b10gr=tk.Button(root)
        b10gr["bg"] = "#bcdfee"
        ft = tkFont.Font(family='Times',size=10)
        b10gr["font"] = ft
        b10gr["fg"] = "#000000"
        b10gr["justify"] = "center"
        b10gr["text"] = "10gr"
        b10gr.place(x=250,y=290,width=40,height=25)
        b10gr["command"] = self.b10gr_command

        b20gr=tk.Button(root)
        b20gr["bg"] = "#bcdfee"
        ft = tkFont.Font(family='Times',size=10)
        b20gr["font"] = ft
        b20gr["fg"] = "#000000"
        b20gr["justify"] = "center"
        b20gr["text"] = "20gr"
        b20gr.place(x=300,y=290,width=40,height=25)
        b20gr["command"] = self.b20gr_command

        b50gr=tk.Button(root)
        b50gr["bg"] = "#bcdfee"
        ft = tkFont.Font(family='Times',size=10)
        b50gr["font"] = ft
        b50gr["fg"] = "#000000"
        b50gr["justify"] = "center"
        b50gr["text"] = "50gr"
        b50gr.place(x=350,y=290,width=40,height=25)
        b50gr["command"] = self.b50gr_command

        b2zl=tk.Button(root)
        b2zl["bg"] = "#bcdfee"
        ft = tkFont.Font(family='Times',size=10)
        b2zl["font"] = ft
        b2zl["fg"] = "#000000"
        b2zl["justify"] = "center"
        b2zl["text"] = "2zl"
        b2zl.place(x=450,y=290,width=30,height=25)
        b2zl["command"] = self.b2zl_command

        b1zl=tk.Button(root)
        b1zl["bg"] = "#bcdfee"
        ft = tkFont.Font(family='Times',size=10)
        b1zl["font"] = ft
        b1zl["fg"] = "#000000"
        b1zl["justify"] = "center"
        b1zl["text"] = "1zl"
        b1zl.place(x=410,y=290,width=30,height=25)
        b1zl["command"] = self.b1zl_command

        wprowadz_nr_rej=tk.Entry(root)
        wprowadz_nr_rej["bg"] = "#ffffff"
        wprowadz_nr_rej["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=13)
        wprowadz_nr_rej["font"] = ft
        wprowadz_nr_rej["fg"] = "#333333"
        wprowadz_nr_rej["justify"] = "center"
        wprowadz_nr_rej["text"] = "wprowadz_nr_rej"
        wprowadz_nr_rej.place(x=310,y=20,width=400,height=30)

        bZatwierdz=tk.Button(root)
        bZatwierdz["bg"] = "#13f122"
        ft = tkFont.Font(family='Times',size=18)
        bZatwierdz["font"] = ft
        bZatwierdz["fg"] = "#000000"
        bZatwierdz["justify"] = "center"
        bZatwierdz["text"] = "Zatwierdź"
        bZatwierdz.place(x=320,y=370,width=160,height=40)
        bZatwierdz["command"] = self.bZatwierdz_command

        label_dodaj_kwote=tk.Label(root)
        ft = tkFont.Font(family='Times',size=13)
        label_dodaj_kwote["font"] = ft
        label_dodaj_kwote["fg"] = "#333333"
        label_dodaj_kwote["justify"] = "center"
        label_dodaj_kwote["text"] = "Dodaj kwote:"
        label_dodaj_kwote.place(x=200,y=250,width=400,height=25)

        okno_terminal=tk.Label(root)
        okno_terminal["bg"] = "#ffffff"
        ft = tkFont.Font(family='Times',size=10)
        okno_terminal["font"] = ft
        okno_terminal["fg"] = "#333333"
        okno_terminal["justify"] = "center"
        okno_terminal["text"] = "_terminal"
        okno_terminal.place(x=20,y=420,width=760,height=260)

        b2gr=tk.Button(root)
        b2gr["bg"] = "#bcdfee"
        ft = tkFont.Font(family='Times',size=10)
        b2gr["font"] = ft
        b2gr["fg"] = "#000000"
        b2gr["justify"] = "center"
        b2gr["text"] = "2gr"
        b2gr.place(x=170,y=290,width=30,height=25)
        b2gr["command"] = self.b2gr_command

        b1gr=tk.Button(root)
        b1gr["bg"] = "#bcdfee"
        ft = tkFont.Font(family='Times',size=10)
        b1gr["font"] = ft
        b1gr["fg"] = "#000000"
        b1gr["justify"] = "center"
        b1gr["text"] = "1gr"
        b1gr.place(x=130,y=290,width=30,height=25)
        b1gr["command"] = self.b1gr_command

        b5zl=tk.Button(root)
        b5zl["bg"] = "#bcdfee"
        ft = tkFont.Font(family='Times',size=10)
        b5zl["font"] = ft
        b5zl["fg"] = "#000000"
        b5zl["justify"] = "center"
        b5zl["text"] = "5zl"
        b5zl.place(x=490,y=290,width=30,height=25)
        b5zl["command"] = self.b5zl_command

        b10zl=tk.Button(root)
        b10zl["bg"] = "#bcdfee"
        ft = tkFont.Font(family='Times',size=10)
        b10zl["font"] = ft
        b10zl["fg"] = "#000000"
        b10zl["justify"] = "center"
        b10zl["text"] = "10zl"
        b10zl.place(x=540,y=290,width=40,height=25)
        b10zl["command"] = self.b10zl_command

        b20zl=tk.Button(root)
        b20zl["bg"] = "#bcdfee"
        ft = tkFont.Font(family='Times',size=10)
        b20zl["font"] = ft
        b20zl["fg"] = "#000000"
        b20zl["justify"] = "center"
        b20zl["text"] = "20zl"
        b20zl.place(x=590,y=290,width=40,height=25)
        b20zl["command"] = self.b20zl_command

        b50zl=tk.Button(root)
        b50zl["bg"] = "#bcdfee"
        ft = tkFont.Font(family='Times',size=10)
        b50zl["font"] = ft
        b50zl["fg"] = "#000000"
        b50zl["justify"] = "center"
        b50zl["text"] = "50zl"
        b50zl.place(x=640,y=290,width=40,height=25)
        b50zl["command"] = self.b50zl_command

        self.pokaz_kwote=tk.Label(root)
        self.pokaz_kwote["bg"] = "#ffffff"
        self.ft = tkFont.Font(family='Times',size=13)
        self.pokaz_kwote["font"] = ft
        self.pokaz_kwote["fg"] = "#333333"
        self.pokaz_kwote["justify"] = "center"
        self.pokaz_kwote["text"] = "0 PLN"
        self.pokaz_kwote.place(x=300,y=330,width=200,height=30)

        b15m=tk.Button(root)
        b15m["bg"] = "#fcc280"
        ft = tkFont.Font(family='Times',size=10)
        b15m["font"] = ft
        b15m["fg"] = "#000000"
        b15m["justify"] = "center"
        b15m["text"] = "+15m"
        b15m.place(x=310,y=140,width=40,height=30)
        b15m["command"] = self.b15m_command

        b1h=tk.Button(root)
        b1h["bg"] = "#fcc280"
        ft = tkFont.Font(family='Times',size=10)
        b1h["font"] = ft
        b1h["fg"] = "#000000"
        b1h["justify"] = "center"
        b1h["text"] = "+1h"
        b1h.place(x=390,y=140,width=30,height=30)
        b1h["command"] = self.b1h_command

        b2h=tk.Button(root)
        b2h["bg"] = "#fcc280"
        ft = tkFont.Font(family='Times',size=10)
        b2h["font"] = ft
        b2h["fg"] = "#000000"
        b2h["justify"] = "center"
        b2h["text"] = "+2h"
        b2h.place(x=460,y=140,width=30,height=30)
        b2h["command"] = self.b2h_command

        b5h=tk.Button(root)
        b5h["bg"] = "#fcc280"
        ft = tkFont.Font(family='Times',size=10)
        b5h["font"] = ft
        b5h["fg"] = "#000000"
        b5h["justify"] = "center"
        b5h["text"] = "+5h"
        b5h.place(x=530,y=140,width=30,height=30)
        b5h["command"] = self.b5h_command

        b10h=tk.Button(root)
        b10h["bg"] = "#fcc280"
        ft = tkFont.Font(family='Times',size=10)
        b10h["font"] = ft
        b10h["fg"] = "#000000"
        b10h["justify"] = "center"
        b10h["text"] = "+10h"
        b10h.place(x=600,y=140,width=40,height=30)
        b10h["command"] = self.b10h_command

        b24h=tk.Button(root)
        b24h["bg"] = "#fcc280"
        ft = tkFont.Font(family='Times',size=10)
        b24h["font"] = ft
        b24h["fg"] = "#000000"
        b24h["justify"] = "center"
        b24h["text"] = "+24h"
        b24h.place(x=670,y=140,width=40,height=30)
        b24h["command"] = self.b24h_command

        label_data_wyjazdu=tk.Label(root)
        ft = tkFont.Font(family='Times',size=13)
        label_data_wyjazdu["font"] = ft
        label_data_wyjazdu["fg"] = "#333333"
        label_data_wyjazdu["justify"] = "center"
        label_data_wyjazdu["text"] = "Data wyjazdu z parkingu:"
        label_data_wyjazdu.place(x=0,y=190,width=274,height=48)

        pokaz_data_wyjazdu=tk.Label(root)
        pokaz_data_wyjazdu["bg"] = "#ffffff"
        ft = tkFont.Font(family='Times',size=10)
        pokaz_data_wyjazdu["font"] = ft
        pokaz_data_wyjazdu["fg"] = "#333333"
        pokaz_data_wyjazdu["justify"] = "center"
        pokaz_data_wyjazdu["text"] = "data_wyj_zpark"
        pokaz_data_wyjazdu.place(x=310,y=200,width=400,height=30)

        pokaz_data_rozpoczecia=tk.Label(root)
        pokaz_data_rozpoczecia["bg"] = "#ffffff"
        ft = tkFont.Font(family='Times',size=13)
        pokaz_data_rozpoczecia["font"] = ft
        pokaz_data_rozpoczecia["fg"] = "#333333"
        pokaz_data_rozpoczecia["justify"] = "center"
        pokaz_data_rozpoczecia["text"] = "data_aktualizowalna"
        pokaz_data_rozpoczecia.place(x=310,y=100,width=400,height=30)

    def b5gr_command(self):
        self.moneys.addMoney(Decimal(0.05))
        self.updateValue()


    def b10gr_command(self):
        self.moneys.addMoney(Decimal(0.1))
        self.updateValue()


    def b20gr_command(self):
        self.moneys.addMoney(Decimal(0.2))
        self.updateValue()



    def b50gr_command(self):
        self.moneys.addMoney(Decimal(0.5))
        self.updateValue()



    def b2zl_command(self):
        self.moneys.addMoney(Decimal(2))
        self.updateValue()


    def b1zl_command(self):
        self.moneys.addMoney(Decimal(1))
        self.updateValue()


    def bZatwierdz_command(self):
        print("command")


    def b2gr_command(self):
        self.moneys.addMoney(Decimal(0.02))
        self.updateValue()


    def b1gr_command(self):
        self.moneys.addMoney(Decimal(0.01))
        self.updateValue()


    def b5zl_command(self):
        self.moneys.addMoney(Decimal(5))
        self.updateValue()


    def b10zl_command(self):
        self.moneys.addMoney(Decimal(10))
        self.updateValue()


    def b20zl_command(self):
        self.moneys.addMoney(Decimal(20))
        self.updateValue()


    def b50zl_command(self):
        self.moneys.addMoney(Decimal(50))
        self.updateValue()


    def b15m_command(self):
        print("command")


    def b1h_command(self):
        print("command")


    def b2h_command(self):
        print("command")


    def b5h_command(self):
        print("command")


    def b10h_command(self):
        print("command")


    def b24h_command(self):
        print("command")

    def updateValue(self):
        max_coins,money_sum = self.moneys.getMoney()
        print(max_coins)
        if max_coins < 200:
            self.pokaz_kwote["text"] = str(money_sum)+" PLN"
        else:
            self.pokaz_kwote["text"] = str(money_sum) + " PLN - Max. monet!"
    def getMoney(self):
        max_coins, money_sum = self.moneys.getMoney()
        return money_sum