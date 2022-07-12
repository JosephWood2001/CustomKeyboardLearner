import tkinter
from tkinter import ttk


class Success:
    #creates parent window
    def __init__(self,home,retry,next):
               
        self.root = tkinter.Tk()
        self.root.focus_force()
        self.root.bind('<Return>', lambda event : self.close(next))
        self.root.bind('<BackSpace>', lambda event : self.close(retry))

        if next != None:
            self.title = ttk.Label(self.root,text="Success")
            self.title.pack()
        else:
            self.title = ttk.Label(self.root,text="Failure")
            self.title.pack()

        self.home_btn = ttk.Button(self.root,text="Home", command = lambda : self.close(home))
        self.home_btn.pack()

        self.retry_btn = ttk.Button(self.root,text="Retry", command = lambda : self.close(retry))
        self.retry_btn.pack()

        if next != None:
            self.next_btn = ttk.Button(self.root,text="Next", command = lambda : self.close(next))
            self.next_btn.pack()

    def close(self, exitFunc):
        exitFunc()
        self.root.destroy()

   