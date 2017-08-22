import math 
class Heap(object):
	#binary
	#each n goes to 2n, 2n+1 as the left and right respectively
	
	def __init__(self,list):
		self.heap = list
		
	#adds something to the end of a heap
	def heap_append(self,a):
		self.heap.append(a)
		
	def maximize_heap(self):
		i = len(self.heap)-1
		while i >= 0:
			self.max_heap(i)
			i -= 1
		
	def max_heap_append(self,a):
		self.heap.append(a)
		
		maximize_heap()
		
		
	def max_heap(self, index):
		left =2*index
		right = 2*index + 1
		largest = index
		
		if right < len(self.heap) and self.heap[largest] < self.heap[right]:
			largest = right
		
		if left < len(self.heap) and self.heap[largest] < self.heap[left]:
			largest = left
		
		if (largest != index):
			max = self.heap[largest] 
			ini = self.heap[index]
			self.heap[index] = max
			self.heap[largest] = ini
			self.max_heap(largest)	
	
	def heap_sort(self):
		ordered_list=[]
		self.maximize_heap()
		out=len(self.heap)
		for i in range(0,out-1):
			ordered_list.append(self.heap[0])
			self.heap[0] = self.heap.pop()
			self.max_heap(0)
		ordered_list.append(self.heap[0])
		return ordered_list
	
	def max_heap_adjusted(self,index):
	#accidental bckwards binary search tree
	#max heap with the left larger than the right
		left = 2*index
		right = 2*index + 1
		
		if right < self.heap.len() and self.heap[index] < self.heap[right]:
			largest = left
			second_largest = right
			third_largest = index
		else:
			largest = index
			second_largest = left
			third_largest = right
			
			if left < self.heap.len() and self.heap[index] < self.heap[left]:
				largest = left
				second_largest = index
		
		if (not(largest == index and left == second_largest and right == third_largest)):
			max = self.heap[largest] 
			mid = self.heap[second_largest]
			min = self.heap[third_largest]
			self.heap[index] = max
			self.heap[left] = second_largest
			self.heap[right] = third_largest
			self.max_heap_adjusted(left)
			self.max_heap_adjusted(right)
	
	
	
	def bottom_level_fullness(self):
		#finds if the left end of the bottom level is full
		#int(math.log(self.heap.len()+1,2)) is the number of completed levels
		#2**(int(math.log(self.heap.len()+1,2))-1) is the size of last completed level 
		#2**(int(math.log(self.heap.len()+1,2)))-1 is the number of elements above the lowest level
		if len(self.heap)-2**(int(math.log(len(self.heap)+1,2)))-1 < 2**(int(math.log(len(self.heap)+1,2))-1):
			return 'left'
		else:
			return 'right'
poop=Heap([1,2,3,3,4,5,5,6,7])
out = poop.heap_sort()
print poop.bottom_level_fullness()