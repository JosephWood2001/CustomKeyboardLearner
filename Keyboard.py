from email.policy import default
import json
from tkinter import LEFT, Frame, Label


class Keyboard():
    
    def __init__(self,frame):
        self.keys:list[Key] = []
        self.rows:list[Frame] = []

        tmp = Frame(frame)
        tmp.pack()
        self.rows.append(tmp)
        for i in range(0,14):
            if i == 13:
                self.keys.append(Key(0,i,tmp,2.2))
                continue
            self.keys.append(Key(0,i,tmp))
        tmp = Frame(frame)
        tmp.pack()
        self.rows.append(tmp)
        for i in range(0,14):
            if i == 0:
                self.keys.append(Key(1,i,tmp,1.6))
                continue
            if i == 13:
                self.keys.append(Key(1,i,tmp,1.6))
                continue
            self.keys.append(Key(1,i,tmp))
        tmp = Frame(frame)
        tmp.pack()
        self.rows.append(tmp)
        for i in range(0,13):
            if i == 0:
                self.keys.append(Key(2,i,tmp,1.93))
                continue
            if i == 12:
                self.keys.append(Key(2,i,tmp,2.4))
                continue
            self.keys.append(Key(2,i,tmp))
        tmp = Frame(frame)
        tmp.pack()
        self.rows.append(tmp)
        for i in range(0,12):
            if i == 0:
                self.keys.append(Key(3,i,tmp,2.5))
                continue
            if i == 11:
                self.keys.append(Key(3,i,tmp,2.97))
                continue
            self.keys.append(Key(3,i,tmp))
        tmp = Frame(frame)
        tmp.pack()
        self.rows.append(tmp)
        for i in range(0,8):
            if i == 0:
                self.keys.append(Key(4,i,tmp,1.6))
                continue
            if i == 2:
                self.keys.append(Key(4,i,tmp,1.3))
                continue
            if i == 3:
                self.keys.append(Key(4,i,tmp,7.3))
                continue
            if i == 4:
                self.keys.append(Key(4,i,tmp,1.3))
                continue
            if i == 7:
                self.keys.append(Key(4,i,tmp,1.6))
                continue
            self.keys.append(Key(4,i,tmp))

    def light(self,char):
        with open('keys.json', 'r') as f:
            chars = json.load(f)
            try:
                row = chars[char]['r']
                column = chars[char]['c']
                if(chars[char]['s'] == None):
                    sRow = None
                    sColumn = None
                else:
                    sRow = chars[char]['s']['r']
                    sColumn = chars[char]['s']['c']
            except KeyError:
                row = None
                column = None
                sRow = None
                sColumn = None
            
            

        for key in self.keys:
            if (key.row == row and key.column == column) or (key.row == sRow and key.column == sColumn):
                key.box.config(background="blue")
            else:
                key.box.config(background="grey")


class Key():
    height = 70
    def __init__(self,row:int,column:int,frame,size:float | None = None):
        self.row = row
        self.column = column
        if size == None:
            self.size = 1
        else:
            self.size = size

        self.box = Frame(frame,width=self.size*Key.height,height=Key.height,background="grey")
        self.box.pack(side=LEFT,padx=5,pady=5)