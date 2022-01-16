import tkinter as tk
import tkinter.font as tkFont
from modules import interface
from modules import money

if __name__ == "__main__":
    root = tk.Tk()
    window = interface.Window()
    window.createWindow(root)
    print(window.getMoney())



    root.mainloop()



