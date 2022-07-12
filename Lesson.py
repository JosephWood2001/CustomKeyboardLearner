from time import time
import jsonpickle
from tkinter import *
from tkinter import ttk

from numpy import pad
import CompleteWindow
from Keyboard import Keyboard

import app

rowLength = 60



class Lesson():
    
    def __init__(self, name, speed, accuracy, showKeys, text):
        self.name = name
        self.speed = speed
        self.accuracy = accuracy
        self.showKeys = showKeys
        self.text = text

    def init(self,root,home,nextLesson):
        self.cursorIndex = 0
        self.startTime = -1
        self.done = False

        self.home = home
        self.nextLesson = nextLesson

        self.frame = ttk.Frame(root, padding=10)
        self.frame.bind('<Key>', self.keyPressed)
        ttk.Label(self.frame, text=self.name).grid(column=0,row=0)
        self.stats = ttk.Frame(self.frame, padding=10)
        self.stats.grid(column=0,row=1,padx=10)
        self.clock = ttk.Label(self.stats, text='Time:0')
        self.clock.grid(column=0,row=0,padx=10)
        self.currentAcc = ttk.Label(self.stats, text='Accuracy:100%')
        self.currentAcc.grid(column=1,row=0,padx=10)
        self.WPM = ttk.Label(self.stats, text='WPM:0')
        self.WPM.grid(column=2,row=0)

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
        self.textFrame.grid(column=0,row=2)
        self.updateLetterColors()

        #Keyboard
        self.keyboardFrame = Frame(self.frame)
        self.keyboard = Keyboard(self.keyboardFrame)
        self.keyboardFrame.grid(column=0,row=3)
        self.keyboard.light(self.text[0])

        #Home button
        ttk.Button(self.frame, text="Home", command=lambda: app.closeLesson(self,home)).grid(column=0,row=4)
        #Lesson button
        ttk.Button(home, text=self.name, command=lambda: app.openLesson(self,home)).pack()

    def reset(self):
        self.cursorIndex = 0
        self.startTime = -1
        self.done = False
        self.correctLetters:list[int] = []
        self.incorrectLetters:list[int] = []
        self.fixedLetters:list[int] = []
        self.updateLetterColors()
        self.currentAcc.config(text="Accuracy:100%")
        self.clock.config(text="Time:0")
        self.WPM.config(text="WPM:0")
        self.frame.bind('<Key>', self.keyPressed)
    
    def accRefresh(self):
        if self.done: return

        if self.cursorIndex == 0:
            self.currentAcc.config(text="Accuracy:100%")
            return
        currentAccuracy = int(100*(self.cursorIndex - 2 * len(self.incorrectLetters) - len(self.fixedLetters))/(self.cursorIndex))
        self.currentAcc.config(text="Accuracy:"+str(currentAccuracy) + "%")

        if (self.cursorIndex - 2 * len(self.incorrectLetters) - len(self.fixedLetters))/(self.cursorIndex) >= self.accuracy:
            self.currentAcc.configure(style="above.Label")
        else:
            self.currentAcc.configure(style="below.Label")

    def clockRefresh(self):
        if self.done or self.startTime == -1: return

        totalTime = int(10*(time()-self.startTime))
        self.clock.config(text="Time:"+str(totalTime/10))
        self.WPMRefresh()
        self.clock.after(100,self.clockRefresh)

    def WPMRefresh(self):
        if self.done: return

        totalTime = time()-self.startTime
        if(totalTime == 0):
            return
        WPM = int(self.cursorIndex/5/totalTime*60)
        self.WPM.config(text="WPM:"+str(WPM))

        if self.cursorIndex/5/totalTime*60 >= self.speed:
            self.WPM.configure(style="above.Label")
        else:
            self.WPM.configure(style="below.Label") 

    def updateLetterColors(self):
        self.accRefresh()
        self.WPMRefresh()
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

        #lesson attempt finished
        if self.cursorIndex > len(self.text) - 1:
            self.endTime = time()
            self.finished()

    def finished(self):
        
        self.done = True
        self.frame.unbind('<Key>')
        if self.cursorIndex/5/(self.endTime - self.startTime)*60 >= self.speed and (self.cursorIndex - 2 * len(self.incorrectLetters) - len(self.fixedLetters))/(self.cursorIndex) >= self.accuracy:
            success = CompleteWindow.Success(lambda: app.closeLesson(self,self.home),self.reset,self.nextLesson)
        else:
            success = CompleteWindow.Success(lambda: app.closeLesson(self,self.home),self.reset,None)

    def keyPressed(self,event):

        if (event.keysym == "Shift_L" or event.keysym == "Shift_R" or event.keysym == "Control_L"
            or event.keysym == "Control_R" or event.keysym == "Caps_Lock" or event.keysym == "Alt_L"
            or event.keysym == "Alt_R" or event.keysym == "Win_L" or event.keysym == "App"
            or event.keysym == "Return"):
            return

        if self.startTime == -1:
            self.startTime = time()
            self.clockRefresh()

        if event.char == '\x08' and self.cursorIndex != 0:
            self.cursorIndex -= 1
            self.keyboard.light(self.text[self.cursorIndex])
            self.updateLetterColors()
            return
        
        if event.char == '\x08': return
        
        if self.cursorIndex + 1 < len(self.text):
            self.keyboard.light(self.text[self.cursorIndex + 1])
        else:
            self.keyboard.light('')

        #cursor index incorrect
        try:
            self.incorrectLetters.index(self.cursorIndex)
            if self.text[self.cursorIndex] == event.char:
                self.incorrectLetters.remove(self.cursorIndex)
                self.fixedLetters.append(self.cursorIndex)
                self.cursorIndex+=1
                self.updateLetterColors()
                return
            else:
                self.cursorIndex+=1
                self.updateLetterColors()
                return
        except ValueError:
            pass

        #cursor index fixed
        try:
            self.fixedLetters.index(self.cursorIndex)
            if self.text[self.cursorIndex] == event.char:
                self.cursorIndex+=1
                self.updateLetterColors()
                return
            else:
                self.fixedLetters.remove(self.cursorIndex)
                self.incorrectLetters.append(self.cursorIndex)
                self.cursorIndex+=1
                self.updateLetterColors()
                return
        except ValueError:
            pass

        #cursor index correct
        try:
            self.correctLetters.index(self.cursorIndex)
            if self.text[self.cursorIndex] == event.char:
                self.cursorIndex+=1
                self.updateLetterColors()
                return
            else:
                self.correctLetters.remove(self.cursorIndex)
                self.incorrectLetters.append(self.cursorIndex)
                self.cursorIndex+=1
                self.updateLetterColors()
                return
        except ValueError:
            pass

        #cursor index none
        if self.text[self.cursorIndex] == event.char:
            self.correctLetters.append(self.cursorIndex)
            self.cursorIndex+=1
            self.updateLetterColors()
            return
        else:
            self.incorrectLetters.append(self.cursorIndex)
            self.cursorIndex+=1
            self.updateLetterColors()
            return


        



def loadLesson(fileName:str,root,home,nextLesson) -> Lesson:
    with open(fileName,'r') as file:
        lesson = jsonpickle.decode(file.read())
        lesson.init(root,home,lambda : nextLesson(lesson))
        return lesson


