from tkinter import *
from tkinter import ttk
from os import listdir
from os.path import isfile, join
import tkinter
from tkinter.font import Font

import Lesson

def openLesson(lesson,home):
   home.forget()
   lesson.frame.grid()

def closeLesson(lesson,home):
   lesson.frame.grid_forget()
   home.pack(fill='both',expand=1)

if __name__ == "__main__":
   root = Tk()

   lettersFont = Font(size=20, family="Courier")
   style = ttk.Style()
   style.configure("current.Label", background='lightblue', font=lettersFont)
   style.configure("correct.Label", background='lightgreen', font=lettersFont)
   style.configure("incorrect.Label", background='red', font=lettersFont)
   style.configure("fixed.Label", background='yellow', font=lettersFont)
   style.configure("blank.Label", font=lettersFont)


   home = ttk.Frame(root, padding=10)
   ttk.Label(home, text="Lessons").pack(pady=20)

   #get files in lessons path
   filePaths = [f for f in listdir("Lessons") if isfile(join("Lessons", f))]

   lessons:list[Lesson.Lesson] = []
   for filePath in filePaths:
      lessons.append(Lesson.loadLesson("Lessons\\"+filePath,root,home))
      

   home.pack(fill='both',expand=1)

   root.mainloop()
