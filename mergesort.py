def merge_sort(list):
	if len(list)==1:
		return list
		
	first_half=merge_sort(list[:int(len(list)/2)])
	second_half=merge_sort(list[int(len(list)/2):])
	ordered_list= []
	i=0
	j=0
	while len(ordered_list) < len(first_half) + len(second_half):
		if i < len(first_half) and j < len(second_half):
			if first_half[i] < second_half[j]:
				ordered_list.append(first_half[i])
				i +=1
			else:
				ordered_list.append(second_half[j])
				j+=1
		elif i < len(first_half):
			ordered_list.append(first_half[i])
			i+=1
		elif j < len(second_half):
			ordered_list.append(second_half[j])
			j+=1
	return ordered_list