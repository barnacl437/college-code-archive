filename = input("moi nhap file: ")
try:
    f = open(filename, 'w')
    
except:
    print("cant open", filename)
    quit()
    
f.write("Ma SV, Ho va ten, Tuoi \n")
print("Nhap so sinh vien: ", end="")

while True:
    try:
        n = int(input())
        if n <= 0:
            print("So sv => 1. Nhap lai so sv: ")
        else:
            break
    except:
        print("Du lieu khong hop le. Moi nhap lai: ", end="")
        
for i in range(0, n):
    print("Moi nhap thu tu sv: ", i+1)
    masv = input("Ma SV: ")
    ten = input("Nhap ten: ")
    print("Tuoi: ", end="")
    while True:
        try:
            tuoi = int(input())
            if tuoi <=0:
                print("bruh u not even born. Moi nhap lai: ", end="")
            else:
                break
        except:
            print("Du lieu khong hop le. Moi nhap lai: ", end="")
        
f.write(masv + ',' + ten + ',' + str(tuoi) + ',' + "\n")
                