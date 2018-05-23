input = list("---------- ")

#print(input)
flips_allowed = 3

count = 0

input_string = "".join(input)

# Check how many minues there are and collect their indices 

# At each minus, flip the next three flips 

# Repeat it until the minus are gone 

# If one of the pattern is the same as before, break the while loop and say it is impossible 
# print(input.count("-"))
# plus_index = input.index("-")
# print(plus_index)

completed = False;




while (input_string != "".join(["+" for j in range(len(input_string))])):
	
	if(input.count("-") > 0 and completed is False):
		plus_index = input.index("-")
		count += 1
	else:
		break

	# print("after count",count)
	print(input)
	for j in range(flips_allowed):
		if(plus_index + j < len(input)):
			if(input[plus_index + j] == "-"):
				input[plus_index + j] = "+"
			else:
				input[plus_index + j] = "-"

		else:
			completed = True
			break


input_string = "".join(input)
if(input_string == "".join(["+" for j in range(len(input_string))])):
	print(count)
else:
	print("IMPOSSIBLE!")


#print(input)