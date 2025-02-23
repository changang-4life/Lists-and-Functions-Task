""" Program which keeps track of speeding tickets and alerts officer if there
is an outstanding warrant to arrest the speeder
Jade Akinbo """

names_list = []
fines_list = []
amt_sped_list = []

def speeding_motorists():
    total_fines = 0
    # counts total cost of all fines

    fine_num = 0
    # counts how many fines there are
    while True:
        name = input("Enter name of speeder: ")
        name = name.title()
        names_list.append(name)

        if (name == 'James Wilson' or name == 'Helga Norman' or name ==
                'Zachary Conroy'):
            print(f"\n{name.upper()} - WARRANT TO ARREST")

        amt_sped = int(input("Enter amount over speed limit: "))
        amt_sped_list.append(amt_sped)


        if amt_sped < 10:
            fine = 30
        elif amt_sped >= 10 and amt_sped <= 14:
            fine = 80
        elif amt_sped >= 15 and amt_sped <= 19:
            fine = 120
        elif amt_sped >= 20 and amt_sped <= 24:
            fine = 170
        elif amt_sped >= 25 and amt_sped <= 29:
            fine = 230
        elif amt_sped >= 30 and amt_sped <= 34:
            fine = 300
        elif amt_sped >= 35 and amt_sped <= 39:
            fine = 400
        elif amt_sped >= 40 and amt_sped <= 44:
            fine = 510
        else:
            fine = 630

        fine_num += 1
        total_fines += fine

        print(f"{name} is to be fined ${fine}.\n")

        user_continue = input("Would you like to end? Enter Y to end or "
                              "anything else to continue: ")
        print()

        if user_continue.upper() == 'Y':
            index = -1
            print(f"Total fines: {fine_num}\n")
            for name in names_list:
                print(names_list[index])
                print(f"Amount over limit: {amt_sped_list[index]}")
                print()
                index -= 1
            print(f"Total cost of fines: ${total_fines}")
            break



speeding_motorists()