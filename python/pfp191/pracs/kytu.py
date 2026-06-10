print("phan loai kytu, jan 2026")
char = input("moi nhap mot ky tu: ")

if 'A' <= char <= 'Z':
    print("chu viet hoa")
elif 'a' <= char <= 'z':
    print("chu viet thuong")
elif '0' <= '9':
    print("chu so")
else:
    print("ki tu khac")