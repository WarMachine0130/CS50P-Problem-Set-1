while True:
    greeting = list(input('Greeting: '))

    i = 0
    for x in greeting:
      if x == ' ' or x == ',':
          greeting = greeting[:i]
          break
      else:
          i += 1

    if "".join(greeting) == 'Hello':
        print('$0')
    elif greeting[0] == 'H':
        print('$20')
    else:
        print('$100')
    
        


