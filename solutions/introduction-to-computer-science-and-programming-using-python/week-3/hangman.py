# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "./includes/words.txt"

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
    lettersGuessed = [item.lower() for item in lettersGuessed]

    for char in secretWord.lower():
        if char not in lettersGuessed:
            return False

    return True


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    lettersGuessed = [item.lower() for item in lettersGuessed]

    answer = ''
    for char in secretWord.lower():
        answer += ' '

        if char in lettersGuessed:
            answer += char
        else:
            answer += '_'


    return answer

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    lettersGuessed = map(str.lower, lettersGuessed)

    letters = []
    for alpha in 'abcdefghijklmnopqrstuvwxyz':
        if alpha not in lettersGuessed:
            letters.append(alpha)

    return letters
    

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

    Follows the other limitations detailed in the problem write-up.
    '''
    guesses = []
    misses = 0
    isGuessed = False

    print("The secret word contains " + str(len(secretWord)) + " characters.")
    print(getGuessedWord(secretWord, guesses))

    while misses < 9 and len(getAvailableLetters(guesses)) > 0:

        print("Number of guesses remaining: " + str(8 - misses))

        letter = input("Please guess a letter: ")

        if letter.lower() not in guesses and letter.lower() not in secretWord.lower():
            misses += 1

        guesses.append(letter.lower())

        print(getGuessedWord(secretWord, guesses))

        if isWordGuessed(secretWord, guesses):
            isGuessed = True
            break

    msg = ''
    if isGuessed:
        msg = "Word guessed!"
    else:
        msg = "Unlucky, you didn't guess the word."

    print(msg + " It was " + secretWord)


# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
