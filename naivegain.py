def naivegain(list): 
	ans = 0 
	for i in range(0,len(list)):
		for j in range(i,len(list)):
			ans = max(ans, list[j]-list[i])

	return ans

print naivegain([1,5,25,11,17,82,57,110,88,250])

