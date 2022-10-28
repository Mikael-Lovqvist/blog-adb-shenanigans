from math import sqrt

top_number = 1000

def is_prime(n):
	m = int(sqrt(n))
	#We have already excluded 2 so let's start on 3
	for div in range(3, m + 1):
		if n % div == 0:
			return False

	return True

for i in range(top_number >> 1):
	n = 2 * i + 1
	if is_prime(n):
		print(n)