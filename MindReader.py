import tkinter as tk
import time
import random
from tkinter import ttk
from tkinter import messagebox
from tkinter import Toplevel

class ControllerPage(Toplevel):
    def __init__(self, parent, thought = None):
        super().__init__(parent)
        self.geometry('300x60')
        self.title('Reading Mind')
        self.thought = thought; 

        self.feedback = tk.Label(self, text = "Analyzing Brainwaves ...")
        self.feedback.pack()
        self.prog = ttk.Progressbar(self, orient= 'horizontal', length = 200, maximum = 180, mode ='determinate')
        self.prog.pack()
        self.prog.start()
        chance = random.randint(0,1)
        
        self.after(2000, self.updateMessage)
        self.after(4000, self.updateMessage2)
        if chance == 1:
            self.after(6000, self.updateMessage3)
        else:
            self.after(6000, self.updateMessage5)
        self.after(8000, self.updateMessage4)
        self.after(10000, self.finalFunction)
        
    def updateMessage(self):
        self.feedback.config(text  = "Parsing Memories ...")
    def updateMessage2(self):
        self.feedback.config(text  = "Predicting Possibilities ...")
    def updateMessage3(self):
        self.feedback.config(text  = "Signing a Deal with Satan ...")
    def updateMessage4(self):
        self.feedback.config(text  = "Reading Your Mind ...")
    def updateMessage5(self):
        self.feedback.config(text  = "Downloading Thoughts ...")
    def finalFunction(self):
        self.prog['value'] = 199
        self.prog.stop()
        time.sleep(.5)
        messagebox.showinfo("Mind Reader", "The Number you are thinking of is " + self.thought)
        self.destroy()


class MainPage(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('300x100')
        self.title('Mind Reader')
        self.grid()

        self.greeting = tk.Label(text = "Welcome to Mind Reader")
        self.message = tk.Label(text = "Think of a number from 1-99")
        self.entry = tk.Entry()
        self.greeting.pack()
        self.message.pack()
        self.entry.pack()

        self.activate = ttk.Button( self, text = "Read Mind", command = self.new_Window).pack()

        self.warning = tk.Label()
    def new_Window(self):
        thought = self.entry.get()
        if thought.isnumeric() and int(thought) > 0 and int(thought) < 100:
            self.message.config(text = "Think of a number from 1-99")
            ControllerPage(self, thought)
        else:
            self.message.config(text = "Please Input a valid Integer from 1-99")

if __name__ == "__main__":
    app = MainPage()
    app.mainloop()
