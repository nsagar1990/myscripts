from prime import *
import time
import traceback
INPUT = 600851475143 
i = 2

def find_factor(result, factor):
	if result == factor: print result
	try:
		if result%factor == 0:
			result = result/factor
			print result
			time.sleep(5)
			find_factor(result, 2)
		else:	
			if not isprime(factor+1):
				factor = get_prime(factor+1)
			else:
				factor = factor + 1
			find_factor(result, factor)
	except:
		import pdb;pdb.set_trace()


def get_prime(n):
	if isprime(n):
		return n
	else:
		n = n + 1
		get_prime(n)

find_factor(INPUT, i)
