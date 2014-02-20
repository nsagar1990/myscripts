from prime import *
from itertools import *
PRIMES 	= []
TEMP	= []
TEMP_1	= []
COUNT	= []

for i in range(2,1000000):
	if isprime(i):
		PRIMES.append(str(i))

for i in PRIMES:
	if not ('2' in i or '4' in i or '6' in i or '8' in i or '5' in i):
		TEMP.append(i)
for i in TEMP:
	i = int(i[::-1])
	if isprime(i):
		TEMP_1.append(str(i))

for i in TEMP_1:
	flag = 0
	t = i
	i = permutations(list(i))
	for k in i:
		num = ''
		for n in k:
			num = num + n
		if not isprime(int(num)):
			flag = 1
			break
	if not flag:
		COUNT.append(num)
		

print len(COUNT)
print len(TEMP_1)
