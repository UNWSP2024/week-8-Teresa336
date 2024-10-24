# Programmer: Teresa Fischer
# Date: 10/24/24
# Program #5: Course Info

# Write a program that has the user input a bunch of course ID and course name pairs.  
# For example a course ID could be "COS 2005" and the course name could be "Python Programming."   
# Then ask the user for a subject (like "COS"). 
# Finally, the program will display the ID and name of all the courses having that subject.

def course_info():
    course_list = {}
    while True:
        input_id = input("Enter a course ID (or 'done' to finish):")
        if input_id == 'done':
            break
        input_name = input("Enter the course name:")
        course_list[input_id] = input_name

    user_subject = input("Enter a subject (like \"COS\"):")
    print('Course ID and name of all courses containing %s:' %user_subject )
    found = False
    for input_id, input_name in course_list.items():
        if input_id.startswith(user_subject):
            print(input_id, ':', input_name)
            found = True

    if not found:
        print('No courses found for %s' %user_subject)
course_info()