input = list("---------- ")
=
flips_allowed = 3

count = 0

input_string = "".join(input)
=

completed = False;




while (input_string != "".join(["+" for j in range(len(input_string))])):
	
	if(input.count("-") > 0 and completed is False):
		plus_index = input.index("-")
		count += 1
	else:
		break

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

