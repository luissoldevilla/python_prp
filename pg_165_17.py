print("Reboot computer and try to connect.\n(Y/N) Enter Y for yes or N for no.")

answer = input("Did that fix the problem? ")

if answer == "Y" or answer == "y" or answer == "n" or answer == "N":
    if answer == "n" or answer == "N":
        print("Reboot the router.")
        answer = input("Did that fix the problem? ")

        if answer == "Y" or answer == "y" or answer == "n" or answer == "N":
            if answer == "n" or answer == "N":
                print("Make sure the cables are plugged in firmly.")
                answer = input("Did that fix the problem? ")

                if answer == "Y" or answer == "y" or answer == "n" or answer == "N":
                    if answer == "n" or answer == "N":
                        print("Move the router to a new location")
                        answer = input("Did that fix the problem? ")

                        if answer == "Y" or answer == "y" or answer == "n" or answer == "N":
                            print("you need  a new router")
                        else:
                            print("Please enter ", Y ," for yes or ", N," for no.\n Rerun program and try again.")
                    else:
                        print("Please enter ",Y," for yes or ",N," for no.\n Rerun program and try again.")