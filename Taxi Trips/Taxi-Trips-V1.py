""" Program which keeps track of details for a taxi
18/02/25
Jade Akinbo
V1
"""
import math

times_list = []
cost_list = []

def taxi_trips():
    name = input("What is the driver's name?: ")
    total_income = 0
    total_time = 0
    avg_time = 0
    avg_cost = 0

    while True:
        trip_confirm = input("Would you like to start a new trip? Enter 'Y' "
                             "for yes or anything else for no: ")

        if trip_confirm.upper() == 'Y':
            trip_time = float(input("How long did the trip take (in "
                                    "minutes)?: "))

            times_list.append(trip_time)
            total_time += trip_time

            cost = (trip_time * 2) + 10
            cost_list.append(cost)

            total_income += cost

            print(f"This trip costs ${cost:.2f}")
            print()

        else:
            if times_list:
                avg_time = total_time / len(times_list)
                avg_cost = total_income / len(cost_list)

            print()
            print("🚕 🚖 🚗 🚘 🚙🚕 🚖 🚗 🚘 🚙🚕 🚖 🚗 🚘 🚙🚕 🚖 🚗 🚘 "
                  "🚙🚕 🚖 🚗 🚘 🚙🚕 🚖 🚗 🚘 🚙")
            print()
            if avg_cost:
                print(f"Driver {name.capitalize()} had 3 trips totalling "
                      f"{total_time:.1f} "
                      f"minutes.\nThe average time of all trips was "
                      f"{avg_time:.1f}.\nThe total income for the day was $"
                      f"{total_income:.2f}.\nThe average cost of all trips was $"
                      f"{avg_cost:.2f}")
            break

taxi_trips()