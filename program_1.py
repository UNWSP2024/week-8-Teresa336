# Programmer: Teresa Fischer
# Date: 10/22/24
# Program #1: Initials

# Write a program that gets a string containing a person's first, middle, and last names, 
# and displays their first, middle, and last initials.  
# For example, if the user enters John William Smith, the program should display J. W. S.

# Add your logic starting on line 11

def initials_generator(personsName):

    personsInitials = ""
    #    Add your logic here
    name_list = personsName.split()
    print('The initals for', personsName, 'are')
    for string in name_list:
        print(string[0].upper(), sep='', end='')
        print('.', sep='', end='')

    return personsInitials.strip()

personsName = input('Enter the users first, middle, and last name:')

initials = initials_generator(personsName)

print(initials)