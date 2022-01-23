import csv
import os
import sys
import unidecode


# import requests


def eqChar(char1, char2):
    return char1 == char2


def simplyfy(word):
    return unidecode.unidecode(word)


def match(word, mandatory_char, optional_chars):
    simplified_word = simplyfy(word)
    remaining_characters = list(simplified_word)
    remaining_characters = [c for c in remaining_characters if not eqChar(c, mandatory_char)]
    if len(remaining_characters) == len(word):
        # mandatory char not present
        return False

    for optional_char in optional_chars:
        remaining_characters = [c for c in remaining_characters if not eqChar(c, optional_char)]

    # print(remaining_characters)
    return len(remaining_characters) == 0


def listToString(s):
    # initialize an empty string
    str1 = ""

    # traverse in the string
    for ele in s:
        str1 += ele

        # return string
    return str1


# Option 1: Remote URL
# url = "https://raw.githubusercontent.com/Softcatala/catalan-dict-tools/master/resultats/lt/diccionari.txt"
# data = requests.get(url).text

# Option 2: Local file
url = "diccionari.txt"
data = open(url, "r").read()

# Convert to iterator by splitting on \n chars
lines = data.splitlines()
# Parse as CSV object
reader = csv.reader(lines, delimiter=' ')

mandatory_char = "n"
optional_chars = "ceortu"

arguments = sys.argv;
if len(arguments) > 1:
    mandatory_char = arguments[1]
if len(arguments) > 2:
    optional_chars = arguments[2]

print("Lletres: {} + {}".format(mandatory_char, optional_chars))

result = []

for row in reader:
    word = row[0]
    if match(word, mandatory_char, optional_chars):
        result.append(word)

result = list(dict.fromkeys(result))
os.environ["PARAULOGIC_RESULT"] = listToString(result)
print("S'han trobat {} resultats".format(len(result)))
print(result)
