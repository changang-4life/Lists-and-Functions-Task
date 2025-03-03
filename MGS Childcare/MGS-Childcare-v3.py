""" Program which will be used by a child daycare centre to keep track of
children throughout the day
Jade Akinbo
14/02/25
v3 - dropoff():
    ⤷  Needs to ask user to input name of a child and then confirm that the
    name has been added to the list
"""

names_list = []

def welcome():
    """ Function that prints a welcome screen and menu selection """
    print()
    print("𐙚‧₊˚📒✏️✩ ₊˚☁️⊹♡ MGS Childcare 𐙚‧₊˚✏️📒✩ ₊˚☁️⊹♡")
    print()
    print("What would you like to do? Please choose your "
                       "action using its corresponding number below:\n")
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

def main():
    """ Main routine """
    choice = welcome()
    if choice == 1:
        dropoff()
    elif choice == 5:
        print("Goodbye!")
    else:
        print("invalid")

main()