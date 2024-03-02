def time_difference(time_one, time_two):
    # add seconds
    hour_one, minutes_one, seconds_one, meridiem_one = int(time_one[:2]), int(time_one[3:5]), int(
        time_one[6:8]), time_one[8:]
    hour_two, minutes_two, seconds_two, meridiem_two = int(time_two[:2]), int(time_two[3:5]), int(
        time_two[6:8]), time_two[8:]

    # result_hour = hour_one - hour_two
    # result_minutes = minutes_one - minutes_two
    # result_seconds = seconds_one - seconds_two

    if meridiem_one == 'PM':
        hours1 = str(int(hour_one) + 12)
    if meridiem_two == 'PM':
        hours2 = str(int(hour_two) + 12)

    # if meridiem_one == 'PM' and hour_one != '12':
    #     hours1 = str(int(hour_one) + 12)
    # if meridiem_two == 'PM' and hour_two != '12':
    #     hours2 = str(int(hour_two) + 12)

    time = (int(hour_two) - int(hour_one)) * 3600 + (int(minutes_two) - int(minutes_one)) * 60

    hours, remainder = divmod(time, 3600)
    minutes, seconds = divmod(remainder, 60)
    b = [hours, minutes, seconds]

    return b

    # return f"{result_hour}:{result_minutes}:{result_seconds}"


time1 = "05:30:00PM"
time2 = "11:00:00AM"
output = time_difference(time1, time2)
print(output)
