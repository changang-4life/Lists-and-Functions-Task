""" Program for a silent auction
Jade Akinbo
17/02/25
V2 - Error checks
"""
# to do: number_checker language checking
# 0 doesnt work when in error check?

bid_list = []

def number_checker(number):
    """ Function which error checks number values """
    number_ = ''
    if number == float():
        return number
    while not number_:
        try:
            number_ = float(input(">>  "))
            print()
        except ValueError:
            print("That was not a number value!")
            print()
    return number_

def auction():
    """ Function which takes care of a silent function """
    bid_item = input("What is the auction for?: ")
    reserve = number_checker((input("What is the reserve price? Press ENTER "
                                    "then enter it below: "
                                    "")))

    # ^^^ Takes user input for bid item and reserve price ^^^

    print(f"The auction for {bid_item.upper()} has started!")
    print("Enter '0' at anytime to end the auction.")

    print()

    highest_bid = 0
    # ^^highest bid variable created
    while True:
        print(f"The highest bid so far is ${highest_bid}.")
        bid = number_checker(input("What is your bid? Press ENTER "
                                         "then enter it below: "))

        bid_list.append(bid)

        if bid < max(bid_list):
            # if the bid is not higher than the highest bid user will enter
            # an error check loop

            while True:
                """ Loops which error checks for a valid bid """
                if bid == 0:
                    # if the user wishes to exit the program, ending the
                    # auction
                    return bid
                    break

                if reserve > highest_bid:
                    # program checks if the reserve was met

                    print()
                    print("Sorry, the item did not sell because the "
                        "reserve price was not met.")
                else:
                    print(f"The auction for {bid_item.upper()} has "
                    f"finished with a bid of ${highest_bid}.")
                quit()

                print("Please enter a higher bid.")
                bid = number_checker(float(input("What is your bid? Press "
                                                "ENTER then "
                                        "enter it below:  ")))

                if bid > max(bid_list):
                    # else, if the bid is the highest, the error check loop
                    # breaks
                    highest_bid = bid
                    break

        if bid == max(bid_list):
            highest_bid = bid

        print()

        if bid == 0:
            if reserve > highest_bid:
                print("Sorry, the item did not sell because the reserve "
                      "price was not met.")
            else:
                print(f"The auction for {bid_item.upper()} has finished with a "
                      f"bid of ${highest_bid}.")
            break

auction()