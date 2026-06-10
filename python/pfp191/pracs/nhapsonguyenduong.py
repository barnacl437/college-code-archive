while True:
    try:
        a = int(input('vui long nhap so nguyen duong: '))
        if a == 0:
            break
        if a < 0:
            continue
        print('so nguyen duong:', a)
    except ValueError:
        print("lmao nhap lai de")