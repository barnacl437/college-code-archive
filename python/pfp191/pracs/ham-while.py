try:
    x = int(input('moi nhap mot so nguyen duong: '))
except ValueError:
    x = 0
while x <= 0:
    try:
        x = int(input('u idiot. nhap so nguyen duong mau: '))
    except ValueError:
        x=0
        
print(x)
        
