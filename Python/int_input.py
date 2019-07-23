def int_input(prompt):
	while True:
		try:
			number = int(input(prompt))
		except ValueError:
			print('Non-numeric value entered. Try again')
		else:
			return number
			break