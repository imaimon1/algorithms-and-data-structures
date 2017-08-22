import random
def quicksort(list,init,final):
	if init == final:
		return list
	
	def partition(list, init, final):
		index = init
		pivot = random.randint(init,final)
		piv_number = list[pivot]
		list[pivot] = list[final]
		list[final] = piv_number
		for i in range(init,final):
			if list[i] <  list[final]:
				new = list[index]
				list[index] = list[i]
				list[i] = new
				index +=1
	
		mid = list[final]
		list[final] = list[index]
		list[index] = mid
		return index

	mid = partition(list, init,final)
	
	if mid != init:
		quicksort(list, init, mid-1)
		
	if mid != final:
		quicksort(list, mid+1, final)
	
	
	
	return list
	
