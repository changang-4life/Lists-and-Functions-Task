""" Program which will be used by a child daycare centre to keep track of
children throughout the day
Jade Akinbo
14/02/25
v7 - Error Checks, calccost() changes,
"""

names_list = []

def welcome():
    """ Function that prints a welcome screen and menu selection """
    print()
    print("𐙚‧₊˚📒✏️✩ ₊˚☁️⊹♡ MGS Childcare 𐙚‧₊˚✏️📒✩ ₊˚☁️⊹♡")
    print()
    print("What would you like to do? Please select your "
                       "action by entering its corresponding number below:\n")
    print("1 - Drop off a child\n"
          "2 - Pick up a child\n"
          "3 - Calculate cost\n"
          "4 - Print roll\n"
          "5 - Exit the system\n")
    choice = int(input(">> "))
    print()
    return choice

def dropoff():
    child_name = input("Please enter the child's name: ")
    if child_name.capitalize() in names_list:
        print(f"{child_name.capitalize()} has been added to the roll "
              "already.")
    else:
        names_list.append(child_name.capitalize())
    print(names_list)


def pickup():
    if names_list == []:
        print("There are no children on the roll right now")
    while names_list != []:
        child_name = input("Please enter the child's name: ")
        if child_name.capitalize() in names_list:
            print(f"{child_name.capitalize()} is already on the roll!")

        if len(names_list[-1]) < 3:
            names_list.remove(child_name.capitalize())
            print("Please enter a name of 3 characters or more.")
            while len(names_list[-1]) < 3:
                child_name = input("Enter the child's name: ")
                if len(names_list[-1]) < 3:
                    print("Please enter a name of 3 characters or more.")

        if child_name.capitalize() in names_list:
            names_list.remove(child_name.capitalize())
            print(f"{child_name.capitalize()} has been removed from the roll.")
        else:
            while child_name.capitalize() not in names_list:
                print(f"{child_name.capitalize()} is not on the roll.")
                user_continue = input("Would you like to re-enter a name? Enter"
                                      " 'Y' for yes or anything else for no"
                                      ": ")
                if user_continue.upper() == 'Y':
                    print()
                    child_name = input("Please enter the child's name: ")
                    if child_name.capitalize() in names_list:
                        names_list.remove(child_name.capitalize())
                        print(f"{child_name.capitalize()} has been removed from"
                              f" the roll.")
                        break
                else:
                    break

    print(names_list)

def calccost():
    if len(names_list) == 0:
        print("There are no children on the roll right now.")
    else:
        hours = int(input("How many hours would you like to charge for?: "))
        cost = len(names_list) * 12 * hours
        print(f"For {len(names_list)} number of children staying {hours} hours, "
              f"it costs ${cost} in total.")

def printroll():
    if names_list == []:
        print("There are no children on the roll right now.")
    else:
        print("Here is the roll for today:")
        for student in names_list:
            print(student)

def main():
    """ Main routine """
    while True:
        choice = welcome()
        if choice == 1:
            dropoff()
        elif choice == 2:
            pickup()
        elif choice == 3:
            calccost()
        elif choice == 4:
            printroll()
        elif choice == 5:
            print("Goodbye!")
            break
        elif choice > 1 or choice < 5:
            while choice < 1 or choice > 5:
                choice = int(
                    input("Please enter a valid number from 1 - 5: "))
                if choice >= 1 and choice <= 5:
                    if choice == 1:
                        print()
                        dropoff()
                    elif choice == 2:
                        print()
                        pickup()
                    elif choice == 3:
                        print()
                        calccost()
                    elif choice == 4:
                        print()
                        printroll()
                    else:
                        print()
                        print("Goodbye!")
                        break

main()