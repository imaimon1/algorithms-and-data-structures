import random 
#rod which each cut costs a certain amount whats the best value
def rod_cut(list, n, memo = []):
	if n == 0:
		return 0
	if len(memo) >=n:
		return memo[n-1]
	else:
		max = None
		for i in range(0,min(len(list),n)):
			num = list[i] + rod_cut(list,n-i-1,memo)
			if max==None or max < num:
				max = num
		memo.append(max)
		print memo
		return max 
		
#print rod_cut([1,5,8,9,10,17,17,20,24,30],40)

#multiply matrices
def matrix_multiplication(mat1,mat2):
	if len(mat1[0]) !=len(mat2):
		raise Exception('Matricies not compatible')
	c = []
	for i in range(len(mat1)):
		c.append([])
		for j in range(len(mat2[0])):
			num=0
			for k in range(len(mat1[i])):
				num += mat1[i][k]*mat2[k][j]
			c[i].append(num)
			
	return c 
	
#print matrix_multiplication([[1,2],[3,4]],[[1,2],[3,4]])
#multiply a bunch of matrices in fastest time
#i.e. say 2*100, 100*3, 3*3, size matrices what order is best to multiply 
def multi_matrix_multiplication(list):
	check = []
	for i in list:
		check.append(len(i))
	check.append(len(i[0]))
	blank_list = []
	for i in range(0,len(list)):
		blank_list.append(None)
#memo[a][b] is min number of operations for matrices between a,b
#info[a][b] is where we cut the matrix multiplication into 2 halves and do them independently
	memo = [blank_list[:] for i in range(len(list))]
	info = [blank_list[:] for i in range(len(list))]
	for k in range(0,len(list)):
		memo[k][k]=0
#l is number of matrices we multiply
	for l in range(1,len(list)):
		for i in range(len(list)-l):
			j= i + l
			min = None
			index = 0 
			for k in range(i,j):
#cost is cost of first half matrix mult. and sec. half and mult. both halves
				num = memo[i][k]+memo[k+1][j]+check[i]*check[k+1]*check[j+1]
				if min == None or min > num:
					min = num 
					index = k
			memo[i][j] = min
			info[i][j] = index
	return multiply_by_parts(0,len(list)-1,list,info)
#actually multiply the  matrices in order given by cutting them in parts	
def multiply_by_parts(first,second,list,info):
	if first == second:
		return list[first]
	first_half = multiply_by_parts(first,info[first][second],list,info)
	second_half = multiply_by_parts(info[first][second]+1,second,list,info)
	return matrix_multiplication(first_half,second_half)
	
#largest common subsequences 
def common_subsequence(string1,string2):
	out = [['' for i in range(len(string2))] for i in range(len(string1))] 
	for i in range(len(string1)):
		for j in range(len(string2)):
			if string1[i] == string2[j]:
				out[i][j] = out[i-1][j-1] + string1[i]
			elif out[i-1][j]>= out[i][j-1]:
				out[i][j] =out[i-1][j]
			else:
				out[i][j]=out[i][j-1]
	return out[-1][-1]
# largest monotonic subsequence 
def monotonic_increasing_sequence(list):
	new = sorted(list)
# out[i] is list of subsequence of size i with the smallest max elem. 
	out = [None]
	for j in range(len(list)):
		for i in range(len(out)-1,-1,-1):
#go through sequence and check if the max element in each subseq. is smaller than
#the elem of the seq. we are at
# if yes then the subs.+ this elem. is the best subs. with that amount of elem. so far
# if there is no subs. than it is the smallest elem.
			#making the smallest element
			if out[i] == None:
				if len(out) == 1:
					out.append([list[j]])
				else:
					out[1] = [list[j]]
			
			elif list[j]>out[i][-1]:
				#making a subseq. of a higher len
				if i+1 == len(out):
					new= out[i][:]
					new.append(list[j])
					out.append(new)
				else:
				#replacing a subseq. with one with smaller max elem.
					new= out[i][:]
					new.append(list[j])
					out[i+1] = new
				break
	return out