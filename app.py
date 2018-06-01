#import json into python -- type of data in json is dictionary to python
import json
#library for close matching keys
from difflib import get_close_matches

json_data = open("data.json")
data = json.load(json_data)

#create a function that inputs a key and returns a value for that key
def retrieve_from(key):
    key = str(key).lower()
    if key in data:
        return data[key]
    elif key.title() in data:
        return data[key.title()]
    elif key.upper() in data:
        return data[key.upper()]
    close = get_close_matches(key,data.keys())[0]
    ans = input("did you mean {}, (enter a Y or N): ".format(close))
    if ans == "Y" or ans == "y":
        return data[close]
    else:
        print("That word doesn't exist")

#input
word = input("Word: ")
definition = retrieve_from(word)

# converting list into str output
if type(definition) == list:
    for item in definition:
        print(item)
else:
    print(definition)
