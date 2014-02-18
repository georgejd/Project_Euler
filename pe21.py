def factors(n):
	sum_fac = 0

	for i in range(1, (n/2) + 1):
		if n % i == 0 and n>i:
			sum_fac = sum_fac + i

	return sum_fac

answer=0

for i in range(220, 10000):
	for j in range(i, 10000):
		if factors(i) == j and factors(j) == i and i != j:
			answer = answer + i + j
text_file = open("PE21.txt", "w")
text_file.write("%s"%answer)
text_file.close()
