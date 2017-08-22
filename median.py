def find_index(list, index):
	if len(list)==1:
		return list[0]
	
	part_list = []
	median_list = []
	
	
	for i in range(0,len(list)/5):
		part_list.append(list[i*5:(i+1)*5])
	if int(len(list)/5)*5 < len(list):
		part_list.append(list[int(len(list)/5)*5:])
	for i in part_list:
		i.sort()
		median_list.append(i[int((len(i)-1)/2)])
	pivot = find_index(median_list,len(median_list)/2)
		
	def partition(list, pivot):
		index = 0
		init = 0
		final = len(list)
		
		for i in range(init,final):
			if list[i] <  pivot:
				new = list[index]
				list[index] = list[i]
				list[i] = new
				index +=1
		for i in range(index,final):
			if list [i] == pivot:
				new = list[index]
				list[index] = pivot
				index += 1
				list[i] = new
				
		return index - 1
		
	pivot = partition(list, pivot)
	if pivot == index:
		return list[pivot]
	if pivot < index:
		return find_index(list[pivot+1:], index-pivot-1)
	if pivot > index:
		return find_index(list[:pivot],index)
list = range(100,10,-1)
print find_index(list,75)