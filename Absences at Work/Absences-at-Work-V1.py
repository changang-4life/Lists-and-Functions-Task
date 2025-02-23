def absences():
    names_list = []
    days_absent_list = []

    while True:
        name = input("What is the employee's name?: ").title()
        absent_num = int(input("How many times have they been away from work in the last year?: "))

        names_list.append(name)
        days_absent_list.append(absent_num)

        user_continue = input("Would you like to end the program? Enter 'Y' for yes, or anything else to continue: ")
        if user_continue.upper() == 'Y':
            break

    # Calculate final results after all input is gathered
    total_absences = sum(days_absent_list)
    average_absences = total_absences / len(days_absent_list) if days_absent_list else 0

    most_absent_list = []
    most_absent_count = 0
    not_absent_list = []
    above_avg_list = []

    for i in range(len(names_list)):
        name = names_list[i]
        absent_num = days_absent_list[i]

        if absent_num == 0:
            not_absent_list.append(name)

        if absent_num > most_absent_count:
            most_absent_list = [name]
            most_absent_count = absent_num
        elif absent_num == most_absent_count:
            most_absent_list.append(name)

        if absent_num > average_absences:
            above_avg_list.append(name)

    # Print final results
    print(f"\nAverage number of days staff were absent: {average_absences:.2f}")

    print("\nPerson(s) with the most days absent:")
    for name in most_absent_list:
        print(f"{name} with {most_absent_count} absences")

    print("\nList of people not absent at all:")
    for name in sorted(not_absent_list):
        print(f"{name}")

    print("\nList of people absent an above average amount of times:")
    for name in sorted(above_avg_list):
        print(f"{name}")

absences()