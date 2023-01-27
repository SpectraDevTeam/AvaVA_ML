import difflib

# list of words
commandslist = ["end", "flip", "joke", "roll", "timer", "systime", "add", "subtract", "multiply", "divide", "search", "image", "app"]

# check if a word is synonym of input word
input_word = input("Word: ")
similar_word = difflib.get_close_matches(input_word, commandslist, cutoff=0.25)
print(similar_word)