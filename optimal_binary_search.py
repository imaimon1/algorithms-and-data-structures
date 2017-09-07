import random
#given two lists the first of keys and their probibilities of happening
#the second of the probility of inputs between every key. 
#i.e. list2[0] is the prob of all inputs before the key with prob list1[0]
#list2[1] is probility of inputs between the keys with probs list1[0],list1[1]
#i.e list2[0]list1[0]list2[1]list1[1]......
def optimal_binary_search1(list1,list2):
	if len(list1)+1 != len(list2):
		return 'false lists'
	#memo1[a,b] is the average cost for subtree with keys from a to b in list1 
	memo1 = [[None for i in range(len(list1)+1)]for i in range(len(list1)+2)]
	#memo2[a,b] is sum of probs between a and b 
	memo2 = [[None for i in range(len(list1)+1)]for i in range(len(list1)+2)]
	#solutions are saved solutions for working backwards
	solution= [[None for i in range(len(list1)+1)]for i in range(len(list1)+1)]
	#there are no keys from i to i-1 so it is just the probibility of inputs 
	#between these keys
	for i in range(1,len(list1)+2):
		memo1[i][i-1] = list2[i-1]
		memo2[i][i-1] = list2[i-1]
	# l i how big the subtree is we start with subtree of one key and get memo[i][i]
	# and keep going up to larger trees
	for l in range(0,len(list1)):
		for i in range(1,len(list1)-l+1):
			j = i+l
#prob getting inputs between i,j = prob( i,j-1) + prob key j and prob inputs between j-1 and j 
			memo2[i][j] = memo2[i][j-1]+list1[j-1]+list2[j]		
			for r in range(i,j+1):
#assume r is root
#left tree expectation + right tree expec. + probs of going through the first node
				guess = memo1[i][r-1] + memo1[r+1][j] + memo2[i][j]
				if memo1[i][j] == None or memo1[i][j]> guess:
					memo1[i][j] = guess
					solution[i][j] = r
	return solution
	
def optimal_binary_search2(list1,list2):
	if len(list1)+1 != len(list2):
		return 'false lists'
	memo1 = [[None for i in range(len(list1)+1)]for i in range(len(list1)+2)]
	memo2 = [[None for i in range(len(list1)+1)]for i in range(len(list1)+2)]
	solution= [[None for i in range(len(list1)+1)]for i in range(len(list1)+1)]
	
	for i in range(1,len(list1)+2):
		memo1[i][i-1] = list2[i-1]
		memo2[i][i-1] = list2[i-1]
	for l in range(0,len(list1)):
		for i in range(1,len(list1)-l+1):
			j = i+l
			memo2[i][j] = memo2[i][j-1]+list1[j-1]+list2[j]
			if j == i:
				guess = memo1[i][i-1] + memo1[i+1][i] + memo2[i][i]	
				memo1[i][i] = guess
				solution[i][i] = i				
			else:	
#root between root for previous solution and next solution
				for r in range(solution[i][j-1],solution[i+1][j]+1):
					guess = memo1[i][r-1] + memo1[r+1][j] + memo2[i][j]
					if memo1[i][j] == None or memo1[i][j]> guess:
						memo1[i][j] = guess
						solution[i][j] = r
	return solution