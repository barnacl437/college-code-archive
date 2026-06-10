print("intchanle, jan 2026")
print("proudly powered by conditional lmao")
a = int(input("moi nhap so nguyen: "))

if a > 0 and a%2 == 0:
    print("so nguyen duong chan")
elif a > 0 and a%2 != 0:
    print("so nguyen duong le")
elif a < 0 and a%2 == 0:
    print("so nguyen am chan")
elif a < 0 and a%2 != 0:
    print("so nguyen am le")
else:
    print("so khong hop le")