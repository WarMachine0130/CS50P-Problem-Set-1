from distutils import extension


while True:
    file = list(input('File name: '))
    
    file.reverse()
    
    extension = []
    for x in file:
        if x == '.':
            break
        else:
            extension.append(x)
    
    extension.reverse()
    extension = "".join(extension)
    extension = extension.lower()

    if extension == 'gif' or extension == 'png' or extension == 'jpeg':
        print(f'image/{extension}')
    elif extension == 'jpg':
        print('image/jpeg')
    elif extension == 'txt':
        print('text/plain')
    elif extension == 'pdf' or extension == 'zip':
        print(f'application/{extension}')
    else:
        print('application/octet-stream')
        
