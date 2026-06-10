def songuyen():
    n = int(input("moi nhap mot so nguyen duong n: "))
    while True:
        try:
            print(n)
            if (n <= 0):
                print("khong phai so nguyen duong. moi nhap so nguyen duong n: ", end=" ")
            else:            
                return n
        except ValueError:
            print("ban da nhap sai lmao vui long nhap lai so nguyen duong n: ", end=" ")
            
def sothuc():
    while True:
        try:
            n = int(input("moi nhap mot so thuc bat ki: "))
            print(n)
            return n
        except:
            print("ban da nhap sai lmao vui long nhap lai")
            
songuyen()

sothuc()
    
