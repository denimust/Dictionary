import json
from difflib import get_close_matches
print("Hello Volvanoes")
def definition(word):
    word = word.lower()
    data = json.load(open("data.json"))
    if word in data:  # Return definition if the word was found in the dictionary
        return data[word]
    elif word.title() in data:  # Checking for names of cities etc
        return data[word.title()]
    elif word.upper() in data:  # Checking for abbreviations
        return data[word.upper()]
    else:  # If the word was not found, we are looking for similar words
        suggest = get_close_matches(word, data.keys(), cutoff = 0.8)
        if len(suggest) > 0:  # If a similar word was found, we suggest it to the user
            yes_or_no = input(f"Did you mean {suggest[0]} instead? Enter Y for yes and N for no: ")
            if yes_or_no == "Y":
                return data[suggest[0]]
            elif yes_or_no == "N":
                return "The word you entered does not exist. Please double check it"
            else:
                return "We didn't understand your entry"
        else:  # If no similar words were found, let the user know that it doesn't exist
            return "The word you entered does not exist. Please double check it"

word = input("Enter a word: ")



output = definition(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)