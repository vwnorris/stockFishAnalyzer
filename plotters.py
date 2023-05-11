import math
import graphviz
import matplotlib.pyplot as plt
from games import *
import numpy as np
from treeNode import *
from tree import *
import pandas as pd
from manager import *

# Plots every graph
def plotEverything(db: Games):
    printOpeningTree(4, "Bird's opening")
    extractPopularOpenings(100, db)
    getStats(db)
    linePlot(db, 150)
    pltStatistics4Stockfish(db)

# Prints a tree of a given opening over a given amount of moves
def printOpeningTree(moves: int, opening: str):
    db = Games()
    m = Manager(db)
    m.addStockFishGames()

    tree = Tree()
    movesList = []
    for p in db.games:
        if p.opening == opening:
            movesList.append(p)

    tree.startTree(movesList)

    makeGraphvizTree(tree, moves)
    printStatsForOpening(opening, db)

# Makes a tree of n moves
def makeGraphvizTree(tree: Tree, moves: int):
    graph2 = graphviz.Digraph()
    graph = graphviz.Digraph()

    def choseColor(index) -> str:
        if index == 0:
            return "#6495ed"
        if index % 2 == 0:
            return "grey"
        else: 
            return "white"

    #Calculates the win percentages for each node
    def xValues(node: TreeNode)->str:
        if node.index != 0:
            return f'WP White: {m.getWhiteWinPercentage()}%\nTies: {m.getTiePercentage()}%\nWP Black: {m.getBlackWinPercentage()}%\nGames: {len(m.games)}'
        else:
            return ""

    tree.getNMoves(moves)

    #Adds the nodes to the tree
    for m in tree._treeNodes:
        graph2.node(m._nodeName, label = m._name, xlabel=f'{xValues(m)}', fontsize="10", fillcolor = f"{choseColor(m.index)}", style = "filled")

    #Adds the edges to the tree
    for e in(tree._treeNodes):
        for c in e.children:
            if c._index <= moves:
                graph2.edge(e._nodeName, c._nodeName)
    
    graph2.graph_attr['nodesep'] = '2'
    graph2.graph_attr['rankdir'] = "LR"
    graph.graph_attr['dpi'] = '800'

    graph2.render('images/OpeningTree', format='png')
    plt.show()

# Prints a table of the most popular openings, given an amount of times the openings has to have been played
def extractPopularOpenings(n: int, games: Games):
    openings = []
    openingsCount = {}
    openingsTies = {}
    openingsWinsW = {}
    openingsWinsB = {}

    # makes dictionaries of openings for different info
    for p in games.games:
        if p.opening not in openings:
            openings.append(p.opening)
            openingsCount[p.opening] = 0
            openingsTies[p.opening] = 0
            openingsWinsW[p.opening] = 0
            openingsWinsB[p.opening] = 0

        openingsCount[p.opening] += 1

        if p.result == "1-0":
            openingsWinsW[p.opening] += 1
        elif p.result == "1/2-1/2":
            openingsTies[p.opening] += 1
        else:
            openingsWinsB[p.opening] += 1

    mostUsedOpenings = []
    for k, v in openingsCount.items():
        if v >= n:
            mostUsedOpenings.append(k)
    print(openingsCount)

    data = {
    'Color': ['White Wins', 'Black Wins', 'Ties'],
    }
    for o in mostUsedOpenings:
        data[o+" - " +str(openingsCount[o])] = [openingsWinsW[o], openingsWinsB[o], openingsTies[o]]


    df = pd.DataFrame(data)
    print(df)
    
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.axis('off')
    ax.axis('tight')
    ax.table(cellText=df.values, colLabels=df.columns, loc='center')

    # Save table as PNG
    plt.savefig('images/NormalOpenings.png', dpi=1000)
    plt.show()

# Prints the stats of the openings, with win percentages for white, black and ties
def printStatsForOpening(opening: str, db: Games):
    #Checking the statistics of the different openings. Then sorted. 
    openings = []
    openingsCount = {}

    openingsTies = {}
    openingsWinsW = {}
    openingsWinsB = {}

    for p in db.games:
        if p.opening not in openings:
            openings.append(p.opening)
            openingsCount[p.opening] = 0
            openingsTies[p.opening] = 0
            openingsWinsW[p.opening] = 0
            openingsWinsB[p.opening] = 0

        openingsCount[p.opening] += 1

        if p.result == "1-0":
            openingsWinsW[p.opening] += 1
        elif p.result == "1/2-1/2":
            openingsTies[p.opening] += 1
        else:
            openingsWinsB[p.opening] += 1
    print('\n')
    print(f'Opening: {opening}')
    print(f'Win percentage for white: {round(openingsWinsW[opening]/openingsCount[opening],3)}')
    print(f'Win percentage for black: {round(openingsWinsB[opening]/openingsCount[opening],3)}')
    print(f'Percentage of ties: {round(openingsTies[opening]/openingsCount[opening],3)}')
    print('\n')

# Returns stats for mean and standard deviation in a table for a list of games. 
def getStats(games: Games):
    #Mean of total games
    totalMoves: int = 0
    for g in games.games:
        totalMoves += int(g.plyCount)//2

    totalMean: float = totalMoves / len(games.games)
    #Mean of white games
    whiteMoves: int = 0
    totalWhite: int = 0
    for g in games.games:
        if g.white == "Stockfish 15 64-bit":
            whiteMoves += int(g.plyCount)//2
            totalWhite += 1
    print(f'Total white wins: {whiteMoves}, total white games: {totalWhite}')
    whiteMean: float = whiteMoves / totalWhite
    #Mean of black games
    blackMoves: int = 0
    totalBlack: int = 0
    for g in games.games:
        if g.black == "Stockfish 15 64-bit":
            blackMoves += int(g.plyCount)//2
            totalBlack += 1

    blackMean: float = blackMoves / totalBlack
    #stdv of all games
    squaredDiffs = []
    for g in games.games:
        squaredDiffs.append(((int(g.plyCount)//2)-totalMean)**2)
    
    sumDiffsSquared = sum(squaredDiffs)
    variance = sumDiffsSquared / len(games.games)

    stDv = math.sqrt(variance)
    #stdv of white games
    squaredDiffsWhite = []
    for g in games.games:
        if g.white == "Stockfish 15 64-bit":
            squaredDiffsWhite.append(((int(g.plyCount)//2)-whiteMean)**2)
    
    sumDiffsSquaredWhite = sum(squaredDiffsWhite)
    varianceW = sumDiffsSquaredWhite / totalWhite

    stDvWhite = math.sqrt(varianceW)

    #stdv of black games
    squaredDiffsBlack = []
    for g in games.games:
        if g.black == "Stockfish 15 64-bit":
            squaredDiffsBlack.append(((int(g.plyCount)//2)-blackMean)**2)
    
    sumDiffsSquaredBlack = sum(squaredDiffsBlack)
    varianceB = sumDiffsSquaredBlack / totalBlack

    stDvBlack = math.sqrt(varianceB)

    #Plot in pandas
    data = {
    'Color': ['Total', 'White', 'Black'],
    'Mean': [round(totalMean, 3), round(whiteMean, 3), round(blackMean, 3)],
    'Standard Deviation': [round(stDv, 3), round(stDvWhite,3), round(stDvBlack, 3)]
    }

    df = pd.DataFrame(data)
    print(df)

    fig, ax = plt.subplots()
    ax.axis('off')
    ax.axis('tight')
    ax.table(cellText=df.values, colLabels=df.columns, loc='center')

    # Save table as PNG
    plt.savefig('images/StatsTable.png')

    #Simple string returned if needed.
    return f"Mean is {round(totalMean, 3)}, and standard deviation is: {round(stDv,3)}"
    
# Plots a line of active games given a limit. 
def linePlot(games: Games, times: int):
    #Total active games, black games and white games
    stats = np.zeros(times)
    statsW = np.zeros(times)
    statsB = np.zeros(times)
    for i in range(times):
        stats[i] = games.howManyActive(i)
        statsW[i] = games.howManyActiveW(i)
        statsB[i] = games.howManyActiveB(i)

    # Create a simple line plot
    x = np.linspace(0, times, times)
    fig, ax = plt.subplots(figsize=(20, 7))
    plt.plot(x, stats, label='Total')
    plt.plot(x, statsW, label='White')
    plt.plot(x, statsB, label='Black')
    plt.title(f"Activity after {times} moves")
    plt.xlabel("Moves made")
    plt.ylabel("Active games")
    plt.legend() 
    plt.savefig("images/ActiveGamesLine.png", dpi=300)
    plt.show()

# Plots the win stats for stockfish. 
def pltStatistics4Stockfish(games: Games ):
    # Could also set total wins to white wins + black wins and so forth,
    # but this way you make it more robust.
    StockfishWins = 0
    stockfishLosses = 0
    stockfishTies = 0
    stockfishBlack = 0
    stockfishWhite = 0 
    whiteTies = 0
    whiteLosses = 0
    blackTies = 0
    blackLosses = 0
    for g in games.games:
        if "Stockfish" in g.white and g.result == ("1-0"):
            StockfishWins += 1
            stockfishWhite += 1
        elif "Stockfish" in g.white and g.result == ("1/2-1/2"):
            whiteTies += 1
            stockfishTies += 1
        elif "Stockfish" in g.white and g.result == ("0-1"):
            whiteLosses += 1
            stockfishLosses += 1
        elif "Stockfish" in g.black and g.result == "0-1":
            StockfishWins += 1
            stockfishBlack += 1
        elif "Stockfish" in g.black and g.result == ("1/2-1/2"):
            blackTies += 1
            stockfishTies += 1
        elif "Stockfish" in g.black and g.result == ("1-0"):
            blackLosses += 1
            stockfishLosses += 1


    data = {"Stockfish\nWins": StockfishWins,
            "Stockfish\nTies": stockfishTies,
            "Stockfish\nLosses": stockfishLosses,
            "Stockfish\nWhite Wins": stockfishWhite,
             "Stockfish\nWhite Ties": whiteTies,
            "Stockfish\nWhite Losses": whiteLosses,
            "Stockfish\nBlack Wins": stockfishBlack,
            "Stockfish\nBlack Ties": blackTies,
            "Stockfish\nBlack Losses": blackLosses}

    fig, ax = plt.subplots(figsize=(28, 10))
    ax.bar(data.keys(), data.values())
    ax.tick_params(axis='x', labelsize=14)

    plt.xlabel("Results", fontsize = 20)
    plt.ylabel("Number of games")
    plt.title("Stockfish performance in chess games")
    plt.savefig("images/stockFish.png", dpi=300)

    plt.show()

    return data
