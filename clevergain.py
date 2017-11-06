#A succinct yet very smart algorithm to maximize the gain in a given array. 
#Runs in O(n) time! 


def clevergain(list):
	n = len(list)

	gain = 0 

	buy = list[0]

	for j in range(1,n):
		buy = min(buy, list[j])
		gain = max(gain, list[j] - buy)
	print gain 

