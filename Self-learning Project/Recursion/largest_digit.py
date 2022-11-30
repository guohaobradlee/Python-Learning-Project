"""
File: largest_digit.py
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n: (int) An integer.
	:return: (int) Single digit integer which is the bigger than any other digits integer.
	"""
	if n < 0:
		n = - n  # Make each integer a positive integer
	# Base case
	if n < 10:
		return n
	# Recursive case
	else:
		remainder_one = n % 10  # Store the last number.
		n = n // 10
		remainder_two = n % 10  # Store the second last number.
		if remainder_one > remainder_two:  # Compare the last two number to find the bigger one.
			n = n // 10 * 10 + remainder_one  # Store the bigger number in unit digit.
		return find_largest_digit(n)


if __name__ == '__main__':
	main()
