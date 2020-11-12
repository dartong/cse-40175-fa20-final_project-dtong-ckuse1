# Imports
import sys
import time


# Classes
class Scene:
    # Constructor
    # Usage example:m0 = Scene("m0", ["Paragraph 1\n", "Paragraph 2\n"], ["Choice 1\n", "Choice 2\n"], ["aristotilian", "utilitarian"], ["s1", "s2"])
    # Important note: have a new line char ("\n") at the end of each paragraph or choice!
    # Ending should look like this: s3 = Scene("s3", ["Line 1\n"], [0], [0], 0)
    def __init__(self, id, text, choiceText, choiceEthic, next):
        self.id = id                    # Scene identification
        self.text = text                # Dialogue text
        self.choiceText = choiceText    # Option text
        self.choiceEthic = choiceEthic  # Ethics associated with options
        self.next = next                # Array containing connected scenarios keys

    # Getters/Setters
    def getID(self):
        return self.id

    def getText(self):
        return self.text

    def getChoiceText(self):
        return self.choiceText
    
    def getChoiceEthic(self):
        return self.choiceEthic

    def getNext(self):
        return self.next

    # Utility
    def printScene(self, name):
        for i in self.text:
            for j in i:
                print(j, end="")
                time.sleep(0.05)

    def printChoice(self, name):
        time.sleep(0)
        for i in self.choiceText:
            for j in i:
                sys.stdout.write(j)
                sys.stdout.flush()
                time.sleep(0.05)

    def getNextScene(self, choice):
        return self.next[choice - 1]

    def getEthic(self, choice):
        return self.choiceEthic[choice - 1]

# Story content
s0 = Scene("s0", ["Line 1", "Line 2"], ["Choice 1", "Choice 2"], ["aristotelian", "epicurian"], ["s1", "s1"])

s1 = Scene("s1", ["Line 1", "Line 2"], ["Choice 1", "Choice 2"], ["aristotelian", "utilitarian"], ["s2", "s2"])

s2 = Scene("s1", ["Line 1", "Line 2"], [0], [0], 0)

eventMap = {"s0" : s0, "s1" : s1, "s2" : s2}        # Update the hash map for all story events
