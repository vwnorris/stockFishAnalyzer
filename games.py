from game import *

#Class for a database of chessgames
class Games:
    def __init__(self) -> None:
        self._games : list[Game] = []

    # Getters and setters
    @property
    def games(self):
        return self._games
    
    def addGame(self, game : Game):
        self._games.append(game)

    # Returns how many games are active after a given number of moves
    def howManyActive(self, moves: int) -> int:
        games = 0
        for g in self.games:
            if int(g.plyCount)//2 > moves:
                games += 1
        return games
    # Same for games where Stockfish played with white pieces
    def howManyActiveW(self, moves: int) -> int:
        games = 0
        for g in self.games:
            if int(g.plyCount)//2 > moves and g.white == "Stockfish 15 64-bit":
                games += 1
        return games
    # Same for games where Stockfish played with black pieces
    def howManyActiveB(self, moves: int) -> int:
        games = 0
        for g in self.games:
            if int(g.plyCount)//2 > moves and g.black == "Stockfish 15 64-bit":
                games += 1
        return games
    # Returns the max number of moves in a game in the database
    def maxMoves(self) ->int:
        max = 0
        for i in range(len(self.games)):
            if int(self.games[i].plyCount) > max:
                max = self.games[i].plyCount
        return max
    # Counts the openings, so that we can se which openings are most popular
    def countOpenings(self) -> dict:
        openings: dict = {}
        for g in self.games:
            if g.opening not in openings:
                openings[g.opening] = 1
            else:
                openings[g.opening] += 1
        sortedDict = dict(sorted(openings.items(), key=lambda item: item[1], reverse=True))
        return sortedDict
