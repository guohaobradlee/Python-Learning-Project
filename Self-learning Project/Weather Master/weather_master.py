"""
File: weather_master.py
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""


# When user inputs -100, this program will terminate.
EXIT = -100


def main():
	"""
	This program will find out the highest, the lowest and average temperature
	in those temperature user entered, and count how many days the temperature
	is below sixteen degrees.
	"""
	print('stanCode "Weather Master 4.0"!')
	new_temperature = int(input('Next Temperature: (Or EXIT to quit)?'))
	# If the first input temperature is not -100, it counts 1.
	times = 1
	if new_temperature == EXIT:
		print('No temperature were entered.')
	else:
		"""
		For first input temperature. Assign the first input temperature
		to highest, lowest and total respectively.
		"""
		highest = new_temperature
		lowest = new_temperature
		total = new_temperature
		average = total / times
		"""
		For first input temperature, it pluses 1
		when temperature is below 16 degrees.
		"""
		cold_days = 0
		if new_temperature < 16:
			cold_days += 1
		while True:
			times += 1
			new_temperature = int(input('Next Temperature: (Or -100 to quit)?'))
			if new_temperature == EXIT:
				break
			if new_temperature < 16:
				cold_days += 1
			highest = higher(highest, new_temperature)
			lowest = lower(lowest, new_temperature)
			total = total + new_temperature
			average = total / times
		print('Highest temperature = ' + str(highest))
		print('Lowest temperature = ' + str(lowest))
		print('Average = ' + str(average))
		print(str(cold_days) + ' cold day(s)')


# Determine which temperature is higher.
def higher(t1, t2):
	if t1 > t2:
		return t1
	else:
		return t2


# Determine which temperature is lower.
def lower(t1, t2):
	if t1 < t2:
		return t1
	else:
		return t2


if __name__ == "__main__":
	main()
