""" Program which will be used by a child daycare centre to keep track of
children throughout the day
Jade Akinbo
14/02/25
v6 - printroll():
    ⤷ Needs to enable user to check the roll
"""

names_list = []

def welcome():
    """ Function that prints a welcome screen and menu selection """
    print()
    print("𐙚‧₊˚📒✏️✩ ₊˚☁️⊹♡ MGS Childcare 𐙚‧₊˚✏️📒✩ ₊˚☁️⊹♡")
    print()
    print("What would you like to do? Please choose your "
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
    names_list.append(child_name.capitalize())

    if child_name.capitalize() in names_list:
        print("Your child has been added to the roll!")
    print(names_list)

def pickup():
    child_name = input("Please enter the child's name: ")
    child_name = child_name.capitalize()

    if child_name in names_list:
        names_list.remove(child_name)
    else:
        print(f"{child_name} is not on the roll.")

    print(names_list)

def calccost():
    hours = int(input("How many hours would you like to charge for?: "))
    cost = hours * 12
    print(f"For one child staying {hours} hours, it costs ${cost}.")

def printroll():
    print("Here is the roll for today:")
    for student in names_list:
        print(student)

def main():
    """ Main routine """
    while True:
        total_cost = 0
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
        else:
            print("invalid")

main()