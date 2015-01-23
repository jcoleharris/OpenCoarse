
import re

# Regular Expressions
#  Find Group pairings
#    paren = re.compile('\(.*\)')
#    brack = re.compile('\[.*\]')
#    brace = re.compile('\{.*\}')
#
#  Find Signs
#   signs = re.compile('[+-]')
#   if polyname[0] == "+" or polyname[0] == "-":
#       sign_array = signs.findall(polyname)
#   else:
#       sign_array = ['+'] + signs.findall(polyname)


def split_poly(polyname):
	polyname = polyname.replace(" ","")
	polyFltr = re.compile('[+-]?[.0-9]*\D*\^*[.0-9]*')
	polySplt = polyFltr.findall(polyname)
	return polySplt

def main():
    polyEquation = raw_input("Enter polynomial: ")
    polyEquation = polyEquation.replace(" ","")

    polynomial = split_poly(polyEquation)
    print("You entered: ",polynomial)


main()
