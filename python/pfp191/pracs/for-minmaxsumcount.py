min = 0
max = 0
sum = 0
cnt = 0

while True:
    x = input('type an integer: ')
    if x=="done":
        break
    try:
        x = int(x)
    except ValueError:
        print('no integer. pls type again.')
        continue
    sum += x
    cnt += x
    if cnt ==1:
        min = x
        max = x
    else:
        if x < min:
            min = x
        if x < max:
            max = x
            
print("  min  |  max  |  sum  |  cnt  ")
print("", min, "    ",  max ,"     ", sum ,"     ", cnt)