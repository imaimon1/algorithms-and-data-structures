import classes
import random
#hahsmaps
class linked_list_extra(classes.linked_list):
	class Node(classes.linked_list.Node):
		def __init__(self,key,next,prev = None,info =None):
			self.key = key
			self.next = next
			self.prev = prev
			self.info = info
class chain_hashmap(object):
	def __init__(self):
		self.out_array = [None for i in range(0,50)] 
		self.a=random.randint(1,700)
		self.b=random.randint(0,700)
		
	def add_new(self,key,out):
		bin = self.hash_function(key)
		if self.out_array[bin] == None:
			self.out_array[bin] = linked_list_extra()
		linked_list = self.out_array[bin]
#		if linked_list.search(key) != None:
#			self.delete(key)
		linked_list.add_node(key)
		linked_list.get_node(linked_list.root.next).info = out
	def hash_function(self,key):
		k=key
		m=50
		return ((self.a*k +self.b) % 701) % 50
	def search(self,key):
		linked_list = self.out_array[self.hash_function(key)]
		if linked_list == None:
			raise Exception('key not in hash')
		else:
			pointer = linked_list.search(key)
			node = linked_list.get_node(pointer)
			return node.info

	def delete(self,key):
		linked_list = self.out_array[hash_function(self.key)]
		if linked_list == None:
			raise Exception('key not in hash')
		else:
			linked_list.del_node(key)

class open_adress_hashmap(object):
	def __init__(self,size=64):
		self.size = size
		self.array = [None for i in range(0,self.size)]
		self.a=random.randint(1,700)
		self.b=random.randint(0,700)
		self.c=random.randint(1,700)
		self.d=random.randint(0,700)
	
	def hash_function(self,key,n):
		k=key 
		first = (self.a*k +self.b) % 701
		second = (self.c*k +self.d)
		if second % 2 == 0:
			second += 1
		second % 701
		return (first +n*second) % self.size
	
	def add_new(self,key,out):
		for i in range(0,self.size):
			guess = self.hash_function(key,i)
			if self.array[guess]==None or self.array[guess]=='deleted':
				self.array[guess] = (key,out)
				return guess
			elif self.array[guess][0] == key:
				self.array[guess] = (key,out)
				return guess
		raise Exception('hash table full')
	def search(self,key):
		for i in range(0,self.size):
			guess=self.hash_function(key,i)
			if self.array[guess] != None: 
				if self.array[guess] != 'deleted':
					if self.array[guess][0] == key:
						return self.array[guess][1]
		raise Exception('not in array')
		
	def delete(self,key):
		for i in range(0,self.size):
			guess=self.hash_function(key,i)
			if self.array[guess] != None: 
				if self.array[guess] != 'deleted':
					if self.array[guess][0] == key:
						self.array[guess] = 'deleted'
new = chain_hashmap()	
check = range(0,64)
for i in range(0,64):
	poop =new.add_new(i,i+2)
#print check
#for i in range(40,50):
#	new.delete(i)
	
for i in range(0,64):
	print i, ((new.a*i +new.b) % 701) % 50, new.search(i), new.a, new.b