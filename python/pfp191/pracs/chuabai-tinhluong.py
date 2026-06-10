print("chua bai tinh luong")

hours=int(input("moi nhap so gio lam viec: "))
rates=float(input("moi nhap luong co ban: "))
extra=max(hours-40,0)
total = hours*rates+extra*0.5*rates
print("tong luong la " + total)