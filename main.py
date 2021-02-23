# Main function raindrops
def raindrops(n):
	output = ""

	try:
		# Return Pling in output if 3 is a factor
		if n%3 == 0:
			output += "Pling"
		# Return Plang in output if 5 is a factor
		if n%5 == 0:
			output += "Plang"
		# Return Pling in output if 7 is a factor
		if n%7 == 0:
			output += "Plong"

		# If no factors of 3,5,7 return n
		if len(output) > 0:
			return output
		else:
			return str(n)

	except TypeError:
		return "please enter a number"


# Use the function if ran from this file
if __name__ == "__main__":
	num = input("please enter a number: ")
	if num.isdigit()
		print(raindrops(int(num)))
	else:
		print(raindrops(num))