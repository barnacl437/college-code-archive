retype = False
try:
    x = int(input("nhap mot so nguyen: "))
except ValueError:
    retype = True
while retype:
    try:
        x = int(input('u idiot. nhap so nguyen mau: '))
        retype = False
    except ValueError:
        retype = True
        
if x==0:
    print(x, ' co 1 chu so')
else:
    digits = 0
    if x < 0:
        y = -x
    else:
        y=x
    while y>0:
        digits+=1
        y=y//10
    print(x, ' co ', digits, ' chu so')