print("tinhluong v1.0, jan 2026")
giolam = float(input("nhap so gio lam viec: "))
luongcb = float(input("nhap luong theo gio co ban: "))

if giolam > 40: 
    tongluong = 40 * luongcb + (giolam - 40) * (luongcb * 1.5)
elif giolam <= 40:
    tongluong = luongcb * giolam
    
print("ket qua tinh luong la: ", tongluong)