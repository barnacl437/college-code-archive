print("gia ve phim, jan 2026")
giave = int(input("vui long nhap gia ve: "))
tuoi = int(input("vui long nhap tuoi: "))  

if tuoi < 6:
    tt= giave * 0 
    
elif tuoi >= 6 and tuoi < 18:
    tt= giave * 0.7
    
elif tuoi >= 65:
    tt= giave * 0.5
    
else:
    giave
    
print("----------")
print("thanh tien: ", tt)