import jsonpickle
from tkinter import *
from tkinter import ttk

import app

rowLength = 30



class Lesson():
    
    def __init__(self, name, speed, accuracy, showKeys, text):
        self.name = name
        self.speed = speed
        self.accuracy = accuracy
        self.showKeys = showKeys
        self.text = text

    def init(self,root,home):
        self.cursorIndex = 0

        self.frame = ttk.Frame(root, padding=10)
        ttk.Label(self.frame, text=self.name).grid(column=0,row=0)

        self.textFrame = ttk.Frame(self.frame)
        self.letters:list[ttk.Label] = []
        self.correctLetters:list[int] = []
        self.incorrectLetters:list[int] = []
        self.fixedLetters:list[int] = []
        i = 0
        j = 0
        for letter in self.text:
            tmp = ttk.Label(self.textFrame, text=letter)
            self.letters.append(tmp)
            tmp.grid(column=j,row=i)
            j+=1
            if j >= rowLength and letter == ' ':
                j=0
                i+=1
        self.textFrame.grid(column=0,row=1)
        self.updateLetterColors()

        ttk.Button(self.frame, text="Home", command=lambda: app.closeLesson(self,home)).grid(column=0,row=2)

        ttk.Button(home, text=self.name, command=lambda: app.openLesson(self,home)).pack()

    def updateLetterColors(self):
        
        for i, letter in enumerate(self.letters):
            if self.cursorIndex == i:
                letter.configure(style="current.Label")
                continue
            
            try:
                self.correctLetters.index(i)
                letter.configure(style="correct.Label")
                continue
            except ValueError:
                pass

            try:
                self.incorrectLetters.index(i)
                letter.configure(style="incorrect.Label")
                continue
            except ValueError:
                pass

            try:
                self.fixedLetters.index(i)
                letter.configure(style="fixed.Label")
                continue
            except ValueError:
                pass
            
            letter.configure(style="blank.Label")


def loadLesson(fileName:str,root,home) -> Lesson:
    with open(fileName,'r') as file:
        lesson = jsonpickle.decode(file.read())
        lesson.init(root,home)
        return lesson


