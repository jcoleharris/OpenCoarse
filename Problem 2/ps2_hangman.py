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

def createBlank(guessTup):
    blankWord = ""
    for i in range(len(guessTup)):
        blankWord += guessTup[i]
        blankWord += " "

    return blankWord

        
# end of helper code
# -----------------------------------

# actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program
wordlist = load_words()

# your code begins here!

def hangman(REVEAL = False):
    # Define key variables
    #   word        This is the word choosen
    #   wordTup     Tuple of the word, indexed per character
    #   guessTup    Tuple of the guessed word, initially equal to "_ _ _..." len(wordTup)
    #   letters     string of lowercase letters [a-z]
    
    word = choose_word(wordlist)
    wordTup, guessTup = word_tuple(word)
    letters = string.ascii_lowercase

    # Debug prints
    #print wordTup, guessTup
                                
    print("\n\tLet's play a game of hangman...")
    print("\n\tI will start, please guess the " + str(len(word)) + " letter word I am thinking of?")

    # If the REVEAL vari is True, print the word before the game
    if REVEAL:
        print("\t\t\t\tThe word is: %s" % (word))
        
    tempStr = ""
    guessCounter = 7
    while True:
        blankWord = createBlank(guessTup)
        print("\n\t" + blankWord)
        
        print("You have " + str(guessCounter) + " guess" + tempStr + " left.")
        print("You have these characters: " + letters )

        # Ask for a valid character [a..z]
        # Capitilized characters are converted to lowercase
        while True:
            char = raw_input("Letter ? ")
            if char.isupper():
                print("\tConverting %s to lower-case..." % (char))
                char = char.lower()

            # Test the char for validity or print warning as to why it isn't
            if char in string.ascii_lowercase:
                break
            else:
                print("\t%s is not a letter in %s" % (char,string.ascii_lowercase))

        #print(char,letters)
        if char in letters:
            # Guess is a previously unguessed letter
            if char in wordTup:
                print("\nGood guess!")

                #print(wordTup,guessTup,letters)
                for loc in range(len(wordTup)):
                    if wordTup[loc] == char:
                        wordTup[loc] = "_"
                        guessTup[loc] = char
                        letters = letters.replace(char,"")
                        
                    #print(wordTup,guessTup,letters)
            else:
                print("\tThe character %s is not in the word!" % (char))
                letters = letters.replace(char,"")
                guessCounter -= 1
        else:
            print("\tYou guessed that already... I won't count against you.")
            #guessCounter -= 1

        if "_" not in guessTup:
            print("\n\t%s is the word -- You Win!" % (word.upper()))
            break

        if guessCounter == 0:
            print("\n\tYou Lost!\n\tThe word is: %s" % (word.upper()))
            break
        elif guessCounter >= 1 and guessCounter < 4:
            print("\tWarning you have only %i guess left!" % (guessCounter))

def hangman_wrapper(REVEAL = False):
    while True:
        hangman(REVEAL)

        validResponses = ['y', 'yes', 'n', 'no']
        while True:
            char = raw_input("Play Again? ")
            if char.isupper():
                char = char.lower()
                
            if char in validResponses:
                break

        if char == validResponses[2] or char == validResponses[3]:
            break


# hangman(True) to reveal word before game
hangman_wrapper()

