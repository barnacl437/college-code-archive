print("tiendien, jan 2026")
print("bang gia dien cap nhat den 2025")
ctThangTruoc = float(input("nhap so cong to thang truoc: ")
ctThangNay = float(input("nhap so cong to thang nay: ")

sd = ctThangNay - ctThangTruoc

# chia ra cac muc tang dan gia dien co so
# muc1 toi da 50kwh
# muc2 tu 51-100
# muc3 tu 101
muc1=min(sd, 50)
muc2=min(max(sd-50,0),50)
muc3=max(sd-100,0)

td = muc1*1984 + muc2*2050 + muc3*2500

print("tien dien la: " + td)