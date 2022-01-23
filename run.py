import csv
import requests
import unidecode
import sys

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


# Define the remote URL
# https://raw.githubusercontent.com/Softcatala/catalan-dict-tools/master/resultats/lt/diccionari-dnv.txt
url = "https://raw.githubusercontent.com/Softcatala/catalan-dict-tools/master/resultats/lt/diccionari.txt"
# Send HTTP GET request via requests
data = requests.get(url)
# Convert to iterator by splitting on \n chars
lines = data.text.splitlines()
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
print("S'han trobat {} resultats".format(len(result)))
print(result)


