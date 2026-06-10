# ============================================
# PROGRAM: Sort a portion of a list by index range
# ============================================

# Error message function - called when user enters invalid input
def again():
    print("invalid value. type again u dumbarse")

# --------------------------------------------
# PART 1: Get list of integers from user
# --------------------------------------------
x_list = list()  # Create an empty list to store integers

while True:   
    # Ask user for input - they can type 'end' to finish
    x = input("type an integer (type 'end' to break the loop): ")
    
    # Check if user wants to stop entering numbers
    if x == "end":
        break  # Exit the loop
    else:
        # Try to convert input to integer
        try:
            x = int(x)  # Convert string to integer
            x_list.append(x)  # Add to our list
        except:
            # If conversion fails (user typed non-number), show error
            again()
               
print(x_list)  # Show the list user created

# --------------------------------------------
# PART 2: Get valid begin and end indices
# --------------------------------------------

# Get start index with validation
while True:
    try:
        # Show valid range in prompt so user knows what to type
        # len(x_list)-1 is the last valid index (since Python is 0-indexed)
        begin = int(input('type the start point in list (0 to {}): '.format(len(x_list)-1)))
        
        # Bounds check: ensure begin is within valid range
        # Valid indices are 0 to len(x_list)-1
        if begin < 0 or begin >= len(x_list):
            print("Start index out of bounds! Must be between 0 and {}".format(len(x_list)-1))
            continue  # Go back to start of loop, ask again
        break  # Input is valid, exit loop
    except:
        # User typed non-numeric input
        again()

# Get end index with validation
while True:
    try:
        end = int(input('type the end point in list (0 to {}): '.format(len(x_list)-1)))
        
        # Bounds check: ensure end is within valid range
        if end < 0 or end >= len(x_list):
            print("End index out of bounds! Must be between 0 and {}".format(len(x_list)-1))
            continue  # Go back to start of loop, ask again
        
        # Logic check: ensure end >= begin (range makes sense)
        if end < begin:
            print("End index must be >= begin index!")
            continue  # Go back to start of loop, ask again
        
        break  # Input is valid, exit loop
    except:
        again()

# Confirm what range we're sorting
print(f"Sorting from index {begin} to {end}")

# --------------------------------------------
# PART 3: Extract, sort, and reinsert
# --------------------------------------------
# Step 1: Extract the slice from begin to end (inclusive)
# Example: if begin=2, end=4, we get indices [2,3,4]
y = x_list[begin:end+1]  # end+1 because slice end is exclusive

# Step 2: Sort the extracted slice in place
y.sort()  # Now y is sorted

# Step 3: Rebuild the list with sorted portion
# x_list[:begin] = everything before begin index
# y = the sorted portion  
# x_list[end+1:] = everything after end index
x_list = x_list[:begin] + y + x_list[end+1:]

# Show final result
print(x_list)
