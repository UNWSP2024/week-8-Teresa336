# Programmer: Teresa Fischer
# Date: 10/22/24
# Program #2: Word Separator

# Write a program that accepts as input a sentence in which all of the words are run together, 
# but the first character of each word is uppercase.  
# Convert the sentence to a string in which the words are separated by spaces, 
# and the first word starts with an uppercase.  
# For example the string "StopAndSmellTheRoses" would be converted to "Stop and smell the roses."

# Start your changes on line 13

def word_separator(sentence):

    new_sentence = ""
    for i, x in enumerate(sentence):
        if i == 0:
            new_sentence += x
        elif not x.isupper():
            new_sentence += x
        else:
            new_sentence = new_sentence + ' ' + x.lower()

    return new_sentence.strip()

# Example usage

sentence = "StopAndSmellTheRoses"

new_sentence = word_separator(sentence)

print(new_sentence)