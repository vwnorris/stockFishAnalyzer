from game import *
import random

# Class for the nodes of the tree
class TreeNode(object):
    def __init__(self, games: list[Game], name: str,  index=0, children=None) -> None:
        self._id = random.randint(0,1000)
        self._nodeName: str = name + str(index)+str(self._id) if name is not None else "Start"
        self._name: str = name if name is not None else "Start"
        self._children = []
        self._games: list[Game] = games
        self._index = index
        self._leaf = True if self._children is None else False

    @property
    def children(self):
        return self._children
    
    @children.setter
    def children(self, value):
        self._children = value
    
    @property
    def games(self):
        return self._games
    
    @games.setter
    def games(self, value):
        self._games = value
    
    @property
    def index(self):
        return self._index
    
    @index.setter
    def index(self, value):
        self._index = value
    
    @property
    def leaf(self):
        return self._leaf
    
    @leaf.setter
    def leaf(self, value):
        self._leaf = value

    # Returns the win percentage for the black player
    def getWhiteWinPercentage(self):
        wins = 0
        total = 0
        for g in self.games:
            if g.result == '1-0':
                wins += 1
            total += 1
        return round(wins/total*100, 2)

    # Returns the win percentage for the white player
    def getBlackWinPercentage(self):
        wins = 0
        total = 0
        for g in self.games:
            if g.result == '0-1':
                wins += 1
            total += 1
        return round(wins/total*100,2)

    # Returns the amount of games ending in a tie
    def getTiePercentage(self):
        ties = 0
        total = 0
        for g in self.games:
            if g.result == '1/2-1/2':
                ties += 1
            total += 1
        return round(ties/total*100, 2)

    # Checks the next possible moves in the databse, and returns the children of the current node
    def makeChildren(self)->list:
        if self.index % 2 == 0:
            color = "White"
        else:
            color = "Black"
        nextMoves = []
        nextNodes = []
        for i in range(len(self.games)):
            if self.games[i].getMovesAsList()[self.index] not in nextMoves:
                nextMoves.append(self.games[i].getMovesAsList()[self.index])
        for i in range(len(nextMoves)):
            games = []
            for j in range(len(self.games)):
                if self.games[j].getMovesAsList()[self.index] == nextMoves[i]:
                    games.append(self.games[j])
            newIndex = self.index + 1
            newNode = TreeNode(games, nextMoves[i], newIndex)
            nextNodes.append(newNode)
            self.children.append(newNode)
        return nextNodes