print("namnhuan, jan 2026")
print("cong cu tinh nam nhuan sieu lo 🐧🐧")
year = int(input("vui long dien nam vao: "))

print("doi mot ti...")
print("-------------")
if year % 100 == 0 and year % 400 == 0:
    print("day la nam the ky nhuan, chia het cho 100 va 400")
elif year % 100 == 0 and not year % 400 == 0:
    print("day la nam the ky khong nhuan, chia het cho 100 nhung khong phai 400")
elif year % 4 == 0 and not year % 100 == 0 and not year % 400 == 0:
    print("day la mot nam nhuan binh thuong")
elif year == 67:
    print("bay lai du trend nua roi, day la nam binh thuong nhe")
else:
    print("day la mot nam binh thuong khong nhuan")
    