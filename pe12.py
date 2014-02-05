def factors(n):
	result = [1]

	for i in range(1, n):
		if n % i == 0:
			result.append(i)

	return result



j=0
for i in range(1, 50000000):
	if len(factors(j))>=500:
		text_file = open("PE12.txt", "w")
		text_file.write("%s"%j)
		text_file.close()
		break
	j=i+j
