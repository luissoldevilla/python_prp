import random

def main():
    # Dictionary of US states and their capitals
    state_capitals = {"Washington": "Olympia",
                      "Oregon": "Salem",
                      "California": "Sacramento",
                      "Ohio": "Columbus",
                      "Nebraska": "Lincoln",
                      "Colorado": "Denver",
                      "Michigan": "Lansing",
                      "Massachusetts": "Boston",
                      "Florida": "Tallahassee",
                      "Texas": "Austin",
                      "Oklahoma": "Oklahoma City",
                      "Hawaii": "Honolulu",
                      "Alaska": "Juneau",
                      "Utah": "Salt Lake City",
                      "New Mexico": "Santa Fe",
                      "North Dakota": "Bismarck",
                      "South Dakota": "Pierre",
                      "West Virginia": "Charleston",
                      "Virginia": "Richmond",
                      "New Jersey": "Trenton", \
                      "Minnesota": "Saint Paul", "Illinois": "Springfield", \
                      "Indiana": "Indianapolis", "Kentucky": "Frankfort", \
                      "Tennessee": "Nashville", "Georgia": "Atlanta", \
                      "Alabama": "Montgomery", "Mississippi": "Jackson", \
                      "North Carolina": "Raleigh", "South Carolina": "Columbia", \
                      "Maine": "Augusta", "Vermont": "Montpelier", \
                      "New Hampshire": "Concord", "Connecticut": "Hartford", \
                      "Rhode Island": "Providence", "Wyoming": "Cheyenne", \
                      "Montana": "Helena", "Kansas": "Topeka", \
                      "Iowa": "Des Moines", "Pennsylvania": "Harrisburg", \
                      "Maryland": "Annapolis", "Missouri": "Jefferson City", \
                      "Arizona": "Phoenix", "Nevada": "Carson City", \
                      "New York": "Albany", "Wisconsin": "Madison", \
                      "Delaware": "Dover", "Idaho": "Boise", \
                      "Arkansas": "Little Rock", "Louisiana": "Baton Rouge"}
    print(state_capitals)

    statesList = list(state_capitals)

    correct = 0
    incorrect = 0

    again = 'y'

    while (again == 'y'):
        num = random.randint(MIN,MAX)
        state = statesList[num]
        print('\n' + state)
        ans = input("\nEnter the capital of this state: ")
        if (ans == state_capitals[state]):
            correct += 1
            print("Correct")
            again = input("Type y to play again, anything else to stop: ")
        else:
            correct +=1
            print("Incorrect")  
            again = input("Type y to play again, anything else to stop: ")
    
    print("\nYou have",correct,"correct answers")
    print("\nYou have",incorrect,"incorrect answers")

main()