import jsonpickle
from tkinter import *
from tkinter import ttk

import app

class Lesson():
    
    def __init__(self, name, speed, accuracy, showKeys, text):
        self.name = name
        self.speed = speed
        self.accuracy = accuracy
        self.showKeys = showKeys
        self.text = text

    def init(self,root,home):
        self.frame = ttk.Frame(root, padding=10)
        ttk.Label(self.frame, text=self.name).pack(pady=20)
        ttk.Button(self.frame, text="Home", command=lambda: app.closeLesson(self,home)).pack()

        ttk.Button(home, text=self.name, command=lambda: app.openLesson(self,home)).pack()



def loadLesson(fileName:str,root,home) -> Lesson:
    with open(fileName,'r') as file:
        lesson = jsonpickle.decode(file.read())
        lesson.init(root,home)
        return lesson


