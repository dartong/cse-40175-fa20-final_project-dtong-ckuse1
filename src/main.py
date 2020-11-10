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
        self.morality = [0 for i in range(9)]       # [Aristotelian, Confucian, Deontological, Egoist, Epicurean, Legalist, Stoic, Utilitarian]
        self.currChoice = 0         # possibly unneeded

    # Getters/Setters
    def getName(self):
        return self.name

    def getLocation(self):
        return self.location

    def getMorality(self):
        return self.morality

    def getCurrChoice(self):
        return self.currChoice

    def setName(self, inputName):
        self.name = inputName

    def setLocation(self, inputLocation):
        self.location = inputLocation

    def setMorality(self, inputMorality):
        self.morality = inputMorality

    def setCurrChoice(self, inputChoice):
        self.currChoice = inputChoice

    # Utility
    def updateMorality(self, inputMorality):
        self.morality[inputMorality] += 1

# Functions
def runGame(player):
    while True:                     # Keep running the game until the end is reached
        scene = story.eventMap[player.getLocation()]    # Get current scene object
        # Check if the story is reaching its end
        if scene.next != 0:
            scene.printScene(player.getName())              # Print scene dialogue
            scene.printChoice(player.getName())             # Print choice dialogue
            choice = sys.stdin.readline().strip()           # Get user choice
            ethic = scene.getEthic(int(choice))                  # Get ethic chosen
            # Update player
            player.setLocation(scene.getNextScene(int(choice)))  # Set next location
            player.updateMorality(ethic)                    # Update player morality

        else:
            scene.printScene(player.getName())              # Print scene dialogue
            return


# Main execution
def main():
    # Get player name as input
    print("Enter Player Name:")
    pname = sys.stdin.readline().strip()

    # create the player object
    player = Player(pname)

    # GAME START
    runGame(player)

    print("done")

# Main declaration
if __name__ == '__main__':
    main()