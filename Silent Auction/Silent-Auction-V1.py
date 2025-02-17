""" Program for a silent auction
Jade Akinbo
17/02/25
V1
"""

# if reserve not met, else

bid_list = []

def auction():
    """ Function which takes care of a silent function """
    bid_item = input("What is the auction for?: ")
    reserve = float(input("What is the reserve price?: "))

    print()

    print(f"The auction for {bid_item.upper()} has started!")
    print("Enter '0' at anytime to end the auction.")

    print()

    highest_bid = 0

    while True:

        print(f"The highest bid so far is ${highest_bid}.")
        bid = float(input("What is your bid?: "))

        print()

        bid_list.append(bid)

        if bid < max(bid_list):
            while True:
                print("Please enter a higher bid.")
                bid = float(input(">> "))

                if bid == 0:
                    if reserve > highest_bid:
                        print("Sorry, the item did not sell because the "
                            "reserve price was not met.")
                    else:
                        print(f"The auction for {bid_item.upper()} has "
                        f"finished with a bid of ${highest_bid}.")
                    quit()

                if bid > max(bid_list):
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