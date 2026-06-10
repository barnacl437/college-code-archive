def getInt():
    print("Moi nhap mot so nguyen duong n: ", end="")
    while True:
        try:
            n = int(input())
            if n <= 0:
                print("so nhap vao khong hop le. nhap so nguyen duong n: ", end="")
            else:
                return n
        except ValueError:
            print("bruh u stupid. nhap so nguyen duong n: ")
            
def getFloat():
    print("Moi nhap mot so thuc:", end="")
    while True:
        try:
            n = int(input())
            return n
        except ValueError:
            print("gia tri khong hop le. nhap mot so thuc: ", end="")
                    
n = getInt()
min = 0
max = 0
sum = 0
count = 0
for i in range(1, n+1):
    n = getFloat(i)
    count+=1
    if (count==1):
        min = n
        max = n
    else:
        if min>n:
            min = n
        if max<n:
            max = n
    sum+=n
print("Min ",min)
print("max ",max)
print("sum ",sum)
print("count ",count)
    
