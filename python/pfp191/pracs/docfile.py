filename = input(str('moi nhap ten file: '))
try:
    file = open(filename, 'r')
    line = 0
    for text in file:
        print(file)
    for lines in file:
        print(lines.rstrip())
        line += 1
    print('ts haz', line, 'lines')

finally:
    print('bruh')
    