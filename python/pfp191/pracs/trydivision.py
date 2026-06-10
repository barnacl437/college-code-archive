try:
    x = int(input('nhap x '))
    y = int(input('nhap y '))
    thuong = x/y
    print(thuong)

except TypeError:
    print('ok boomer')
except ZeroDivisionError:
    print('wai wai wai y u div by 0??//?/')
except:
    print('u r gay lmfao')
finally:
    print('u r cute btw')