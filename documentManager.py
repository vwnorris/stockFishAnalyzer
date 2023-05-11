from tkinter import Label
from pylatex import Document, Section, Subsection, Command, Figure, Package
from pylatex.utils import italic, NoEscape
import os

# Creates the document
def generateDocument():
    #Name of the document
    doc = Document('Figures')

    #Fills the odcument
    def fill_document(doc : Document):
        #First section
        with doc.create(Section('Section one - Figures:')):
            doc.append('The following are figures:')
            #Subsections with figures. 
            with doc.create(Subsection('Statistics over games won, tied and lost')):
                with doc.create(Figure(position='h!')) as fig:
                    fig.append(Command(r' \hspace*{-5cm}'))
                    fig.add_image('stockFish.png', width=NoEscape(r'1.8\textwidth'))
                    fig.add_caption('A plot of Stockfish performance in chess games. In total, with white and with black pieces.')

            with doc.create(Subsection('Lineplot')):
                with doc.create(Figure(position='h!')) as fig:
                    fig.append(Command(r' \hspace*{-4cm}'))
                    fig.add_image('ActiveGamesLine.png', width=NoEscape(r'1.8\textwidth'))
                    fig.add_caption('A plot of active games after x moves. Shows the plot for total games, games played as white by stockfish and as black by stockfish')

            with doc.create(Subsection('Statistics of mean and standard deviation:')):
                with doc.create(Figure(position='h!')) as fig:
                    fig.append(Command(r' \hspace*{-3cm}'))
                    fig.add_image('table.png', width=NoEscape(r'1.4\textwidth'))
                    fig.add_caption('Stats for all games, white games and black games by stockfish')
            
            with doc.create(Subsection('Statistics over most popular openings')):
                with doc.create(Figure(position='h!')) as fig:
                    fig.append(Command(r' \hspace*{-5cm}'))
                    fig.add_image('NormalOpenings.png', width=NoEscape(r'1.8\textwidth'))
                    fig.add_caption('A table with the most popular openings, as well as stats for these')
        #Second section
        with doc.create(Section('Section two - Opening Tree:')):
            doc.append('The following section is a tree for a selected chess opening.')
            #Subsection with a figure
            with doc.create(Subsection('Opening tree')):
                with doc.create(Figure(position='h!')) as fig:
                    fig.append(Command(r' \hspace*{-2cm}'))
                    fig.add_image('OpeningTree.png', width=NoEscape(r'0.7\textwidth'))
                    fig.add_caption('A plot of an opening tree')


    # Add title, author, date and att the title to the document
    doc.preamble.append(Command('title', 'Statistics of chess games played by Stockfish'))
    doc.preamble.append(Command('author', 'Emilia Salvesen Kozarevic and Victor Windsor Torbjørn Norris'))
    doc.preamble.append(Command('date', NoEscape(r'\today')))
    doc.preamble.append(Command('maketitle'))

    fill_document(doc)
    doc.generate_tex()


    #Prints the success and removes the unneccessary files generated by pylatex. 
    print(".tex document made!")
    os.system('pdflatex Figures.tex')
    print(".pdf document made!")
    os.system('rm Figures.log')
    os.system('rm Figures.aux')