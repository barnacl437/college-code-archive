path = input("type the location of the file: ")

try:
    file = open(path, 'r')
    print("filename ok")
except:
    print("no wei cant open", "'" + path + "'")