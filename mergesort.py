def merge(A,B):
	sortedList = []
	def recur(A,B):
		if len(A) == 0:
			sortedList.extend(B)
			return 
		if len(B) == 0:
			sortedList.extend(A)
			return
		if A[0] <= B[0]:
			sortedList.append(A[0])
			recur(A[1:],B)
		else:
			sortedList.append(B[0])
			recur(A,B[1:])
	recur(A,B)
	return sortedList





def mergesort(list):

	if len(list)>1:
		mid = len(list)//2
		left = list[:mid]
		right = list[mid:]

		mergesort(left)
		mergesort(right)

		i = 0 

		j = 0

		k = 0

		while i < len(left) and j < len(right):
			if left[i] < right[j]:
				list[k] = left[i]
				i += 1
			else: 
				list[k] = right[j]
				j+=1
			k+=1 
		while i < len(left):
			list[k]=left[i]
			i += 1
			k +=1 
		while j < len(right):
			list[k]=right[j]
			j+=1
			k+=1


			
list = [1,2,5,7,10,5,44,3,97]

mergesort(list)
print list