print("check nguyen am phu am")
textReg = input(str("moi nhap van ban bat ky: "))
text = textReg.lower()
vwel = 'ueoai'
csnt = 'bcdfghklmnpqrstvxyz'
vowels = 0
consonants = 0
for chars in text:
    if chars in vwel:
        vowels += 1
    if chars in csnt:
        consonants += 1
    
print("vowels count:", vowels, ", consonant count:", consonants)