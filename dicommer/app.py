import datetime
import os
import sys, json

# Read data from stdin


def read_in():
    lines = sys.stdin.readlines()
    return json.loads(lines[0])


serverResponse = read_in()
inputFile = ""  # static value to be replaced
for txt in serverResponse:
    inputFile += txt

# inputPdf = "en.jpg"

inputLanguage = "English"  # static value to be replaced
# print(os.listdir())
location = "dicommer/downloads/"
outputTiff = str(datetime.datetime.now().timestamp())
outputText = str(datetime.datetime.now().timestamp()) + "output"

verifierCounter = 0


strings = "magick mogrify -path outputs -format PNG -colorspace gray -auto-level *.dcm"
convertCommand = "magick mogrify -path outputs -format PNG -colorspace gray -auto-level " + location + inputFile

print(convertCommand)
print("=============")
os.system(convertCommand)




