import tkinter as tk
import time
from tkinter import ttk
from tkinter import messagebox
from tkinter import Toplevel

class ControllerPage(Toplevel):
    def __init__(self, master = None, thought = None):
        super().__init__(master = master)
        self.geometry('300x100')
        self.title('Mind Reader')
        self.grid()

        message2 = tk.Label(text = "Analyzing Brainwaves ...")

        message2.pack()

        #time.sleep(10)

        #messagebox.showinfo("Mind Reader", thought)

class MainPage:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry('300x100')
        self.window.title('Mind Reader')
        self.window.grid()

        self.greeting = tk.Label(text = "Welcome to Mind Reader")
        self.message = tk.Label(text = "Think of a number from 1-99")
        self.entry = tk.Entry()
        self.greeting.pack()
        self.message.pack()
        self.entry.pack()

        self.activate = ttk.Button( self.window, text = "Read Mind", command = self.new_Window(self.entry.get()))
        self.activate.pack()

        self.window.mainloop()

    def new_Window(self, thought):
        print("thought")
        
        tk.messagebox.showinfo("Mind Reader", "thought")
        #ControllerPage(self.window, thought)

if __name__ == "__main__":
    MainPage()
