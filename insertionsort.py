def insertionsort(list):
	for index in range(1,len(list)):

		current = list[index]

		position = index
		while position>0 and list[position-1]>current:
			list[position] = list[position-1]
			position = position -1 

		list[position]=current
	return list