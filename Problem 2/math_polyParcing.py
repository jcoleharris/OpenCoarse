# Polynomial Parcer
#
#
#

# Define global variables
polynomial = []

# Define debug printing or allow for warning statements:
DEBUG = True
WARNING = True

def printDebug(string):
    if DEBUG:
        print(string)
    return

def printWarning(string):
    if WARNING:
        print(string)
    return



# polyParce parces through a given polynomial, 're-writing' it
#   into a tuple -- polynomial -- of Terms
#
# Each Term is = Coefficient * Variable ^ Exponant
#
def polyParce(polynomial_str):
    # Define variables
    isSign = False
    isCoef = False
    isExpo = False
    isVari = False
    isNewTerm = True
    isDot = False
    char_Sign = ''
    char_Coef = ''
    char_Expo = ''
    char_Vari = ''
    char_Last = 'Start' # Store last char type
    char_FirstVari = '' # Store the FIRST variable, there can only be one!

    poly = 0
    n = 0 # Track characters
    
    # Remove all space-characters
    #   Add end ' ' to single end of polynomial
    polynomial_str = polynomial_str.replace(" ","") + ' '

    # Cycle through each character of the polynomial
    for chars in range(len(polynomial_str)):
        # Grab a character
        char = polynomial_str[chars]
        n = n + 1

        # SIGN
        if char == "+" or char == "-" or char == " ":
            printDebug("Sign = " + char)
            if char_Last == 'Sign' and char != " ":
                # Signs back to back are multiplied to achieve new sign
                temp = int(char + '1') * int(char_Sign + '1')
                printDebug("Fixing Signs!")
                printDebug("char: " + char + ", char_Sign: " + char_Sign + ", new value: " + str(temp))
                if temp == 1:
                    char_Sign = '+'
                else:
                    char_Sign = '-'
            elif char_Last != 'Exponant':
                # TO DO: Signs always start a new Term, so create poly and clear old values
                if isCoef or char_Expo or char_Vari:
                    poly = poly + 1
                    definePolyTerm(poly, char_Sign, char_Coef, char_Vari, char_FirstVari, char_Expo)
                
                # char is a Sign
                isSign = True
                char_Sign = char
                printDebug(str(n) + ": Sign is: " + char)

                printDebug(str(n) + ":\tReseting variables for next Term")
                isCoef = False
                isExpo = False
                isVari = False
                isNewTerm = True
                isDot = False
                char_Coef = ''
                char_Expo = ''
                char_Vari = ''
                char_Last = 'Sign'
            else:
                # If the Sign is first, then it simply is the sign of the first coefficent
                isSign = True
                char_Expo = '-'

        # DOT
        elif char == ".":
            # Check for too many Dots, which is an ERROR
            if checkChar_Dot(poly, char, isDot, isVari):
                # Determine if the Dot belongs to Coefficient or Eponant
                if isVari:
                    # If isVari is True, the dot is the Exponant
                    if char_Expo == '':
                        char_Expo = '0'
                    char_Expo = char_Expo + char
                else:
                    # If isVari is False, the number is the Coefficient
                    if char_Coef == '':
                        char_Coef = '0'
                    char_Coef = char_Coef + char
            else:
                # Too many Dots!
                break
            isDot = True
            
        # EXPONANT
        elif char == "^":
            # start the Exponant
            if isExpo:
                # Exponant already started, ERROR
                printWarning("Char " + str(n) + ": Only one ^ allowed per Term! Stopping.")
                break
            elif char_Last == "Variable" or char_Last == "Digit":
                isExpo = True
            else:
                printWarning("Char " + str(n) + ": Exponant in wrong place! Stopping.")
                break

            char_Last = 'Exponant'
            printDebug(str(n) + ": Exponant!")

        # DIGIT
        elif str.isdigit(char):
            # char is a number, could either be Coefficient or Eponant (?)
            if isSign == False:
                # Sign might not be defined in first Term, if so, assign it
                isSign = True
                char_Sign = '+'
                printDebug(str(n) + ": Assigning Coefficient Sign = +")

            if isVari:
                # If isVari is True, the number is the Exponant
                isExpo = True
                char_Expo = char_Expo + char
                printDebug(str(n) + ": Exponant = " + char_Expo)
            else:
                # If isVari is False, the number is the Coefficient
                isCoef = True
                char_Coef = char_Coef + char
                printDebug(str(n) + ": Coefficient = " + char_Coef)
                
            char_Last = 'Digit'

        # CHARACTER
        elif str.isalpha(char):
            # char is an alpha [a-z] so this is the Variable
            if isSign == False:
                # Sign might not be defined in first Term, if so assign it
                isSign = True
                char_Sign = '+'
                printDebug("Char " + str(n) + ": Assigning Variable Sign = +")
               
            if isVari:
                # If isVari is True, the variable has already been defined
                # Variables are only one character
                printWarning("Char " + str(n) + ": Invalid variable, it must be 1-character!")
                break
            elif isNewTerm and char_FirstVari != '' and char != char_FirstVari:
                # char must be equal to char_LastVari, only 1 variable allowed
                printWarning("Char " + str(n) + ": Multiple variables detected across Terms - only one variable allowed! Stopping.")
                break

            isVari = True
            isDot = False # Reset for Exponant tests
            char_Vari = char
            printDebug(str(n) + ": Variable = " + char_Vari)

            char_Last = 'Variable'
            char_FirstVari = char

        # CATCH ALL
        else:
            printDebug(str(n) + ": Not sure what " + char + " is! Stopping.")
            break
    
    return polynomial


        
def definePolyTerm(poly,char_Sign,char_Coef,char_Vari,char_FirstVari,char_Expo):
# Fix definitions if there are missing parts
    
    if char_Coef != '' and char_Expo != '' and char_Vari == '':
        # The Term is #^# --> Calc
        temp = float(char_Coef) ** int(char_Expo)
        char_Coef = str(temp)
        char_Expo = '1'

    if char_Coef == '':
        char_Coef = '1'
        
    char_Coef = char_Sign + char_Coef
    
    if char_Expo == '':
        char_Expo = '1'
        
    if char_Vari == '':
        if char_FirstVari == '':
            char_Vari = 'x'
        else:
            char_Vari = char_FirstVari
        char_Expo = '0'

    if char_Expo != str(abs(int(float(char_Expo)))):
        printWarning("\tTerms stored in list with index = exponant.")
        printWarning("\tExponants must be possitive Integers only!")
        printWarning("\tCan't process " + char_Expo + "!")
        exit()
    
    polyVar = int(char_Expo)
    polyCoe = float(char_Coef)

    # Print the Term
    #print("\tTerm "+ str(poly) +" = " + char_Coef + char_Vari + "^" + char_Expo)

    polyLocError = False
    try:
        temp = polynomial[polyVar]
    except (TypeError, IndexError):
        polyLocError = True
    
    if polyLocError:
        # The polyVar (char_Expo) is not in polynomial[] => Create the entry
        # First append 0 to empty spots between last loc and desired loc
        polyLen = len(polynomial)
        polyExtend = polyVar - polyLen
        for i in range(polyExtend):
            polynomial.append(0)
        # Append polyCoe as last entry
        polynomial.append(polyCoe)

    else:
        # Entry already exists, add the values and replace
        temp = polynomial[polyVar] + polyCoe
        polynomial[polyVar] = temp
        
    # Debug print
    printDebug("Polynomial = " + str(polynomial))



def checkChar_Dot(poly, char, isDot, isVari):
    if isDot:
        # isDot is reset in SIGN & CHARACTER
        if isVari:
            temp = 'Exponant'
        else:
            temp = 'Coefficient'
        printDebug("Term " + str(poly) + ": Only one . allowed per " + temp + "! Stopping.")
        return False
    return True





    
