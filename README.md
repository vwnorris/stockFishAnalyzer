# Stockfish Analyzer
Welcome to our stockfish chess analyser, created by Emilia Salvesen Kozarevic and Victor Norris! In this project, you'll find a variety of functionality for analyzing chess games, such as importing/exporting games, performing statistics on these, generating plots, opening trees and much more.

## Getting Started
* To test the functionalities provided, refer to the guide in main.py.
* For a visual overview of the results, check out Figures.pdf.
* If you have any questions about the code or encounter any issues running it, don't hessitate to contact me at [vic@norris.no](vic@norris.no)
* To run the full project, you will need the packages in [dependencies](#dependencies)

## Classes and files Overview
* Game: Handles chess game functionality. Includes getters and setters.
* Games: Offers advanced functionality for a database (list) of chess games.
* Manager: Manages a database of games.
* TreeNode: Implements tree node functionality. Contains getters, setters, and relevant game information.
* Tree: Constructs a tree by connecting tree nodes recursively.
* The folder "images" contains images of plots and tables.

## Features
1. **Data structure of games**: Game class in `game.py` file provides the data structure for the Game object, as well as move management.
2. **Import game from text file**: `saveHandler.py` file contains the function for reading a game from a .pgn file. It returns a list of Game objects using regular expressions.
3. **Export game to text file**: `saveHandler.py` also includes the function for exporting a single Game object to a .pgn file.
4. **Database**: `saveHandler.py` has a function for exporting multiple games to a .pgn file, saving a list of Game objects.
5. **Excel management**: `excelReader.py` file offers functionality for reading and writing games from/to Excel. Check `written.xlsx` for the result.
6. **Create LaTeX document**: `documentManager.py` file is responsible for generating a LaTeX document with a title, sections, subsections, paragraphs, tables, and figures.
7. **Stockfish game results**: `plotters.py` file extracts wins, draws, and losses for Stockfish, which are found in `stockFish.png` and the final PDF. The relevant function is `pltStatistics4Stockfish()`.
8. **Proportion of ongoing games**: `activeGamesLine.png` shows the proportion of games still ongoing after n moves. The line plot is generated by the `linePlot()` function in `plotters.py`. Additionally, `getStats()` in the same file produces a table of mean moves and standard deviation for black and white pieces.
9. **Data structure of tree**: The Tree class (`tree.py`) contains TreeNode objects (`node.py`). Each TreeNode holds a list of Game objects sharing the same opening moves up to that node.
10. **Database loading to a tree**: To load a database into a Tree, load it into a Games object and then use the `startTree()` function, adding the games from the Games object.
11. **Opening tree at a given depth**: `printOpeningTree()` function in `plotters.py` displays an opening tree based on the specified number of moves and opening.
12. **Openings played more than n times**: `extractPopularOpenings()` function in `plotters.py` creates a table (`normalOpenings.png`) showing openings played more than n times, given the number of moves and a database.

## Dependencies
To run this project, you'll need the following Python libraries installed:

* graphviz
* matplotlib
* numpy
* pandas
* openpyxl
* pylatex

### Installing Required Packages
To install the required packages, follow these steps:

1. Install `graphviz`, `openpyxl`, and `pylatex` using pip:
```
pip install graphviz openpyxl pylatex
```
2. Install Graphviz, which is a separate software package that `graphviz` library relies on. You can download Graphviz from [the official website](https://graphviz.org/download/), or you can install it using a package manager:

- **On macOS** with [Homebrew](https://brew.sh/):

  ```
  brew install graphviz
  ```


- **On Windows** with [Chocolatey](https://chocolatey.org/):

  ```
  choco install graphviz
  ```

## Installing Conda

To install conda, follow the instructions on the [official Anaconda website](https://www.anaconda.com/products/individual) to download and install the Anaconda distribution, which includes conda and many other useful packages.

Alternatively, you can install Miniconda, which is a smaller distribution that only includes conda and Python:

1. Download Miniconda from the [official Miniconda website](https://docs.conda.io/en/latest/miniconda.html) for your operating system.

2. Follow the installation instructions provided on the website for your operating system.

Once conda is installed, you can create a new environment and install the required packages using the commands mentioned earlier in this guide.

