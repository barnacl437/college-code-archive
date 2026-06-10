tudien = dict()
tudien['hello'] = 'xin chao'
tudien['goodbye'] = 'tam biet'
tudien['stepbro'] = 'anh trai di bo'
tudien['bruh'] = 'bieu cam ngac nhien'
tudien['gay'] = 'dong tinh' 
tudien['eat'] = 'an'
tudien['femboy'] = 'dan ong dich thuc'
tudien['67'] = 'sau bay'

while True:
    menu = input("go t de thoat, nhan phim bat ky de tim tu: ")
    if menu == 't':
        break
    word = input('nhap mot tu tieng anh: ').lower()
    if word in tudien:
        print(tudien[word])
    else:
        meaning = input(str("word not found. please type its meaning: "))
        tudien[word] = meaning
        print("bruh ok thank you")