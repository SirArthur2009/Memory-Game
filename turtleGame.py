import random
import turtle
import time
import sqlite3

tess = turtle.Turtle()
alex = turtle.Turtle()
josh = turtle.Turtle()
dave = turtle.Turtle()

turtles = ["tess", "alex", "josh", "dave"]

BasicAddr = "C:\\Users\\levig\\OneDrive\\Documents\\Coding\\Python\\Games\\Memory Game\\"
BTLAddr = BasicAddr + "Blue-Top-Left.gif"
YBLAddr = BasicAddr + "Yellow-Bottom-Left.gif"
RBRAddr = BasicAddr + "Red-Bottom-Right.gif"
GTRAddr = BasicAddr + "Green-Top-Right.gif"
DTLAddr = BasicAddr + "Depressed-Top-Left.gif"
DBLAddr = BasicAddr + "Depressed-Bottom-Left.gif"
DBRAddr = BasicAddr + "Depressed-Bottom-Right.gif"
DTRAddr = BasicAddr + "Depressed-Top-Right.gif"
shapes = [BTLAddr, YBLAddr, RBRAddr, GTRAddr, DTLAddr, DBLAddr, DBRAddr, DTRAddr]
for shape in shapes:
    turtle.register_shape(shape)

patternString = []
currentString = []
listening = True
bgColor = "light blue"

wn = turtle.Screen()
wn.title("Memory Game")
#Automatically set the size of the window to fullscreen
wn.setup(width=0.95, height=0.9)

def addNewPattern():
    global patternString
    patternString.append(turtles[random.randint(0, 3)])

def playPattern():
    bgColor = "light green"
    updateScore(len(patternString)-1, bgColor)
    wn.bgcolor(bgColor)
    updatePlayer("Playing...", bgColor)
    time.sleep(1)
    for unit in patternString:
        if unit == "tess":
            tess.shape(DTLAddr)
            time.sleep(0.2)
            tess.shape(BTLAddr)
        elif unit == "alex":
            alex.shape(DBLAddr)
            time.sleep(0.2)
            alex.shape(YBLAddr)
        elif unit == "josh":
            josh.shape(DBRAddr)
            time.sleep(0.2)
            josh.shape(RBRAddr)
        elif unit == "dave":
            dave.shape(DTRAddr)
            time.sleep(0.2)
            dave.shape(GTRAddr)
        time.sleep(0.5)

def updateClickTess(x, y):
    global currentString
    currentString.append("tess")
    tess.shape(DTLAddr)
    time.sleep(0.17)
    tess.shape(BTLAddr)
    checkRest()
def updateClickAlex(x, y):
    global currentString
    currentString.append("alex")
    alex.shape(DBLAddr)
    time.sleep(0.17)
    alex.shape(YBLAddr)
    checkRest()
def updateClickJosh(x, y):
    global currentString
    currentString.append("josh")
    josh.shape(DBRAddr)
    time.sleep(0.17)
    josh.shape(RBRAddr)
    checkRest()
def updateClickDave(x, y):
    global currentString
    currentString.append("dave")
    dave.shape(DTRAddr)
    time.sleep(0.17)
    dave.shape(GTRAddr)
    checkRest()


def checkRest():
    global currentString, bgColor
    time.sleep(0.2)
    correct = checkPatterns()

    if not correct:
        endGame()

    #Check if at end
    if len(patternString) == len(currentString):
        currentString = []
        addNewPattern()
        playPattern()

        bgColor = "light blue"
        updateScore(len(patternString)-1, bgColor)
        wn.bgcolor(bgColor)
        updatePlayer("Your turn", bgColor)

#Update functions
def updatePlayer(player, bgColor, display=True):
    playerTurn = turtle.Turtle()
    playerTurn.hideturtle()
    playerTurn.speed(0)
    playerTurn.penup()
    playerTurn.goto(0, 50)
    playerTurn.pendown()
    playerTurn.color(bgColor)
    playerTurn.begin_fill()

    playerTurn.fd(60)
    playerTurn.lt(90)
    playerTurn.fd(30)
    playerTurn.lt(90)
    playerTurn.fd(125)
    playerTurn.lt(90)
    playerTurn.fd(30)
    playerTurn.lt(90)
    playerTurn.fd(65)

    playerTurn.end_fill()
    if display:
        playerTurn.color("black")
        playerTurn.write(player, False, 'center', ("Times New Roman", 22, "normal"))
def updateScore(score, color, display = True, full = False):
    scoreTurtle = turtle.Turtle()
    scoreTurtle.hideturtle()
    scoreTurtle.speed(0)
    scoreTurtle.color(color)
    scoreTurtle.begin_fill()
    
    scoreTurtle.fd(75)
    scoreTurtle.lt(90)
    scoreTurtle.fd(25)
    scoreTurtle.lt(90)
    scoreTurtle.fd(155)
    scoreTurtle.lt(90)
    scoreTurtle.fd(25)
    scoreTurtle.lt(90)
    scoreTurtle.fd(75)

    scoreTurtle.end_fill()
    if display:
        scoreTurtle.color("black")
        scoreTurtle.write("Your score is: " + str(score), False, 'center', ("Times New Roman", 18, "normal"))

#End game function
def endGame():
    global listening
    wn.clear()
    listening = False
    heyo = turtle.Turtle()
    heyo.hideturtle()
    heyo.penup()
    heyo.goto(0, 150)
    heyo.write("Game Over", False, "center", ("Arial", 72, "normal"))

    #Create popup which ask for the players name to add to the leaderboard
    name = wn.textinput("Game Over", "Enter your name to add to the leaderboard:")
    if name is None or name == "":
        name = "Anonymous"

    leaderboardUpdate(name, len(patternString)-1)
    
def checkPatterns():
    for i in range(len(currentString)):
        if currentString[i] != patternString[i] and currentString[i] in ["alex", "tess", "josh", "dave"]:
            return False
    return True

def main():
    tess.shape(BTLAddr)
    alex.shape(YBLAddr)
    josh.shape(RBRAddr)
    dave.shape(GTRAddr)
    myTurtles = [tess, alex, josh, dave]
    for myTurtle in myTurtles:
        myTurtle.penup()
    
    tess.goto(-170, 170)
    alex.goto(-170, -170)
    josh.goto(170, -170)
    dave.goto(170, 170)

    displayLeaderboard()

    addNewPattern()
    playPattern()
    updatePlayer("Your turn", bgColor)
    updateScore(len(patternString)-1, bgColor)
    wn.bgcolor(bgColor)

    #Check for clicks
    wn.listen()
    if listening:
        tess.onclick(updateClickTess)
        alex.onclick(updateClickAlex)
        josh.onclick(updateClickJosh)
        dave.onclick(updateClickDave)

    wn.mainloop()

#Leaderboard functions
def leaderboardUpdate(name, score):
    # Connect to a database (or create one if it doesn't exist)
    conn = sqlite3.connect(BasicAddr+"leaderBoard.db")
    # Create a cursor object
    c = conn.cursor()

    # Create a table
    c.execute('''CREATE TABLE IF NOT EXISTS scores
              (id INTEGER PRIMARY KEY, name TEXT, score INTEGER)''')
    # Insert a row of data
    c.execute('''INSERT INTO scores (name, score) VALUES (?, ?)''', (name, score))
    conn.commit()
    conn.close()    

def getLeaderboard():
    # Connect to a database (or create one if it doesn't exist)
    conn = sqlite3.connect(BasicAddr+"leaderBoard.db")
    # Create a cursor object
    c = conn.cursor()

    # Create a table
    c.execute("""SELECT name, score FROM scores
              ORDER BY score DESC
LIMIT 10;""")

    scores = c.fetchall()
    print(scores)
    conn.commit()
    conn.close()   
    return scores

def compileLeaderBoard(leaderboard):
    newLeaderboard = "Top 10 Leaderboard:\n"

    for score in leaderboard:
        newLeaderboard += str(leaderboard.index(score)+1) + ". " + score[0] + "\t" + str(score[1])+"\n"

    return newLeaderboard

def displayLeaderboard():
        # Create a turtle for the leaderboard and modify its properties
        newT = turtle.Turtle()
        newT.hideturtle()
        newT.penup()
        newT.speed(0)
        newT.color("black")
        newT.goto(-500, 200)
        newT.write(compileLeaderBoard(getLeaderboard()), False, 'center', ("Times New Roman", 18, "normal"))

if __name__ == "__main__":
    main()