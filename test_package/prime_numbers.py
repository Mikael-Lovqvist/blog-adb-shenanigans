from math import sqrt

def is_prime(n):
	m = int(sqrt(n))
	#We have already excluded 2 so let's start on 3
	for div in range(3, m + 1):
		if n % div == 0:
			return False

	return True

def list_primes(start_number, top_number):
	for i in range(start_number >> 1, (top_number >> 1) + 1):
		n = 2 * i + 1
		if is_prime(n):
			print(n)