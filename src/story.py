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
                #time.sleep(0.05)

    def printChoice(self, name):
        time.sleep(0)
        if self.choiceText:
            for i in self.choiceText:
                for j in i:
                    sys.stdout.write(j)
                    sys.stdout.flush()
                    time.sleep(0.01)

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

r1 = Scene("r1", ["The boss tells you that it's nothing to worry about. She respects your decision, and tells you to go back to work. Of course, she suggests that she'd really appreciate it if you didn't tell anyone else. After the day's ended, back home, you decide to go to bed early. You think deeply about what the boss told you today. While you don't particularly regret your decision, you're feeling a bit uncertain about what to do with this knowledge.\n", "The easiest thing to do would certainly be to ignore that this happened and continue on with your life. However, the fact that the company has a secret team, much less a team that works on illicit projects, is enough to bother you. Maybe you should go talk to the boss about your concerns, or even find someone who can help resolve this issue.\n"], ["1: Decide not to do anything about the boss's team\n", "2: Decide to report your information about the team to an outside source\n", "3: Directly approach your boss with your conflicted feelings\n"], ["deontological", "aristotelian", "stoic"], ["r2", "r3", "r4"])

r2 = Scene("r2", ["Since you chose not to get involved, everything continues for the next few weeks as normal. However, soon enough, you are contacted by a news journalist from a fairly recognized media source.\n", "Apparently, the news source has received some kind of anonymous tip that there is some kind of consumer data stealing scheme going on behind the scenes at your company, and asks if you know anything about it.\n", "Your first thought is immediately of the secret team that your boss mentioned to you. You're not entirely sure that this is what the journalist is talking about, but you know that it at the very least might be. At this point, you could choose to reveal what you know to this journalist - after all, it might be for the good of society, and you don't even really have to be involved. On the other hand, you respect the boss and don't want to cause unnecessary trouble for her by sending a nosy journalist her way.\n"], ["1: Protect the boss by saying that you know nothing\n", "2: Mention suspicions of the team and tip off the journalist to investigate\n"], ["epicurean", "deontological"], ["mehEnd", "kantEnd"])

r3 = Scene("r3", ["You decide that the best way to handle the situation from here is to try and go public with the information that you have accrued. This seems to be the most effective way of putting a stop to the stealing of consumer data that is going on.\n", "Of course, while you have decided on this, you are unsure who to report your findings to. You could report them to the top executives of your company - that way, you may be able to shut it down without any overall damage to the company. You could also choose to report your findings to the media, as that always garners a reaction from the public. Finally, you could also choose to report to a newly established consumer privacy protection agency that, while still having to go through all the trials and tribulations of official process, could be just what you're looking for.\n"], ["1: Report to the company bigwigs\n", "2: Report to the media\n", "3: Report to the consumer protection agency\n"], ["aristotelian", "feminist", "legalist"], ["badNarcEnd", "r5", "r6"])

r4 = Scene("r4", ["You decide that what the boss and her team are doing is not right, and that it needs to stop. You decide that the best way to proceed in this case is to directly confront your boss about the issue. After all, you and her respect one another, and one another's opinion. There is a chance that she'll listen to what you have to say.\n", "The next morning, you go to talk to your boss. You tell her that you feel very strongly that she and the special company team shouldn't be stealing consumer data in the manner they are, even if it will result in strong profits for the company.\n", "After your confrontation, the boss seems hesitant to change her perspective. After all, she probably has a strong attachment to the idea still..\n"], ["1: Continue trying to convince the boss to stop the team\n", "2: Threaten to whistleblow the team's actions if they don't stop\n"], ["confucian", "utilitarian"], ["pointlessEnd", "r7"])

r5 = Scene("r5", ["You decide that the best way to solve the issue at hand is to garner public attention for it by reporting the story to the media. After all, the power truly lies in the hands of the people. You begin to consider which news source in particular to report it to. Three come to mind.\n", "Firstly, you could choose to report it to a very large news station. A story like yours could certainly garner a lot of attention, and by having it represented on such an important news source could bring even more results than you're looking for. Getting your story picked up at all would be hard to achieve, of course.\n", "You could also choose to report the story to a smaller, more local news outlet. They're not invisible, mind you - just not to the same scale as a massive news network. Reporting to this source could still lead to pretty noticeable awareness in the local community and change in the company. Plus, this source is more likely to listen to you.\n", "There is also the third option, which is choosing to report your findings to what is typically regarded as questionable news. This source will certainly take your story - they may even ask you for it before you get a chance. However, there is a far lower likelihood that anyone will take your story seriously because of the way that it is presented - but at the very least, it could still garner some attention in the company and community that leads to change.\n"], ["1: Report to a large, national news source\n", "2: Report to a smaller local news source\n", "3: Report to Alex Jones\n"], ["stoic", "aristotelian", "confucian"], ["CNEnd", "observerEnd", "infowarsEnd"])

r6 = Scene("r6", ["You decide that the most effective course of action would be to report your findings to that consumer privacy protection agency. After all, this type of thing is exactly what they were created to handle. You end up giving them a call.\n", "A few months later, a trial is called. This trial is the result of the protection agency calling a lawsuit on the company you used to work at, and accusing them of exactly what you learned - the illegal stealing of consumer data. You are called in to act as a witness for the trial.\n", "At some point, you are called to the stand to testify. As you are asked a series of questions, your eyes meet the boss's in the audience. She turns away. You start to have second thoughts about what you are doing. Could you really go against the boss like this?\n", "The moment of truth arrives and you are asked to deliver decisive testimony against the boss herself for being involved with this group. Will you mention her involvement, or will you try to protect the boss?\n"], ["1: Lie and say that the boss wasn't involved with the secret scheme\n", "2: Reveal everything you know, and incriminate all involved guilty parties\n"], ["epicurean", "legalist"], ["simpEnd", "legalEnd"])

r7 = Scene("r7", ["After bringing your threat to light, the boss looks very taken aback. After all, you and her had a strong and trustful relationship, and it seems that you've brought harm to that in her eyes. However, she decides that her project is too important, and that because of it, it's simply too dangerous to keep you at the company where you could potentially expose more information. She fires you.\n", "After being sent home, you once again reflect on your situation. Now, there's certainly no reason to keep quiet about what you have learned, especially after seeing a knee-jerk reaction like the one the boss had. Plus, it'd be a perfect way to enact revenge for being fired.\n", "Of course, your feelings of trust with the boss still persist, even now. Maybe it would be better to help someone that you do know rather than potentially helping consumers that you don't.\n"], ["1: Change your mind, and try to expose the boss's secret team to the public\n", "2: Stay quiet about the situation and move on with your life\n"], ["egoist", "epicurean"], ["r3", "cuckEnd"])

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
    "r2": r2,
    "r3": r3,
    "r4": r4,
    "r5": r5,
    "r6": r6,
    "r7": r7,
    "trashEnd": trashEnd,
    "reverseNarcEnd": reverseNarcEnd,
    "chadEnd": chadEnd,
    "mehEnd": mehEnd,
    "kantEnd": kantEnd,
    "badNarcEnd": badNarcEnd,
    "pointlessEnd": pointlessEnd,
    "CNEnd": CNEnd,
    "observerEnd": observerEnd,
    "infowarsEnd": infowarsEnd,
    "simpEnd": simpEnd,
    "cuckEnd": cuckEnd,
    "legalEnd": legalEnd
}
