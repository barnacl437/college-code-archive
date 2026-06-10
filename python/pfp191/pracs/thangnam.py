print("thangnam, jan 2026")
year = int(input("moi nhap nam: "));
month = int(input("moi nhap thang:: "));

leapYr = (year % 400 == 0) or (year%4==0 and year%100!=0)
dates = 30

if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    dates = 31
elif month == 2:
    dates = 28
    if leapYr:
        dates = dates + 1
        
while year != 0:
    print(str(year) +'/'+ str(month) +' co '+ str(dates)+' ngay.')
else:
    print("nam khong ton tai.")