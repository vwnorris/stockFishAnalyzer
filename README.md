# Assignment 2 - Group 8
## Group members:
### Emilia Salvesen Kozarevic and Victor Windsor Torbjørn Norris

## How-To:
* Everything you need to know to test all functionality in the tasks can be found with a guide in main.py. 
* Check out Figures.pdf before starting, to see the results of all the plots and tables. 
* If there is any problem running any part of the code, we will be in the lecture on thursday and we have all dependencies installed locally. 

## Classes described briefly:
(There is also comments in the code explaining the functions)
* Game - The functionality for a chess game. Mostly getters and setters.
* Games - More advanced functionality for a database (list) of chess games.
* Manager - Manages a database of games. 
* TreeNode - The functionality for a tree node. Mostly getters and setters, as well as keeping all information for all relevant games. 
* Tree - The functionality of making a tree by connecting the tree nodes recursively. 
* The folder also contains a lot of images and other files, these are all described in the main.py file. 


## Tasks:

1. __Data structure of games__
<br>
Datastructure for the Game object is in the Game-class in the game.py file. It also contains managing moves. 

2. __Import game from textfile__
<br>
The function for reading a game from a .pgn file is in the saveHandler.py file. It uses regular expressions and returns a list of Game-objects. 

3. __Export game to textfile__
<br>
The function for exporting a game to a .pgn file is also in the saveHandler.py file. It saves a single Game-object to a file, in .pgn format. 

4. __Database__
<br>
The function for exporting several games to a .pgn file is also in the saveHandler.py file. It saves a list of Game-objects to a file, in .pgn format. 

5. __Excel management__
<br>
The functionality for reading a game from excel and writing one to excel can be found in the excelReader.py file. Check out written.xlsx to see the result. 

6. __Create Latex document__
<br>
The functionality for creating a LaTeX document is found in the documentManager.py file. It creates a document with a title, some sections, subsections, paragraphs, tables and figures. 

7. __Extract the number of games won, drawn and lost by Stockfish__
<br>
The functionality for extracting wins, draws and losses for Stockfish is found in the plotters.py file. The result is in the stockFish.png file and also in the final pdf. The function for this is called pltStatistics4Stockfish(). 

8. __Proportion of games still on-ongoing__
<br>
The proportion of games still ongoing after n moves is plotted in the activeGamesLine.png file, and is also inserted in the .tex document. The function that makes, linePlot(), it is found in plotters.py. 
<br>
<br>
The function for getting mean moves and standard deviation for black and white pieces is called getStats(), and is also found in plotters.py. This generates a table table.png which is later inserted in the document. This table is made using pandas. 

9. __Datastructure of tree__
<br>
The datastructure of a tree is a Class called Tree, which contains TreeNode-objects. The Tree class is found in tree.py, and the TreeNode class is found in node.py. Each treeNode contains a list of all Game-objects which follow the same opening moves up to that node. 

10. __Database loading to a tree__
<br>
Loading a database into a Tree is done by loading the database into a Games object and then starting a Tree using the startTree() function and adding the games from the Games-object. 

11. __Opening tree at given depth__
<br>
Printing an opening tree is done with the printOpeningTree() function from plotters.py. This function takes in the amount of moves you want to see, and the opening you want to check out. 

12. __Openings played more than n times__
<br>
The openings played more than n times is printed to a table normalOpenings.png with the function extractPopularOpenings() from plotters.py which takes in the n moves and a database. 

## Assumptions:
* There has been added two linebreaks in the stockfish file so that our readerfuncion can read the first game as well. 

## Testing:
* We have tested all our functionality the entire way, using all the different print functions and the methods in the main.py file. 
