from tkinter import *
from tkinter import ttk
from os import listdir
from os.path import isfile, join

import Lesson

def openLesson(lesson,home):
   home.forget()
   lesson.frame.pack()

def closeLesson(lesson,home):
   lesson.frame.forget()
   home.pack()

if __name__ == "__main__":
   root = Tk()
   home = ttk.Frame(root, padding=10)
   ttk.Label(home, text="Lessons").pack(pady=20)

   #get files in lessons path
   filePaths = [f for f in listdir("Lessons") if isfile(join("Lessons", f))]

   lessons:list[Lesson.Lesson] = []
   for filePath in filePaths:
      lessons.append(Lesson.loadLesson("Lessons\\"+filePath,root,home))
      

   home.pack(fill='both',expand=1)

   root.mainloop()
