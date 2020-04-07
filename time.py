import time

def units_of_time():
    days = int(input('Days: '))
    hours = int(input('Hours: '))
    minutes = int(input('Minutes: '))
    seconds = int(input('Seconds: '))

    days = days * 24 * 60 * 60
    hours = hours * 60 * 60
    minutes = minutes * 60
    total_seconds = days + hours + minutes + seconds

    print(total_seconds, 'seconds')


def rev_units_of_time():
    seconds = int(input('Seconds: '))
    days = 0
    hours = 0
    minutes = 0
    
    while seconds >= 60:
        if seconds >= 86400:
            seconds -= 86400
            days += 1
        elif seconds >= 3600:
            seconds -= 3600
            hours += 1
        elif seconds >= 60:
            seconds -= 60
            minutes += 1
    
    if len(str(hours)) < 2:
        hours = '0' + str(hours)
    if len(str(minutes)) < 2:
        minutes = '0' + str(minutes)
    if len(str(seconds)) < 2:
        seconds = '0' + str(seconds)
    
    print(f'{days}:{hours}:{minutes}:{seconds}')
        

def current_time():
    seconds = time.time()


if __name__ == '__main__':
    current_time()
