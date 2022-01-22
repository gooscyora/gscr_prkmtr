import tkinter as tk
from modules import interface


if __name__ == "__main__":
    root = tk.Tk()
    window = interface.Window(root)
    window.createWindow(root)
    root.mainloop()