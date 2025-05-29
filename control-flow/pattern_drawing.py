pattern_size = int(input("Enter the size of the pattern:"))

#Ensure the number is positive
if pattern_size < 0:
	pattern_size *= -1

i = 0
while i < pattern_size:
	for j in range(pattern_size):
		print("*", end="")
	i += 1
	print()
