#start clock at 1'oclock
hours = 1
while hours <= 12:
    #each hour starts at 0 minutes
    minutes = 0
    while minutes < 60:
        #each minute starts at 0 seconds
        seconds = 0
        while seconds < 60:
            if hours < 10:
                if minutes < 10:
                    if seconds < 10:
                        print(f'0{hours}:0{minutes}:0{seconds}')
                    else:
                        print(f'0{hours}:0{minutes}:{seconds}')
            else:
                print(f'{hours}:{minutes}:{seconds}')
            #after printing the current time,
            #increment the seconds counter
            seconds = seconds + 1

            #increment the minutes counter
        minutes = minutes + 1
    #after we reach 59 minutes, we add another hour to hour
    hours = hours + 1
