from tkinter import *
from tkinter import ttk
from os import listdir
from os.path import isfile, join

from Lesson import Lesson, loadLesson


if __name__ == "__main__":
   root = Tk()
   home = ttk.Frame(root, padding=10)
   home.grid()
   ttk.Label(home, text="Lessons").grid(column=0, row=0)

   #get files in lessons path
   filePaths = [f for f in listdir("Lessons") if isfile(join("Lessons", f))]

   lessons:list[Lesson] = []
   for filePath in filePaths:
      lessons.append(loadLesson("Lessons\\"+filePath))
   
   for i, lesson in enumerate(lessons):
      ttk.Button(home, text=lesson.name).grid(column=0,row=i+1)

   root.mainloop()
