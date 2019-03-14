import random
bigTenList = ["PURDUE","INDIANA","MICHIGAN", "NEBRASKA", "RUTGERS","IOWA","MARYLAND","MICHIGAN STATE","OHIO STATE","PENN STATE","MINNESOTA","ILLINOIS","WISCONSIN","NORTHWESTERN"]
purdue = "PURDUE"

bigTenFactor = 2
weight = 20

def PurdueCheck(team1, team2):
    if (team1["name"] == purdue):
        return team1
    if (team2["name"] == purdue):
        return team2
    return None

def BigTenBias(team):
    if team["name"] in bigTenList:
        team["rank"] -= bigTenFactor
    return None

def MathWay(team1,team2):
    print(str(team1["rank"]))
    print(str(team2["rank"]))
    
    BigTenBias(team1)
    BigTenBias(team2)

    team1Chance = weight - team1["rank"]
    team2Chance = weight - team2["rank"] 

    chanceCombine = team1Chance + team2Chance

    numberGenerated = random.randint(1,chanceCombine + 1)

    if (numberGenerated <= team1Chance):
        return team1

    return team2

def DetermineWinner(team1, team2):
    purdueResults = PurdueCheck(team1, team2)
    if (purdueResults != None):
        print("Boiler Up!")
        return purdueResults

    mathResults = MathWay(team1, team2)
    if (mathResults != None):
        return mathResults

    return "Yeah we shouldn't get here"
    
def RunProgram():
    bigTenFactor = input("What is your big ten bias? ")
    while(True):
        team1 = {}
        team1["name"] = input("What is Team 1's Name? ").upper()
        if (team1["name"] == "QUIT"):
            break
        team1["rank"] = input("What is Team 1's Rank ")
        team2 = {}
        team2["name"] = input("What is Team 2's Name? ").upper()
        team2["rank"] = input("What is Team 2's Rank ")

        

        print(DetermineWinner(team1, team2)["name"] + " is the Winner!")


RunProgram()