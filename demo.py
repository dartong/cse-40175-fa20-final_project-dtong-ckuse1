# IMPORTS
import sys
import time

# GLOBALS
# CLASSES
class Player:

    # Constructor/Initialization
    def __init__(self, inputName):
        self.name = inputName
        self.location = 'start'
        self.morality = 0
        self.decisionCount = 0
        self.currChoice = 0

    # Getters/Setters
    def getName(self):
        return self.name

    def getLocation(self):
        return self.location

    def getMorality(self):
        return self.morality

    def getDCount(self):
        return self.decisionCount

    def getCurrChoice(self):
        return self.currChoice

    def setName(self, inputName):
        self.name = inputName

    def setLocation(self, inputLocation):
        self.location = inputLocation

    def setMorality(self, inputMorality):
        self.morality = inputMorality

    def setDCount(self, inputCount):
        self.decisionCount = inputCount

    def setCurrChoice(self, inputChoice):
        self.currChoice = inputChoice

    def incrementDCount(self):
        self.decisionCount = self.decisionCount + 1

# FUNCTIONS
def main():

    # get player name as input
    print("Enter Player Name:")
    pname = sys.stdin.readline().strip()

    # create the player object
    player = Player(pname)

    # GAME START
    player.setLocation("officeOne")
    loadArea(player)

# function for when the player goes to a new location/scenario
def loadArea(player):

    # read out new scenario for new location
    readScenario(player)

    # print text for decision count
    print("--------------------\nDECISION " + str(player.getDCount() + 1) + "\n--------------------")

    # player makes their choice
    makeDecision(player)

    # change player location
    route(player)

    # load new scenario in
    loadArea(player)

# function for reading all scenario text
def readScenario(player):
    pl = player.getLocation()

    if pl == "officeOne":
        print("Office: scenario text")
        time.sleep(2)
        print("Office: scenario text part two")
        time.sleep(2)
    elif pl == "officeTwo":
        print("You've decided that the right thing to do is to report your new, juicy findings.")
        time.sleep(4)
        print("However, you're not sure who exactly to report them to.")
        time.sleep(3)
        print("Therefore, you take some time to think about who might be worth exposing these secrets with.")
        time.sleep(5)
    elif pl == "newsOne":
        print("You decide to report your findings to a local news outlet.")
        time.sleep(2)
        print("Good job, you narc.")
        time.sleep(2)
        exit()
    elif pl == "failOne":
        print("You decide not to do anything about it. After all, it's not your problem, right?")
        time.sleep(4)
        print("You head home and call it a day. You do feel slightly guilty, though.")
        time.sleep(4)
        print("test: failure")
        time.sleep(1)
        exit()
    elif pl == "failTwo":
        print("You decide to report your findings to the SEC.")
        time.sleep(2)
        print("However, you get the government agency confused with the NCAA conference.")
        time.sleep(3)
        print("Therefore, your only response is a quite angry and confused one from a college sports manager.")
        time.sleep(3)
        print("test: failure")
        time.sleep(1)
        exit()
    else:
        print("This location has no scenario.")
        time.sleep(3)
        exit()


# function for when the player makes a decision
def makeDecision(player):
    pl = player.getLocation()

    # Universal decision code
    choiceCount = 0
    print("Input your choice: (0 to exit)")

    # Logic for different locations
    if pl == "officeOne":
        choiceCount = 2
        print("1: Report your findings")
        print("2: Trash your findings")
    elif pl == "officeTwo":
        choiceCount = 3
        print("1: Report your findings the top executives in your company")
        print("2: Report your findings to a local news source, The Big Scoop")
        print("3: Report your findings to the SEC")

    # More universal decision code
    choosing = True
    choice = 0

    # loop for failed inputs
    while choosing:
        try:
            choice = int(sys.stdin.readline().strip())
        except:
            print("Invalid input, try again.")
            continue

        if choice == 0:
            exit()

        if choice > choiceCount or choice < 1:
            print("Invalid input, try again.")
        else:
            choosing = False

    player.setCurrChoice(choice)
    player.incrementDCount()

# function with all logic for transitioning scenarios
def route(player):
    pl = player.getLocation()
    pcc = player.getCurrChoice()

    if pl == "officeOne":
        if pcc == 1:
            player.setLocation("officeTwo")
        elif pcc == 2:
            player.setLocation("failOne")
    if pl == "officeTwo":
        if pcc == 1:
            player.setLocation("officeThree")
        elif pcc == 2:
            player.setLocation("newsOne")
        elif pcc == 3:
            player.setLocation("failTwo")

# MAIN DECLARATION
if __name__ == '__main__':
    main()
