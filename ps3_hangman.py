# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''

    done = True
    
    # if any letter form word is not in list give false
    for c in secretWord:
        if(c not in lettersGuessed):
            done = False
            break
    
    return done



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    
    gussedStr = ""
    
    for c in secretWord:
        if(c in lettersGuessed):
            gussedStr += (c + " ")
        else:
            gussedStr += "_ "
            
    return gussedStr



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''

    alpStr = "abcdefghijklmnopqrstuvwxyz"
    alpList = list(alpStr)
    
    #remove letters in input list from complete alphabet list
    for c in lettersGuessed:
        if(c in alpList):
            alpList.remove(c)
    
    return "".join(alpList)

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.
      
    '''
    # string to be used
    greet = "Welcome to the game Hangman!"
    alreadyChoosedStr = "Oops! You've already guessed that letter: "
    goodGuessStr = "Good guess:"
    wrongGuessStr = "Oops! That letter is not in my word: "
    winStr = "Congratulations, you won!"
    looseStr = "Sorry, you ran out of guesses. The word was "
    resultStr = ""  
    seperator = "-----------"
    wordLenInfo = "I am thinking of a word that is " + str(len(secretWord)) + " letters long."
    
    #initial no of guesses and list of guessed Letters
    guess = 8
    lettersGuessed = []
    
    print(greet, wordLenInfo, seperator, sep="\n")
    
    #iterate untill either win or user out of guesses 
    while(not isWordGuessed(secretWord, lettersGuessed) and guess > 0):
       
        gussedChar = ""
        gusseUpdate = ""
        
        print("\nyou have " + str(guess) + " guesses left." )
        print("Available letters:", getAvailableLetters(lettersGuessed))
        gussedChar = input("Please guess a letter: ")
        gussedChar = gussedChar.lower()
        
        #check if guess is wrong or right and if right (already guessed or not)
        if(gussedChar in lettersGuessed):
            gusseUpdate = alreadyChoosedStr 
        else:
            if(gussedChar in secretWord):
                gusseUpdate = goodGuessStr
                lettersGuessed.append(gussedChar)
            else:
                gusseUpdate = wrongGuessStr
                lettersGuessed.append(gussedChar)
                #reduce no. of guesses if guess is wrong 
                guess -= 1
            
        print(gusseUpdate, getGuessedWord(secretWord, lettersGuessed))
        print(seperator)
    
              
    #decide weather user win or loose
    if(isWordGuessed(secretWord, lettersGuessed)):
        resultStr = winStr
    else:
        resultStr = looseStr + secretWord
    
    print(resultStr)
	



secretWord = chooseWord(wordlist).lower()
hangman("y")
