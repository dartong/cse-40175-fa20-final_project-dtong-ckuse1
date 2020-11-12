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
                sys.stdout.write(j)
                sys.stdout.flush()
                time.sleep(0.05)

    def printChoice(self, name):
        time.sleep(0)
        if self.choiceText:
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
b1 = Scene("b1", ["\"Good morning. The time is 8:30 AM. You have 5 appointments today, starting with...\" The voice of your virtual assistant fades away as your mind drifts towards getting ready for work today.\n", "You are an employee at a large internet advertisement agency. You specifically are an expert at devising algorithms to target web consumers based on their available data. Today, walking into work, someone lets you know that your boss is looking to speak with you at some point. You shrug your things off at your desk and wander over to the boss's office. Your boss calls you in and asks you to sit down, and you do as you're told. Then, the boss changes everything. She begins to explain that she wants you to join a team - a secret team operating within the company, which holds the task of personally looking through illegally gathered consumer data, and devising the best possible algorithms from them. Since your skills are exactly what they need, they want you. What do you do?\n", "Accepting her offer could definitely lead to financial or other benefits in your career - but you would be risking dangerous activity, not to mention messing with peoples' data. On the other hand, turning away from this could damage your career at this company as well.\n"], ["1: Accept the boss's offer and join the team\n", "2: Politely refuse to join\n"], ["egoist", "feminist"], ["m1", "r1"])

m1 = Scene("m1", ["The boss tells you that she is very satisfied with your answer! She then tells you that she’ll tell you more tomorrow, but that for now you should just go back to work like normal. After the day's ended, back home, you decide to go to bed early. You think deeply about what the boss told you today, but still feel a bit uncertain about joining her special team. You decide to think about how to approach this project.\n", "If you decide to fully get on board with this, there could definitely be good things in store for you - perhaps a promotion? Certainly fame in the community, after developing such a noteworthy algorithm. It would also certainly bring profits to the company you've worked at for so long. Plus, the consumer data isn't really going to anything bad, so they're barely even victims.\n", "Of course, you would still be stealing consumer data, which is illegal and just doesn't sit right with you. Perhaps there could be a better way? Maybe the algorithm could still be completed in some other, painstaking way. It'd be a long shot, but you may feel better about it.\n"], ["1: Decide that the benefits of using consumer data outweighs it's privacy violations\n", "2: Try to change the development approach\n"], ["egoist", "utilitarian"], ["m2", "m4"])

m2 = Scene("m2", ["The next day, you have your very first meeting with the secret company team. The boss is there, of course. She is accompanied by 5 other company members, all looking relatively older in age, and quite stern. Not exactly what you're looking for from a team, but you keep your hopes up. As they brought you onto the team because of your algorithm expertise, they proceed to show you what their previous plans were. Looking through them, you observe that they are actually pretty good.\n", "However, you also immediately notice that with a slight addition in consumer data, the algorithm could be greatly improved, making it groundbreaking. However, that slight addition would be highly questionable consumer data that would certainly violate privacy laws.\n", "You could also choose not to mention anything and agree to use the plans they already had in store - that way, you would just be using consumer data that didn't make you feel as bad for using. Of course, not as many benefits would be in store if you were to do that.\n"], ["1: Suggest that the algorithm be upgraded even further by looking even deeper into personal customer data\n", "2: Agree that the team's ideas for the algorithm are sufficient and decide to go along with plans using less consumer data"], ["egoist", "epicurean"], ["m3", "m4"])

m3 = Scene("m3", ["You decide to present your algorithm improvement - the benefits just sound too good. You're not the only one who thinks so, though. Everyone on the team is excited by your newfound discoveries. Enthusiastically, the motion to move forward with this enhanced algorithm carries through. However, one member of the team, a middle-aged man, seems mildly displeased throughout all of it.\n", "Three weeks have passed. Progress is continuing extremely well. Thanks to your helpful suggestions and efforts, the efficiency of the working algorithm has nearly doubled, and the team couldn't be happier with your progress. However, one day, the boss calls a meeting to discuss an email that she had recently received. Apparently, the boss received an inquiry from a local news source asking about the potential illegal data harvesting that is present in the algorithm. Everyone is surprised - however, that one man who didn't seem fully on board with your ideas seems to have developed a sudden nervous twitch.\n", "After the meeting, you report your suspicious claims about the man to the boss. The boss takes your suggestions under advisement and subtly suggests to you that you test the algorithm one more time - this time, perhaps on your fellow employee. After all, that may make the problem at hand go away.\n", "If you were to do so, it may remove this suspicious news source, as well as remove any potential danger of revealing information by an insider. This would help guarantee your safety, as well as keep yourself profitable. You would have to blackmail a man to do it, though.\n"], ["1: Take your boss's off-the-record advice and blackmail your coworker\n", "2: Decide to risk it and not blackmail him\n"], ["egoist", "stoic"], ["trashEnd", "reverseNarcEnd"])

m4 = Scene("m4", ["You decide that digging even deeper into consumer data is not worth the troubles that accompany it - and it certainly doesn't make you feel good about it, either. Rather, you become inspired - you now want to find a way to develop an algorithm that only uses consumer data that is legally available and safe to use. For now, you will wait and simply go along with the plans that the team has already proposed from you. However, whenever you have a team meeting, you can notice the cautious gaze of one team member in particular..\n", "After a few months, the boss calls you in to talk. Then, she explains that the team has discovered a way to improve the algorithm by furthering consumer data usage - the very thing you already noticed. She wants you to begin implementation of this immediately. However, your hesitant thoughts from before resurface - you ask if there is any way to simply continue your current progress. The work already being done has still been successful, after all. However, it seems the boss has no choice, as she then gives you an ultimatum - either you do what she asks, or unfortunately the only other option is for you to leave the team, and lose all benefits that you were receiving for it.\n", "This is a big decision - it could be worth risking asking the boss for more time. That may backfire, though.\n"], ["1: Agree that the algorithm be upgraded even further by looking even deeper into personal customer data\n", "2: Decide to ask the boss to wait for a decision\n"], ["epicurean", "confucian"], ["reverseNarcEnd", "chadEnd"])

r1 = Scene("r1", ["\n", "\n", "\n"], ["1: \n", "2: \n"], ["", ""], ["r2", "r3", "r4"])
r2 = Scene("r2", ["\n", "\n", "\n"], ["1: \n", "2: \n"], ["", ""], ["mehEnd", "kantEnd"])
r3 = Scene("r3", ["\n", "\n", "\n"], ["1: \n", "2: \n", "3: \n"], ["", "", ""], ["badNarcEnd", "r5", "r6"])
r4 = Scene("r4", ["\n", "\n", "\n"], ["1: \n", "2: \n"], ["", ""], ["pointlessEnd", "r7"])
r5 = Scene("r5", ["\n", "\n", "\n"], ["1: \n", "2: \n", "3: \n"], ["", "", ""], ["CNEnd", "observerEnd", "infowarsEnd"])
r6 = Scene("r6", ["\n", "\n", "\n"], ["1: \n", "2: \n"], ["", ""], ["simpEnd", "legalEnd"])
r7 = Scene("r7", ["\n", "\n", "\n"], ["1: \n", "2: \n"], ["", ""], ["r3", "cuckEnd"])

trashEnd = Scene("trashEnd", ["You decide that the danger that your coworker poses is too risky. After all, you've put everything on the line at this point so that you can reap the benefits - but there's a lot at stake in the eyes of the law. Lucky for you, however, you find this guy's info using the very service you are developing, and boy is it good. There's plenty there to blackmail with - and surely enough, after the fact, that local news source had decided to stop sending their journalists to investigate. I suppose they had lost motivation for some reason.\n", "Well, after all, you end up rich and successful. However, at the expense of so many along the way, was it truly worth it? Only you will know.\n"], 0, 0, 0)

reverseNarcEnd = Scene("reverseNarcEnd", ["After making your decision, a few weeks pass. Turns out, that suspicious looking guy on your team ended up being the one to report everything to the local news. Eventually, they got enough info to release the story, and it blew up instantly. After all, the company had a decent name for itself up until now.\n", "Eventually, this led to lawsuits, and you were prosecuted successfully along with your secret team and the boss, leading to heavy consequences. It seems that leaving certain factors unchecked led to your consumer treatment being your downfall.\n"], 0, 0, 0)

chadEnd = Scene("chadEnd", ["Due to the trustful relationship that you share with the boss, they decide to believe in you and give you some extra time before removing you from the team. You excuse yourself for the day.\n", "At the end of the day, after getting ready to fall asleep, you think back on everything that's happened. The team, the algorithm... the algorithm. That's it! You've thought of a way to improve the algorithm without using extra unnecessary consumer data. This could work!\n", "After a week of the team not meeting, and a week of your hard work to develop your new algorithm, the team meeting finally arrives. You present your new discoveries - and it turns out the algorithm works even better than was originally expected! It seems by breaking out of your tunnel vision, you were able to find an even better solution. Since this new algorithm will still make the company big profits, the team agrees to use your new solution. Everything seemed to work out well, in the end - and you didn't even have to steal data.\n"], 0, 0, 0)

mehEnd = Scene("mehEnd", ["\n", "\n", "\n"], 0, 0, 0)
kantEnd = Scene("kantEnd", ["\n", "\n", "\n"], 0, 0, 0)
badNarcEnd = Scene("badNarcEnd", ["\n", "\n", "\n"], 0, 0, 0)
pointlessEnd = Scene("pointlessEnd", ["\n", "\n", "\n"], 0, 0, 0)
CNEnd = Scene("CNEnd", ["\n", "\n", "\n"], 0, 0, 0)
observerEnd = Scene("observerEnd", ["\n", "\n", "\n"], 0, 0, 0)
infowarsEnd = Scene("infowarsEnd", ["\n", "\n", "\n"], 0, 0, 0)
simpEnd = Scene("simpEnd", ["\n", "\n", "\n"], 0, 0, 0)
legalEnd = Scene("legalEnd", ["\n", "\n", "\n"], 0, 0, 0)
cuckEnd = Scene("cuckEnd", ["\n", "\n", "\n"], 0, 0, 0)


# Update the hash map for all story events
eventMap = {
    "b1": b1,
    "m1": m1,
    "m2": m2,
    "m3": m3,
    "m4": m4,
    "r1": r1,
    "trashEnd": trashEnd,
    "reverseNarcEnd": reverseNarcEnd,
    "chadEnd": chadEnd
}
