import time

def factors(n):
	sum_factors=0
	factors_list = set(reduce(list.__add__,([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
	sum_factors = sum(factors_list)-n
	return sum_factors

answer=0

for i in range(220, 10000):
	for j in range(i+1, 10000):
		if factors(i) == j:
			if factors(j) == i and i != j:
				answer += i + j
text_file = open("PE21.txt", "w")
text_file.write("%s"%answer)
text_file.close()
