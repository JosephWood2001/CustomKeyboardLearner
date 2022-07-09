from random import random
import json
import jsonpickle

class Lesson():
    
    def __init__(self, name, speed, accuracy, showKeys, text):
        self.name = name
        self.speed = speed
        self.accuracy = accuracy
        self.showKeys = showKeys
        self.text = text



def loadLesson(fileName:str) -> Lesson:
    with open(fileName,'r') as file:
        return jsonpickle.decode(file.read())
