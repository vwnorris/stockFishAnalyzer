from manager import *
from games import *
from saveHandler import *
from excelReader import *
from plotters import *
from treeNode import *
from tree import *
from documentManager import *

def main():
    print("Begin")
    db = Games()
    m = Manager(db)
    m.addStockFishGames()
    ##############################################################
    # Insert the functinoality for the task you want to test here. 

    task11("Bird's opening", 4)

    # All tasks are explained in the documentation, and the 
    # code for testing them can be found below this main method: 
    ##############################################################
    print('Finished')


# Task 1
"""
Check out the game.py file. It is a datastructure for a game of chess, 
and can hold all information found in the stockfish.pgn file. 
"""

# Task 2
"""
The first lines already in the main-method contain reading all 2600 given stockfish games 
into a database of games in a manager class. This managerclass manages the database. 
The function for this can be found in the file saveHandler.py, called regexImport and saveGameToPgn. 
"""

# Task 3
"""
Add the function task3 to the main method, add "m" as the manager and chose an index from 0 to 2599. 
The funcion will then save that game to the file "testfile.pgn" in this folder. 
Try it with a few different indexes to make sure it works. 
"""
def task3(manager: Manager, index: int):
    manager.saveGame(index)

# Task 4
"""
The regexImport function that reads games already had that functionality, and now a new saver funciton 
saveGamesToPgn also has the same functionality. You can test this method below: 
This function saves the games in the manager, and therefore from the database to a file called "testfile2.pgn". 
As you can se in the file saveHandler.py, you can add any list of Game objects to that function and they will be 
saved in the same file. 
"""
def task4(manager: Manager):
    manager.saveGames()

# Task 5
"""
The functionality for this is found in the excelReader.py file. 
The game read from the Readeable.xlsx file has been modified some so it is not exactly found
in the given zip file of games. 

Remember to insert manager m into the writeexcelgame function, as well as the index of
the game you want to save. The games have been saved with the moves written down in pairs, 
as you suggested in the lecture. 
"""


def printTheGame():
    def readExcelFile()-> Game:
        newGame = getGameFromExcel('Readable.xlsx')
        return newGame
    g = readExcelFile()
    print(f'Event: {g.event}, White: {g.white}, Black: {g.black}, Result: {g.result}')
    print(g.moves)

def writeExcelGame(manager: Manager, index: int): 
    writeGameToExcel('written.xlsx', manager._database.games[index])

# Task 6
"""
The functionality for this is found in the documentManager.py file. 

Running the function generateDocument() generates the Figures.tex document. This document
also contains figures and tables already generated in this folder of all the other tasks. 

NB: In our computers, pylatex was not always cooperating. When it tries to make a pdf of the
.tex file, you must follow these steps in the terminal:

1. press enter
2. Write "Figures.tex"
3. Write "R"

We will have a premade pdf already in the folder in case this problem happens for you as well. 
"""
def task6():
    generateDocument()

# Task 7
"""
Functionality for generating this table is found in plotters.py. 

Use the function below to generate the chart again, and also check out the
function pltStatistics4Stockfish() in plotters.py. The generated png is 
saved as StockFish.png.
"""
def showStatsStockfish(m: Manager):
    pltStatistics4Stockfish(m._database)

# Task 8
"""
The graph of games still on-going after 1, 2, 3 ... n moves up to 150 full moves is in the pdf.
The function is called linePlot() in the file plotters.py, and you can choose the n yourself.

This graph also has the curves for games where stockfish started with white and where stockfish
started with black pieces. We can se that when stockfish started with black, more games lasted 
longer, but they all evened out pretty evenly. 

The calculation of the mean and standard deviation in total, when using white and when using 
black pieces is also in a table in the pdf. They were calculated using the function getStats()
in the file plotters.py
"""

def task8(db: Games, n: int):
    # Prints out to the terminal the means and standard deviations, 
    # as well as saving the png of the table as table.png
    getStats(db)
    linePlot(db, n)
    

# Task 9
"""
The datastructure for the tree can be found in the Class Tree, found in tree.py. 
It contains a list of Node - objects, found in treeNode.py. These nodes contain all
information conserning that specific move, including win percentages for white, 
black and tie percentage. It also contains a list of all games in the database that
have the same moves up to that specific move. Making new trees will be shown in 
task 11. 
"""


#Task 10
"""
With the startTree() method in tree.py, you parse a list of Game-objects and 
load them into a loading tree. The result is best when the list of games you 
load the tree with are a selected opening. You then you get more similar games over
the first moves, and don't get to much overwhelming information. The resolution of the 
.png is also low when loading to many moves, so when choosing an opening as the data
the result is best. 
"""


# Task 11
"""
The function makeGraphvizTree() in plotters.py plots a graph of the tree from a Tree object
over a chosen number of moves. The functinon printStatsForOpening() in plotters.py 
takes in an opening, and prints the stats for that opening to the terminal. 

The file of the tree is called OpeningTree.png, and will later be inserted in the table. 

Suggested openings are further down in this document, to copy and test. 
"""
def task11(openingMove: str, moves: int):
    printOpeningTree(moves, openingMove)


# Task 12
"""
The function we made to solve task 12 is in plotters.py, and is called
extractPopularOpenings(). This function takes in an integer n and a list 
of Game-objects. It then returns a table of all openings that have been 
played at least n times. The table also contains the win percentage of
the white player, the win percentage of the black player and the percentage
of games ending in a tie for that opening. 

Next to the opening name is the amount of times the opening has been played. 

The table is added to the pdf report when it is generated.
"""
def task12(n: int, db: Games):
    extractPopularOpenings(n, db)

# Finally
"""
For plotting all graphs and tables with our selected input, and then generating 
the latex document in one big function. 

The opening tree printed is Bird's opening, for 4 moves. 
The openings played over 100 times are inserted in the table.
The line plot shows active games after 150 moves. 

NB: Make sure to do the generatePDF() funciton AFTER you have 
already run the putItAllTogether() function, not at the same time. 
Generating the document must be the last ting happening. 

If there is a problem generating the pdf, the .tex file will still work
and should contain everything itself, the only problem is with generating the pdf. 

The .pdf Figures_copy.pdf contains a premade pdf of the generated .tex file. 
"""

def putItAllTogether(db: Games):
    plotEverything(db)

def generatePDF():
    generateDocument()


# For reference when testing task 11 and 12 - Please copy any of these available 
# openings. Copying htese will guarantee the correct spelling. 
openings = ["Bird's opening", 'Nimzo-Indian', 'Sicilian', 'QGA', 
'QGD', 'Budapest', "Queen's pawn game", 'French', 'Ruy Lopez', 
'English opening', 'Gruenfeld', 'Reti opening', 'Caro-Kann', 
'QGA, Bogolyubov variation', 'English', 'Modern defence', 
"Queen's Indian", 'Dunst (Sleipner, Heinrichsen) opening', 
'Vienna gambit', 'QGD semi-Slav', "King's Indian, 3.Nf3", 'Petrov', 
"Sicilian, Szen (`anti-Taimanov') variation", 'Sicilian, Szen, hedgehog variation', 
"Queen's gambit declined", "King's Indian", 'KGA', 'Evans gambit', 
'Scotch game', "Two knights defence (Modern bishop's opening)", 'Pirc', 
'Benko gambit', 'Catalan', 'Benoni', "Benko's opening", 
'Bogo-Indian defence', 'Sicilian defence', 
'Trompovsky attack (Ruth, Opovcensky opening)', 'Reti', 'Caro-Kann defence', 
'Robatsch (modern) defence', "Alekhine's defence", 'Benoni defence', 
'Polish (Sokolsky) opening', 'Kevitz-Trajkovich defence', 'Robatsch defence', 
'English, Kramnik-Shirov counterattack', 'Pirc defence', 'Giuoco Piano', 
'QGD Slav defence', 'QGD Slav', "Queen's pawn", "Bishop's opening", 
'Scotch', 'Benko gambit half accepted', 'Catalan opening', 'Ponziani', 
'Benko gambit accepted', 'KP', 'Dutch defence', 'Dutch', 
'Bogo-Indian defence, Gruenfeld variation', "Queen's pawn, Mason variation", 
'Giuoco Pianissimo', "Queen's gambit accepted", 'Four knights', 
'Neo-Gruenfeld, 5.Nf3', 'Scandinavian', 'Neo-Gruenfeld, 6.cd Nxd5, 7.O-O Nb6', 
'Gruenfeld defence', "King's Indian defence", "Queen's Indian accelerated", 
'Nimzovich-Larsen attack', 'Inverted Hanham', 'Old Indian', 
'Neo-Gruenfeld, 6.O-O c6', 'Dutch, 2.Bg5 variation', 'Reti v Dutch', 
'Mieses opening', "Queen's pawn, Mason variation, Steinitz counter-gambit", 
'Philidor', 'Scandinavian (centre counter) defence', 'Centre game', 
"King's Indian defence, 3.Nc3", "Semi-Benoni (`blockade variation')", 
"King's pawn opening", 'Owen defence', 'Sicilian, Chekhover variation', 
'Old Benoni defence', "Queen's bishop game", 'Blumenfeld counter-gambit accepted', 
'Bird', 'Danish gambit', 'Ponziani counter-gambit', 'Blackmar gambit', 
'Two knights defence', "Queen's Pawn", 'Konstantinopolsky opening', 
'Scandinavian defence', 'St. George defence', 'QGD Slav defence, Alekhine variation', 
'Neo-Gruenfeld, 6.O-O, main line', "Levitsky attack (Queen's bishop attack)"]

if __name__ == "__main__":
    main()