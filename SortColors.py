file = open("ColorListUnsorted.txt", "r")
x = 1 

names = []
colors = []

for line in file: 
	x+= 1
	if x % 2 == 0:
		names.append(line)
	else: 
		colors.append(line)

x =0 
#write the arrays to a new file
print(names)
print (" ")
print(colors)
file.close()