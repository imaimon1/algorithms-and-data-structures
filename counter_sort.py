def counter_sort(list, sort_by, sort_by_input, max):
	info = []
	out= [] 
	#sort_by is the function you are sorting the list by 
	for input in range(0,max+1):
		info.append(0)
	for i in range(0,len(list)):
		info[sort_by(list[i],sort_by_input)] += 1
	for i in range(1,max+1):
		info[i] += info[i-1]
	for i in range(0, len(list)):
		out.append(0)
	for i in range(len(list)-1, -1, -1):
		#return info[sort_by(list[i],sort_by_input)]
		out[info[sort_by(list[i],sort_by_input)]-1] = list[i]
		info[sort_by(list[i],sort_by_input)] -= 1
	return out
def radix_sort(list, digits):
	for i in range(1,digits+1):
		list = counter_sort(list,sort_by,i,9)
	return list 
def sort_by(number,digit):
	out = (number/10**(digit-1)) % 10
	return out

list = range(100,10,-1)
#for i in list:
#	print sort_by(list[i],2)
print radix_sort(list,3)