import tkinter as tk
import tkinter.font as tkFont
from modules import interface
from modules import money
from modules import clock

if __name__ == "__main__":
    root = tk.Tk()
    window = interface.Window(root)
    window.createWindow(root)
    root.mainloop()





