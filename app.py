from tkinter import *
from tkinter import ttk

from Lesson import Lesson


if __name__ == "__main__":
   root = Tk()
   home = ttk.Frame(root, padding=10)
   home.grid()
   ttk.Label(home, text="Lessons").grid(column=0, row=0)

   lessons:list[Lesson] = []
   lessons.append(Lesson())
   lessons.append(Lesson())
   
   for i, lesson in enumerate(lessons):
      ttk.Button(home, text=lesson.name).grid(column=0,row=i+1)

   root.mainloop()