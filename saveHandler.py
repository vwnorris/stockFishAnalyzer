from games import *
from game import *
import re

# Regex import function that imports all games from a given .pgn file and returns a list of Game - objects
def regexImport(filename: str) -> list[Game]:
    games = []
    with open(filename) as file:
        gameNr = 0
        # read the file as a single string
        pgn_str = file.read()
        # split the string into individual games using the regex pattern
        game_strs = re.findall(r'\n\n(\[.*?\].*?(?=\n\n|\Z))', pgn_str, flags=re.DOTALL)
        moves_strs = re.findall(r'\n\n(1.*?(1-0|1/2-1/2|0-1).*?(?=\n\n|\Z))', pgn_str, flags=re.DOTALL)
        for game_str in game_strs:
            headers = dict(re.findall(r'\[([A-Za-z0-9_]+)\s+"(.*?)"\]', game_str))
            event = headers.get('Event', 'Unknown')
            site = headers.get('Site', 'Unknown')
            date = headers.get('Date', 'Unknown')
            rnd = headers.get('Round', 'Unknown')
            white = headers.get('White', 'Unknown')
            black = headers.get('Black', 'Unknown')
            result = headers.get('Result', 'Unknown')
            eco = headers.get('ECO', 'Unknown')
            opening = headers.get('Opening', 'Unknown')
            plyCount = headers.get('PlyCount', 'Unknown')
            whiteElo = headers.get('WhiteElo', 'Unknown')
            blackElo = headers.get('BlackElo', 'Unknown')
            # Extracts the moves using the regex pattern
            moves_match = moves_strs[gameNr]
            gameNr += 1
            if moves_match is not None:
                moves_str = re.sub(r'(\{[^}]+\})|\\n', '', str(moves_match))[2:-9]
            else:
                moves_str = ''
            # create a Game object and add it to the list
            game_obj = Game(event, site, date, rnd, white, black, result, eco, opening, plyCount, whiteElo, blackElo, moves_str)
            games.append(game_obj)
    return games

# Saves a single game to a .pgn file
def saveGameToPgn(game: Game, filename: str) -> None:
    with open(filename, 'w') as file:
        file.write(f'[Event "{game.event}"]\n')
        file.write(f'[Site "{game.site}"]\n')
        file.write(f'[Date "{game.date}"]\n')
        file.write(f'[Round "{game.rnd}"]\n')
        file.write(f'[White "{game.white}"]\n')
        file.write(f'[Black "{game.black}"]\n')
        file.write(f'[Result "{game.result}"]\n')
        file.write(f'[ECO "{game.eco}"]\n')
        file.write(f'[Opening "{game.opening}"]\n')
        file.write(f'[PlyCount "{game.plyCount}"]\n')
        file.write(f'[WhiteElo "{game.whiteElo}"]\n')
        file.write(f'[BlackElo "{game.blackElo}"]\n')
        file.write("\n")
        file.write(f'{game.moves}')
    print("Saved successfully!")

# Saves a list of Game - objects to a .pgn file. 
def saveGamesToPgn(games: list[Game], filename: str)-> None:
    with open(filename, 'w') as file:
        for game in games:
            file.write(f'[Event "{game.event}"]\n')
            file.write(f'[Site "{game.site}"]\n')
            file.write(f'[Date "{game.date}"]\n')
            file.write(f'[Round "{game.rnd}"]\n')
            file.write(f'[White "{game.white}"]\n')
            file.write(f'[Black "{game.black}"]\n')
            file.write(f'[Result "{game.result}"]\n')
            file.write(f'[ECO "{game.eco}"]\n')
            file.write(f'[Opening "{game.opening}"]\n')
            file.write(f'[PlyCount "{game.plyCount}"]\n')
            file.write(f'[WhiteElo "{game.whiteElo}"]\n')
            file.write(f'[BlackElo "{game.blackElo}"]\n')
            file.write("\n")
            file.write(f'{game.moves}\n\n')
    print("Games saved successfully!")