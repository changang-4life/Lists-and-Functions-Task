""" Program which allows staff to borrow a vehicle for the day and keeps
track of which vehicles have already been booked
Jade Akinbo
V1
"""

suzuki_van_seats = 2
toyota_corolla_seats = 4
honda_crv_seats = 4
suzuki_swift_seats = 4
mitsubishi_airtrek_seats = 4
nissan_dc_ute = 4
toyota_pervia_seats = 7
toyota_hi_ace = 12

seats_list = [2,4,4,4,4,4,7,12]
vehicles_booked = []
booker_list = []

car_list = ["No. 1  - Suzuki Van  - 2 seater", "No. 2 - Toyota Corolla - 4 "
"seater", "No. 3 - Honda CRV - 4 seater", "No. 4 - Suzuki Swift - 4 seater",
"No. 5 - Mitsubishi Airtrek - 4 seater", "No. 6 - Nissan DC Ute - 4 seater",
"No. 7 - Toyota Previa - 7 seater", "No. 8 - Toyota Hi Ace - 12 seater",
"No. 9 - Toyota Hi Ace - 12 seater "]

car_list_indx = ["Suzuki Van", "Toyota Corolla", "Honda CRV", "Suzuki Swift",
              "Mitsubishi Airtrek", "Nissan DC Ute", "Toyota Previa",
              "Toyota Hi Ace", "Toyota Hi Ace"]

def vehicle_booking_system():
    not_enough = (' ^^ NOTE: The car listed above this message does not have '
                  'enough seats.\n')
    while True:
        user_seats = int(input("\nPlease enter the number of seats required "
                               "(Type -1 to quit): "))
        if user_seats != -1:
            if user_seats < min(seats_list) or user_seats > max(seats_list):
                print(f"Sorry, there are currently vehicles with seats ranging "
                      f"from {min(seats_list)} to {max(seats_list)}.\n")
                continue

            print('VEHICLE NUMBER  - MODEL  -  NO. SEATS\n')

            index = 0
            for car in car_list:
                print(car)
                if user_seats > seats_list[index]:
                    print(not_enough)
                    index += 1

            name = input("\nEnter your name: ")
            name = name.title()
            car_picked = int(input("Please enter car to book by entering its "
                                   "corresponding number: "))

            print(f"{car_list_indx[car_picked - 1]} booked by {name}")

            booker_list.append(name)
            vehicles_booked.append(car_list[car_picked - 1] + ' - ' + 'Booked '
            'by: ' + name)

        else:
            print("\nVEHICLES BOOKED TODAY")
            for bookings in vehicles_booked:
                print(bookings)
            break

vehicle_booking_system()
