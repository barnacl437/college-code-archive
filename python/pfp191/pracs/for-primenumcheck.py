while True:
    try:
        x = (input("nhap so nguyen duong bat ky: "))
        if x == q:
            break
        
        x = int(x)
        
        if x < 2:
            print(x, "khong phai so nguyen to")
        else:
            isprime = True
            
            i == 2
            while i * i <= x:
                if x%i == 0:
                    isprime = False
                    break
                i = i + 1
                
            if isprime == True:
                print(x, 'la so nguyen to')
            else:
                print(x, 'khong phai so nguyen to')
       
    except ValueError:
        print("bruh sai gia tri roi bozo")
    except:
        print("can loi")
            
        
