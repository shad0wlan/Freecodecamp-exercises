def add_time(start, duration, day=None):
    # Registering working variables

    day_hours = 24
    days_counter = 0
    days_array = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    if day is not None and day.capitalize() not in days_array:
        return 'Enter a valid day please.'

    start_array = start.split()

    # Array validation

    # Hour format validation

    am_pm_handler = start_array[1]

    if am_pm_handler.upper() not in ["AM", "PM"]:
        return 'Please use a valid hour identifier "AM or PM'
    elif ":" not in start_array[0]:
        return 'Missing hour divider ":"'

    start_time = start_array[0].split(":")

    if not start_time[0].isdigit():
        return 'Only numeric values between 1 - 12 accepted'
    elif int(start_time[0]) <= 0 or int(start_time[0]) > 12:
        return 'Enter a valid hour between 1 - 12'

    start_hour = int(start_time[0])

    if not start_time[1].isdigit():
        return 'Only numeric values between 0 - 59 accepted'
    elif int(start_time[0]) < 0 or int(start_time[0]) > 59:
        return 'Enter a valid minute between 0 - 59'

    start_minute = int(start_time[1])

    # Duration format validation

    if ":" not in duration:
        return 'Missing duration divider ":"'
    duration = duration.split(":")

    if not (duration[0].isdigit()):
        return 'Only numeric values accepted higher than or equal to zero'
    elif int(duration[0]) < 0 or int(duration[1]) < 0:
        return 'Only values higher than or equal to zero accepted'

    duration_hours = int(duration[0])
    duration_minutes = int(duration[1])
    pm_array = [i for i in range(13, 24)]
    max_minutes = 60
    substractions_hour = start_hour + duration_hours
    substraction_minute = start_minute + duration_minutes

    # Manipulating AM and PM based on calculations substaction calculations
    while True:
        if duration_hours == 00 and duration_minutes == 00:
            break
        elif start_hour < 12 and ((am_pm_handler == "AM" and substractions_hour < 24)
                                  or (am_pm_handler == "PM" and substractions_hour < 12)):
            am_pm_handler = "PM"
            break
        elif am_pm_handler == "AM" and substractions_hour <= 26:
            break
        else:
            am_pm_handler = "AM"
            days_counter += 1
            break

    # Increasing days counter if calculations exceeds a single day and hours manipulation
    while substractions_hour > day_hours:
        if substractions_hour > day_hours:
            substractions_hour = substractions_hour - day_hours
            days_counter += 1
            continue

    # changing time format 12-hour format based on array

    else:
        if 12 < substractions_hour < 24:
            for i in range(11):
                if substractions_hour == pm_array[i]:
                    substractions_hour = i + 1

    # increasing hour per 1 if substaction of minutes exceed max minutes / hour and decimal formatting

    if substraction_minute >= max_minutes:
        substractions_hour += 1
        substraction_minute = substraction_minute - max_minutes
        substraction_minute = '{:>02}'.format(substraction_minute).strip()
    else:
        substraction_minute = '{:>02}'.format(substraction_minute).strip()

    # constructing main hour array and creating working variable

    final_hour_array = [str(substractions_hour), ":", str(substraction_minute), " ", am_pm_handler]
    new_time = "".join(final_hour_array)

    # manipulating outcome based on days passed if user hasn't entered any day

    if day is None:
        if days_counter == 0:
            return new_time.rstrip()
        elif days_counter == 1:
            new_time += f' (next day)'
            return new_time.rstrip()
        else:
            new_time += f' ({days_counter} days later)'
            return new_time.rstrip()

    # if day is entered, different outcome returned based on value

    else:
        if day.capitalize() in days_array:
            day_string = day.capitalize()
            if days_counter == 0:
                new_time += f', {day_string}'
                return new_time.rstrip()
            elif days_counter == 1:
                try:
                    get_day_index = days_array.index(day_string) + 1
                    day_string = days_array[get_day_index]
                except IndexError:
                    day_string = days_array[0]
                new_time += f', {day_string} (next day)'
                return new_time.rstrip()
            else:
                get_day_index = days_array.index(day_string) + days_counter
                try:
                    day_string = days_array[get_day_index]
                except IndexError:
                    day_string = days_array[get_day_index % len(days_array)]
                new_time += f', {day_string} ({days_counter} days later)'
                return new_time.rstrip()

    return


print(add_time("2:59 AM", "24:00", "saturday"))
# Returns: 6:10 PM

print(add_time("11:30 AM", "2:32", "Monday"))
# Returns: 2:02 PM, Monday

print(add_time("11:43 AM", "00:20", "Monday"))
# Returns: 12:03 PM

print(add_time("10:10 PM", "3:30", "Sunday"))
# Returns: 1:40 AM (next day)

print(add_time("11:43 PM", "24:20", "Monday"))
# Returns: 12:03 AM, Thursday (2 days later)

print(add_time("6:30 PM", "205:12", "Friday"))
# Returns: 7:42 AM (9 days later)

print(add_time("8:16 PM", "466:02", "Wednesday"))
# Returns: 6:18 AM (20 days later)

print(add_time("5:00 PM", "00:00", "Monday"))
# Returns: 5:00 PM
