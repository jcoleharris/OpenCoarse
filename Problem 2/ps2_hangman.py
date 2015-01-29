# 6.00 Problem Set 3
# 
# Hangman
#


# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

def word_tuple(word):
    tup = []
    guess = []
    for i in range(len(word)):
        tup.append(word[i])
        guess.append("_")

    return tup, guess

def define_tuple(number=0, default=' ', sliceDefault=False):
    tup = []
    if sliceDefault:
        for i in range(len(default) - 1):
            tup.append(default[i])
    else:
        for i in range(number - 1):
            tup.append(default)
            
    return tup


# end of helper code
# -----------------------------------

# actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program
wordlist = load_words()
guessCounter = 7

# your code begins here!

def main():
    word = choose_word(wordlist)
    wordTup, guessTup = word_tuple(word)
    print word, wordTup, guessTup

    letters = "abcdefghijklmnopqrstuvwxyz"
    guessLetters = define_tuple(default=letters, sliceDefault=True)
    print(letters, guessLetters)
                                
    print("\n\tLet's play a game of hangman...")
    print("\n\tI will start, please guess the " + str(len(word)) + " letter word I am thinking of?")
    print("\n")

    tempStr = ""
    while True:
        if guessCounter > 1:
            tempStr = "es"
        print("You have " + str(guessCounter) + " guess" + tempStr + " left.")
        print("You have these characters: " + letters )
        break
    





main()

