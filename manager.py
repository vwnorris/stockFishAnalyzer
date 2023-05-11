from games import *
from saveHandler import *

# Class for managing a database
class Manager:
    def __init__(self, database: Games = None) -> None:
        if database == None:
            data = Games()
            self._database = data
        else:
            self._database = database
            
    # Add games from a file to the manager
    def addGamesFromFile(self, filename: str):
        games = regexImport(filename)
        for g in games:
            self._database.addGame(g)

    # Add the games from the given .pgn document
    def addStockFishGames(self):
        games = regexImport("Stockfish_15_64-bit.commented.[2600].pgn")
        for g in games:
            self._database.addGame(g)

    # Save a single game by given index of the database to a file "testfile.pgn"
    def saveGame(self, index: int):
        saveGameToPgn(self._database.games[index], "testfile.pgn")

    # Save all games in the database to a file "testfile2.pgn"
    def saveGames(self):
        saveGamesToPgn(self._database.games, "testfile2.pgn")