def main():
    time = input('What time is it? ')
    time = convert(time)
    
    if time >= 7 and time <= 8:
        print('breakfast time')
    elif time >= 12 and time <= 13:
        print('lunch time')
    elif time >= 18 and time <= 19:
        print('dinner time')
    else:
        print('WRONG')
     

def convert(time):
    time = list(time)
    hour = []
    minute = []
    m = False
    
    for x in time:
        if x == ':':
            m = True
        elif m == False:
            hour.append(x)
        elif m == True:
            minute.append(x)

    hour = ''.join(hour)            
    minute = ''.join(minute)

    return float(hour) + (float(minute) / 60)
            


while True:
    if __name__ == "__main__":
        main()