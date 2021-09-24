def add_time(start, duration, day=None):
    
    week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    
    start_time, meridium = start.split()
    start_time = list(map(int, start_time.split(':')))
    duration = list(map(int, duration.split(':')))

    days = 0
    hours = 0
    minutes = start_time[1] + duration[1]

    # Next hour begins after completion of 60 minutes
    if minutes >= 60:
        hours += 1
        minutes %= 60

    hours = hours + start_time[0] + duration[0]

    # Next days begins after completion of 24 hours
    if hours >= 24:
        days += hours // 24
        hours %= 24

    # Meridium changes after 12 hours
    if hours >= 12:
        hours %= 12

        # New day begins if 12 pass after beginning of 'PM'
        if meridium == 'PM':
            meridium = 'AM'
            days += 1
        else:
            meridium = 'PM'
    
    # In 12 hours format 0th hour is often read as 12
    if hours == 0:
        hours = 12

    new_time = f'{hours}:{minutes:02d} {meridium}'

    # Find the day of resulting time
    if day:
        index = week.index(day.capitalize())
        result_index = (index + days) % 7

        day = week[result_index]
        new_time += f', {day}'

    if days == 1:
        new_time += ' (next day)'
    elif days > 1:
        new_time += f' ({days} days later)'

    return new_time
