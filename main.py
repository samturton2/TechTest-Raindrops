# Main function raindrops
def raindrops(n):
	output = ""

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














# Use the function if ran from this file
if __name__ == "__main__":

	num = input("please enter a number: ")
	try:
		print(raindrops(int(num)))
	except ValueError:
		try:
			print(raindrops(float(num)))
		except ValueError:
			print("Please enter a number")