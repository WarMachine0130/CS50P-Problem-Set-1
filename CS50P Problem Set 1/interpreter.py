while True:
    userEx = list(input('Expression: '))
    
    val1 = []
    op = ''
    val2 = []
    
    for x in userEx:
        if x == ' ':
            val1 = ''.join(val1)
            break
        else:
            val1.append(x)
            
    for x in userEx:
        if x == '+' or  x == '-' or  x == '*' or  x == '/':
            op = x
            break
        
    userEx.reverse()
    
    
    for x in userEx:
        if x == ' ':
            val2.reverse()
            val2 = ''.join(val2)
            break
        else:
            val2.append(x)
    
    if op == '+':
        print(float(val1) + float(val2))
    elif op == '-':
        print(float(val1) - float(val2))
    elif op == '*':
        print(float(val1) * float(val2))
    elif op == '/':
        print(float(val1) / float(val2))
    else:
        print('error')


    
            

    

    