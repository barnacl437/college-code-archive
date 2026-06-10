try:
    x = int(input('moi nhap mot so nguyen duong: '))
except ValueError:
    x = 0
while x<=0:
    try:
        x= int(input('u idiot. nhap lai so nd mau: '))
    except ValueError:
        x=0

y=0
while (y<x):
    print(y,end=" ")
    y += 2
    
        