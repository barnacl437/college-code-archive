            
def confirm():
    while True:
        try:
            print("m co muon vao k (c/k): ", end="")
            confirm = input()
            if confirm == "c":
                break
            if confirm == "k":
                exit()
            else:
                print("invalid input.")
        except ValueError:
            print("bruh")
    
def getInt():
    print("nhap mot so nguyen duong n: ", end="")
    while True:
        try:
            n = int(input())
            if n <= 0:
                print("so nhap vao khong hop le. nhap so nguyen duong n: ", end="")
            else:
                return n
        except ValueError:
            print("bruh u stupid. nhap so nguyen duong n: ")

def printstr():
    for row in range(1, n+1):
        line = ""
        
        # Determine starting digit based on row number
        if row % 2 == 1:  # Odd row
            start_digit = 1
        else:  # Even row
            start_digit = 0
        
        # Build the row by alternating digits
        for pos in range(row):
            if pos % 2 == 0:
                # Even position: use start digit
                line += str(start_digit)
            else:
                # Odd position: use opposite digit
                line += str(1 - start_digit)
        
        print(line)

confirm()
n = getInt()
printstr()