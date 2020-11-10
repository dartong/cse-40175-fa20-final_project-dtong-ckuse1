# Imports
import sys
import time


# Classes
class Scene:
    # Constructor
    def __init__(self, id, text, choiceText, next):
        self.id = id                    # Scene identification
        self.text = text                # Dialogue text
        self.choiceText = choiceText    # Option text
        self.next = next                # Array containing connected scenarios keys

    # Getters/Setters
    def getID(self):
        return self.id

    def getText(self):
        return self.text
    
    def getNext(self):
        return self.next

    def getNextScene(self, choice):
        return self.next[choice - 1]

    # Utility
    def printScene(self):
        for i in self.text:
            print(i)
            time.sleep(3)
        time.sleep(2)
        for i in self.choiceText:
            print(i)


# Story content

s1 = Scene("s1", ["l1", "l2"], ["c1", "c2"], ["s2"])

map = {"s1" : s1, "s2" : s2}
