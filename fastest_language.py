#This code was written by SamusTea to help speedrunners determine what language
#is fastest when running Breath of the Wild. If you have any questions about
#the code or have any suggestions, please message me on Twitter, @SamusTea.

import numpy

cutscene_times={}
#The order of times are English, Spanish (Latin America), French (Canada),
#Japanese, Spanish (Spain), French (France), German, Italian, and Russian.
languages = ["English", "Spanish (Latin America)", "French (Canada)", "Japanese", "Spanish (Spain)", "French (France)", "German", "Italian", "Russian"]
cutscene_times["Sheikah Slate"] = numpy.array([.1, 1.29, 3.28, 0, .14, 4.01, 3.28, 1.27, .27])
cutscene_times["Open SoR"] = numpy.array([0, 5.01, 3.28, 3.1, 5.21, 7., 10.01, 6.10, 7.25])
cutscene_times["First Divine Beast"] = numpy.array([7.01, 8.18, 8.13, 0, 12.13, 11.14, 9.03, 12.11, 6.08])
cutscene_times["Divine Beasts Completed"] = numpy.array([9.02, 7.06, 9.06, 0, 12.23, 9.29, 12.26, 14.21, 13.26])
cutscene_times["Hebra Labyrinth"] = numpy.array([7.03, .04, .03, .05, .04, 0, 0, 0, 7.05])
cutscene_times["Gerudo Labryinth"] = numpy.array([7.07, .07, .05, .07, .07, .02, 0, .02, 7.07])
cutscene_times["Akkala Labryinth"] = numpy.array([7.04, .05, .03, .05, .05, 0, .04, .03, 7.07])
cutscene_times["Typhlo Ruins"] = numpy.array([7.03, .04, .03, .04, .04, 0, .03, .01, 7.06])
cutscene_times["Eventide Intro"] = numpy.array([13.24, 7.01, 6.29, 7.01, 7.01, 6.19, 6.14, 13.29, 0])
cutscene_times["Eventide Outro"] = numpy.array([6.28, .01, 7.01, 7.02, 0, 6.27, 7.02, 6.29, 7.02])
#The cutscenes times are ripped from Swiffy22's YouTube video:
#https://www.youtube.com/watch?v=yVaZdsgjWz8

print("Which speedrun are you doing?")
print("Options include: AnyPercent, AllShrines, AD, AMQ and Hundo.")
speedrun = raw_input("If your run isn't listed here, press return. \n")

timesaves = numpy.zeros(len(languages))

if (speedrun == "AnyPercent" or speedrun == "anypercent") or (speedrun=="any%" or speedrun=="Any%"):
    Slate = "y"
    SoR = "y"
    Beasts = "n"
    All_Beasts = "n"
    Labs = "n"
    Typhlo = "n"
    Eventide = "n"
 
elif speedrun == "AllShrines" or speedrun == "allshrines":
    Slate = "y"
    SoR = "y"
    Labs = "y"
    Typhlo = "y"
    Eventide = "y"
    Beasts = "n"
    All_Beasts = "n"

elif (speedrun == "AD" or speedrun == "AllDungeons") or (speedrun=="ad" or speedrun == "alldungeons"):
    Slate = "y"
    SoR = "y"
    Beasts = "y"
    All_Beasts = "y"
    Labs = "n"
    Typhlo = "n"
    Eventide = "n"

elif (speedrun == "AMQ" or speedrun == "AllMainQuests") or (speedrun == "amq" or speedrun == "allmainquests"):
    Slate = "y"
    SoR = "y"
    Beasts = "n"
    All_Beasts = "y"
    Labs = "n"
    Typhlo = "n"
    Eventide = "n"

elif (speedrun == "Hundo" or speedrun == "100%") or speedrun == "hundo":
    Slate = "y"
    SoR = "y"
    Beasts = "y"
    All_Beasts = "y"
    Labs = "y"
    Typhlo = "y"
    Eventide = "y"

else:
    print("Your run didn't fit a preset, so let's see which cutscenes you'll see:")
    Slate = raw_input("Are you going to pick up the Sheikah Slate? [y/n] ")

    SoR = raw_input("Are you going to clip out of Shrine of Resurrection? [y/n] ")

    Beasts = raw_input("Are you going to do a Divine Beast (before talking to Impa)? [y/n] ")

    All_Beasts = raw_input("Are you going to beat all of the Divine Beasts? [y/n] ")

    Labs = raw_input("Are you going to do the Labryinths? [y/n] ") 

    Typhlo = raw_input("Are you going to do the Typhlo Ruins? [y/n] ") 

    Eventide = raw_input("Are you going to do Eventide? [y/n] ")
    
if (Slate == "y" or Slate == "Y") or (Slate == "yes" or Slate == "Yes"):
    print("\nIncluding the sheikah slate cutscene...")
    timesaves = cutscene_times["Sheikah Slate"]

if (SoR == "n" or SoR == "N") or (SoR == "no" or SoR == "No"):
    print("Including the cutscene to exit the Shrine of Resurrection...")
    timesaves = timesaves + cutscene_times["Open SoR"]

if (Labs == "y" or Labs == "Y") or (Labs == "yes" or Labs == "Yes"):
    print("Including the cutscenes for the Labryinths...")
    timesaves = timesaves + cutscene_times["Hebra Labyrinth"] + cutscene_times["Gerudo Labryinth"] + cutscene_times["Akkala Labryinth"]

if (Beasts == "y" or Beasts == "Y") or (Beasts == "yes" or Beasts == "Yes"):
    print("Including the cutscene for the first Divine Beast...")
    timesaves = timesaves + cutscene_times["First Divine Beast"]

if (All_Beasts == "y" or All_Beasts == "Y") or (All_Beasts == "yes" or All_Beasts == "Yes"):
    print("Including the cutscene for completing all Divine Beasts...")
    timesaves = timesaves + cutscene_times["Divine Beasts Completed"]

if (Typhlo == "y" or Typhlo == "Y") or (Typhlo == "yes" or Typhlo == "Yes"):
    print("Including the cutscenes for the Typhlo Ruins...")
    timesaves = timesaves + cutscene_times["Typhlo Ruins"] 

if (Eventide == "y" or Eventide == "Y") or (Eventide == "yes" or Eventide == "Yes"):
    print("Including the cutscenes for the Eventide...")
    timesaves = timesaves + cutscene_times["Eventide Intro"]+ cutscene_times["Eventide Outro"]

fastest = numpy.where(timesaves == numpy.amax(timesaves))[0][0]

print("\nHere are the timesaves (compared to the slowest language) for all the languages:")
print("English: {} seconds".format(timesaves[0]))
print("Spanish (LA): {} seconds".format(timesaves[1]))
print("French (Canadian): {} seconds".format(timesaves[2]))
print("Japanese: {} seconds".format(timesaves[3]))
print("Spanish: {} seconds".format(timesaves[4]))
print("French: {} seconds".format(timesaves[5]))
print("German: {} seconds".format(timesaves[6]))
print("Italian: {} seconds".format(timesaves[7]))
print("Russian: {} seconds".format(timesaves[8]))
print("\nThe fastest language is {} and has {} seconds of timesave.".format(languages[fastest], numpy.amax(timesaves)))
exit()
