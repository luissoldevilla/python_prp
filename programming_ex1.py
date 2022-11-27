# Write a program that creates a dictionary containing 
# course numbers and the room numbers of the rooms 
# where the courses meet. The dictionary should have
# the following keyvalue pairs:

# 'CS101':'3004'
# 'CS102':'4501'
# 'CS103':'6755'
# 'NT110':'1244'
# 'CM241':'1411'

roomNumbers = {
    'CS101':'3004',
    'CS102':'4501',
    'CS103':'6755',
    'NT110':'1244',
    'CM241':'1411'
}

# The program should also create a dictionary containing course numbers and the names of 
# the instructors that teach each course. The dictionary should have the following key-value pairs:

instructorCourse = {
    'CS101':'Haynes',
    'CS102':'Alvarado',
    'CS103':'Rich',
    'NT110':'Burke',
    'CM241':'Lee'
}

# The program should also create a dictionary containing course numbers and the meeting
# times of each course. The dictionary should have the following key-value pairs:

courseTimes = {
    'CS101':'8:00 a.m.',
    'CS102':'9:00 a.m.',
    'CS103':'10:00 a.m.',
    'NT110':'11:00 a.m.',
    'CM241':'1:00 p.m.'
}

#Prompt the user to enter the course number.

courseNumber = input("Enter the Course Number: ")

#Display the Course Room Number

print("Course's Room Number:",roomNumbers[courseNumber])