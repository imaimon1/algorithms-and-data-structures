def Merge_sort(List, Order):
	#first is a list second is a total order function
	if len(List)<2:
		return List[:]
	else:
		mid = int(len(List)/2)
		first_half=Merge_sort(List[:mid],Order)
		second_half=Merge_sort(List[mid:],Order)
	return Merge(first_half,second_half,Order)
def Merge(List1,List2,Order):
	#merges sorted list1 and list2 with ordering Order
	i1=0 
	i2=0
	Result=[]
	while(i1<len(List1) and i2<len(List2)):
		if Order(List1[i1],List2[i2]):
			Result.append(List1[i1])
			i1+=1
		else:
			Result.append(List2[i2])
			# a is not less than b and b is not less than a means
			#a==b so there is noe repeating elements
			#if Order(List1[i1],List2[i2])==Order(List2[i2],List1[i1])== False:
				#i1+=1
			i2+=1
	while(i1<len(List1)):
		Result.append(List1[i1])
		i1+=1
	while(i2<len(List2)):
		Result.append(List2[i2])
		i2+=1
	
	return Result
	
def Order(a,b):
	# any total ordering 
	return a < b
print Merge_sort([1,2,3,4,5,6,7,8,9],Order)

def Binary_search(List,Element,Order):
	#assumes ordered list with Order
	if len(List)==0:
		return False
	mid = int((len(List)-1)/2)
	if Order(List[mid],Element)==Order(Element,List[mid])==False:
		return True
	elif Order(List[mid],Element):
		if mid==len(List)-1:
			return False
		return Binary_search(List[mid+1:],Element,Order)
	else:
		if mid==0:
			return False
		return Binary_search(List[:mid],Element,Order)
print Binary_search([1,2,3,4,5],2,Order)
		
	






