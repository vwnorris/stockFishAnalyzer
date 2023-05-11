import re 

#Class for a ChessGame
class Game:
    def __init__(self, event, site, date, rnd, white, black, result, eco, opening, plyCount, whiteElo, blackElo, moves) -> None:
        self._event : str = event
        self._site : str = site
        self._date : str = date
        self._rnd : str = rnd
        self._white : str = white
        self._black : str = black
        self._result : str = result
        self._eco : str = eco
        self._opening : str = opening
        self._plyCount : str = plyCount
        self._whiteElo : str = whiteElo
        self._blackElo : str = blackElo
        self._moves : str = moves if moves is not None else ""

    #Getters and setters
    @property
    def event(self):
        return self._event

    def setEvent(self, value):
        self._event = value

    @property
    def site(self):
        return self._site

    def setSite(self, value):
        self._site = value

    @property
    def date(self):
        return self._date

    def setDate(self, value):
        self._date = value

    @property
    def rnd(self):
        return self._rnd

    def setRound(self, value):
        self._rnd = value

    @property
    def white(self):
        return self._white

    def setWhite(self, value):
        self._white = value

    @property
    def black(self):
        return self._black

    def setBlack(self, value):
        self._black = value

    @property
    def result(self):
        return self._result

    def setResult(self, value):
        self._result = value

    @property
    def eco(self):
        return self._eco

    def setEco(self, value):
        self._eco = value

    @property
    def opening(self):
        return self._opening

    def setOpening(self, value : str) -> None:
        self._opening = value

    @property
    def plyCount(self):
        return self._plyCount

    def setPlyCount(self, value):
        self._plyCount = value

    @property
    def whiteElo(self):
        return self._whiteElo

    def setWhiteElo(self, value):
        self._whiteElo = value

    @property
    def blackElo(self):
        return self._blackElo

    def setBlackElo(self, value):
        self._blackElo = value

    @property
    def moves(self):
        return self._moves

    def setMoves(self, value):
        self._moves = value

    #Returns a list of the moves made by the white player
    def getWhiteMoves(self) -> list[str]:
        allMoves = self.getMovesAsList()
        whiteMoves: list[str] = []
        for i in range(int(self.plyCount)):
            if i%2 == 0:
                whiteMoves.append(allMoves[i])
        return whiteMoves
    
    #Returns a list of all moves in the game
    def getMovesAsList(self) -> list[str]:
        lst = self.moves.split(" ")
        faen = re.sub(r'\d+\.\s*', "", self.moves)
        lst2 = faen.split(" ")
        lst = [elem for elem in lst if not elem.replace(".", "").isdigit()]
        cleaned_moves = [move for move in lst2 if move != '']
        x = cleaned_moves.pop()
        return cleaned_moves
    
    # Returns a list of full moves, with white and black moves together as objects in the list
    def getDuoMovesAsList(self) -> list[str]:
        duoMoves: list[str] = []
        cleaned_moves = self.getMovesAsList()
        for i in range(len(cleaned_moves)):
            if i%2 == 1:
                string = ""
                string += str(cleaned_moves[i-1])
                string += ", "
                string += str(cleaned_moves[i])
                duoMoves.append(str(string))
        return duoMoves
    
    #Prints a game with all information
    def printAll(self):
        print(f'Event: {self.event}')
        print(f'Site: {self.site}')
        print(f'Date: {self.date}')
        print(f'Round: {self.rnd}')
        print(f'White: {self.white}')
        print(f'Black: {self.black}')
        print(f'Result: {self.result}')
        print(f'Eco: {self.eco}')
        print(f'Opening: {self.opening}')
        print(f'Play Count: {self.plyCount}')
        print(f'White Elo: {self.whiteElo}')
        print(f'Black Elo: {self.blackElo}')
        print(f'Moves: {self.getMovesAsList()}.')