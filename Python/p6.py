#Martin C
#Oct 10, 2024
def get_day_name(day_number):
    match day_number:
        case 0:
            return "sunday"
        case 1:
            return "monday"
        case 2:
            return "tuesday"
        case 3:
            return "wednesday"
        case 4:
            return "thursday"
        case 5:
            return "friday"
        case 6:
            return "saturday"
        case _:
            return "unacceptable day number"

starting_day= int(input("enter the starting day number (0 through 6; 0 for sunday, 6 for saturday):"))
length_of_stay= int(input("enter the length of your stay:"))
#This is where the calculation happens
return_day=(starting_day+length_of_stay) % 7
return_day_name=get_day_name(return_day)
print(f"you will return on {return_day_name}, day {return_day}")
#program that asks for number (0 to 6), then asks for length of stay in days, and asnwers with the number and day of the week you will return on.