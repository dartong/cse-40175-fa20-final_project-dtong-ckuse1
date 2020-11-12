# Imports
import sys
import time
import story

# Globals

# Classes
class Player:

    # Constructor/Initialization
    def __init__(self, inputName):
        self.name = inputName
        self.location = "s0"
        self.morality = {
            "aristotelian"  : 0,
            "confucian"     : 0,
            "deontological" : 0,
            "egoist"        : 0,
            "epicurian"     : 0,
            "legalist"      : 0,
            "stoic"         : 0,
            "utilitarian"   : 0
        }
        self.choiceCount = 0         # possibly unneeded

    # Getters/Setters
    def getName(self):
        return self.name

    def getLocation(self):
        return self.location

    def getMorality(self):
        return self.morality

    def getCount(self):
        return self.choiceCount

    def setName(self, inputName):
        self.name = inputName

    def setLocation(self, inputLocation):
        self.location = inputLocation

    def setMorality(self, inputMorality):
        self.morality = inputMorality

    # Utility
    def updateMorality(self, inputMorality):
        self.morality[inputMorality] += 1

    def reset(self):
        self.setLocation("s0")
        self.setMorality([0 for i in range(9)])
        self.choiceCount = 0

    def newChoice(self):
        self.choiceCount += 1


# Functions
def runGame(player):
    while True:                     # Keep running the game until the end is reached
        scene = story.eventMap[player.getLocation()]    # Get current scene object
        # Check if the story is reaching its end
        if scene.next != 0:
            scene.printScene(player.getName())              # Print scene dialogue
            scene.printChoice(player.getName())             # Print choice dialogue
            choice = input("\n")           # Get user choice
            ethic = scene.getEthic(int(choice))                  # Get ethic chosen
            # Update player
            player.setLocation(scene.getNextScene(int(choice)))  # Set next location
            player.updateMorality(ethic)                    # Update player morality
            player.newChoice()

        else:
            scene.printScene(player.getName())              # Print scene dialogue
            return

def stat(player):
    morality = player.getMorality()
    max = 0
    alignment = "none of the"
    for key in morality.keys():
        if morality[key] > max:
            alignment = key
    print("\nYou made", player.choiceCount, "decisions.")
    print("Your ethic most closely aligns with", alignment, "ethics.")
    
    print("\nEthical Decision Distribution:")
    print("%15s0   20  40  60  80  100" % (""))
    for key in morality.keys():
        print("%14s |" % (key), end = "")
        string = ""
        for i in range(1, int((morality[key] / player.choiceCount) * 100), 5):
            string = string + "="
        print("{0:<20s}|".format(string))
    print("%15s  10  30  50  70  90" % (""))
    print("Values are shown in percentage, ")

# Main
def main():
    # Get player name as input
    uinput = input("Enter Player Name: ")

    # create the player object
    player = Player(uinput)

    # GAME START
    keepPlaying = True
    while keepPlaying == True:

        runGame(player)
        stat(player)

        uinput = input("Do you want to play again? y to continue, n to exit:")
        while uinput != "y" and uinput != "n":
            uinput = input("Invalid input! y to continue, n to exit: ")
        if uinput == "n":
            break
        else:
            player.reset()

    print("Thanks for playing!")

# Main declaration
if __name__ == '__main__':
    main()