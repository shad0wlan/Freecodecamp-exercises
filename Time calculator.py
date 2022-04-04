def add_time(start, duration, day=None):
    day_hours = 24
    days_counter = 1
    start_array = start.split()
    am_pm_handler = start_array[1]
    start_time = start_array[0].split(":")
    start_hour = int(start_time[0])
    start_minute = int(start_time[1])
    duration = duration.split(":")
    duration_hours = int(duration[0])
    duration_minutes = int(duration[1])
    final_hour = []
    pm_array = [i for i in range(13, 24)]
    max_minutes = 60
    substractions_hour = start_hour + duration_hours
    substraction_minute = start_minute + duration_minutes

    if substraction_minute >= max_minutes:
        substractions_hour += 1
        substraction_minute = substraction_minute - max_minutes
        if substraction_minute < 10:

            substraction_minute ='{:>02}'.format(substraction_minute).strip()

    while True:
        if substractions_hour > day_hours and (am_pm_handler == "PM" or am_pm_handler == "AM"):
            days_counter += 1
            substractions_hour = substractions_hour - day_hours
            if substractions_hour > 12 and substractions_hour < 24:
                for i in range(11):
                    if substractions_hour == pm_array[i]:
                        substractions_hour = i + 1
                        am_pm_handler = "PM"
        elif substractions_hour > 12 and substractions_hour < 24 and (am_pm_handler == "PM" or am_pm_handler == "AM"):
            for i in range(11):
                if substractions_hour == pm_array[i]:
                    substractions_hour = i + 1
                    days_counter += 1
                    am_pm_handler = "AM"
                    break

        else:
            # am_pm_handler = "PM"

            break


    print(substractions_hour)
    # print(substraction_minute)
    print(substraction_minute)
    print(am_pm_handler)
    print(days_counter)




add_time("3:00 PM", "3:10")
# Returns: 6:10 PM
print("===============")
add_time("11:30 AM", "2:32", "Monday")
# Returns: 2:02 PM, Monday
print("===============")

add_time("11:43 AM", "00:20")
# Returns: 12:03 PM
print("===============")

add_time("10:10 PM", "3:30")
# Returns: 1:40 AM (next day)
print("===============")

add_time("11:43 PM", "24:20", "tueSday")
# Returns: 12:03 AM, Thursday (2 days later)
print("===============")

add_time("6:30 PM", "205:12")
# Returns: 7:42 AM (9 days later)



