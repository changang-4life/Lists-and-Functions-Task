""" Program which will be used by a child daycare centre to keep track of
children throughout the day
Jade Akinbo
14/02/25
v2 - welcome():
    ⤷ Needs to have a welcome screen and present the user with a menu selection
"""

names_list = []

def welcome():
    """ Function that prints a welcome screen and menu selection """
    print()
    print("𐙚‧₊˚📒✏️✩ ₊˚☁️⊹♡ Welcome to MGS Childcare 𐙚‧₊˚✏️📒✩ ₊˚☁️⊹♡")
    print()
    print("What would you like to do? Please choose your "
                       "action using its corresponding number below:\n")
    print("1 Drop off a child\n"
          "2 Pick up a child\n"
          "3 Calculate cost\n"
          "4 Print roll\n"
          "5 Exit the system\n")
    choice = int(input(">> "))
    print()
    return choice

def main():
    """ Main Routine """
    choice = welcome()

main()