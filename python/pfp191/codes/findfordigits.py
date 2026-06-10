# this python program looks for any number with at least a digit 7 in the predefined range.
count = 0

for i in range(0,1000000000000000000):
	if "7" in str(i):
		count+=1
		continue

print(count)
