# Programmer: Teresa Fischer
# Date: 10/22/24
# Program #3: Capital Quiz

# Write a program that creates a dictionary containing the U.S. states as keys, 
# and their capitals as values.  
# The program should then randomly quiz the user by displaying the name of a state 
# and asking the user to enter the state's capital.  
# The program should count of the number of correct and incorrect responses.  
# (You could alternatively use another country and provinces, 
# or countries of the world and capitals).

import random

# Create Dictionary
capitals = {
    "Alabama": "Montgomery", "Alaska": "Juneau", "Arizona": "Phoenix", "Arkansas": "Little Rock", "California": "Sacramento",
            "Colorado": "Denver", "Connecticut": "Hartford", "Delaware": "Dover", "Florida": "Tallahassee", "Georgia": "Atlanta",
            "Hawaii": "Honolulu", "Idaho": "Boise", "Illinois": "Springfield", "Indiana": "Indianapolis", "Iowa": "Des Moines",
            "Kansas": "Topeka", "Kentucky": "Frankfort", "Louisiana": "Baton Rouge", "Maine": "Augusta", "Maryland": "Annapolis",
            "Massachusetts": "Boston", "Michigan": "Lansing", "Minnesota": "St. Paul", "Mississippi": "Jackson", "Missouri": "Jefferson City",
            "Montana": "Helena", "Nebraska": "Lincoln", "Nevada": "Carson City", "New Hampshire": "Concord", "New Jersey": "Trenton",
            "New Mexico": "Santa Fe", "New York": "Albany", "North Carolina": "Raleigh", "North Dakota": "Bismark", "Ohio": "Columbus",
            "Oklahoma": "Oklahoma City", "Oregon": "Salem", "Pennsylvania": "Harrisburg", "Rhode Island": "Providence", "South Carolina": "Columbia",
            "South Dakota": "Pierre", "Tennessee": "Nashville", "Texas": "Austin", "Utah": "Salt Lake City", "Vermont": "Montpelier",
            "Virginia": "Richmond", "Washington": "Olympia", "West Virgina": "Charleston", "Wisconsin": "Madison", "Wyoming": "Cheyenne"
}

# Randomly select and ask question
print("U.S. Capitols Quiz")
states = list(capitals.keys())
points = 0
question_number = 0
while True:
    question_number += 1
    rand_key = random.choice(states)
    answer = capitals[rand_key]
    question = input('What is the capital of %s?' %rand_key)
    if question == capitals[rand_key]:
        print('Correct!')
        points += 1
        print('Your current score is:', points, '/', question_number)

    else:
        print('Incorrect!')
        print('The correct answer is:', capitals[rand_key])
        print('Your current score is:', points, '/', question_number)

    # get another quiz question
    user_input = input('Do you want to answer another question? (Y/N)')

    if user_input == 'Y':
        continue
    else:
        print('Final score:', points, '/', question_number)
        break