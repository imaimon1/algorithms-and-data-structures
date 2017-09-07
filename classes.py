class Stack(object):
	def __init__(self):
		self.stack = []
	
	def push(self,a):
		self.stack.append(a)
		
	def pop(self):
		if self.top() > 0:
			out = self.stack[-1]
			self.stack = self.stack[:-1]
			return out
		else:
			return "underflow"
	
	def top(self):
		return len(self.stack)
			
class Queue(object):
	def __init__(self):
		self.queue = []
		
	def enqueue(self,a):
		self.queue.append(a)
		
	def dequeue(self):
		if len(self.queue) > 1:
			out = self.queue[0]
			self.queue = self.queue[1:]
			return out
		elif len(self.queue) == 1:
			out = self.queue[0]
			self.queue = []
			return out
			
class linked_list(object):
	#last is last element and double_link asks if it is double_linked
	#use a pointer array so that two lists can interact and store memory in the same place
	def __init__(self, pointer_array = [], init = -1, double_linked = False):
		self.list = pointer_array
		self.list.append(None)
		self.init = init
		if self.init == -1:
			self.init = len(pointer_array)-1
		self.list[self.init] = self.Node(None,None,None)
		self.root =self.list[self.init]
		self.double_linked=double_linked
		self.last = self.init
	class Node(object):
		def __init__(self,key,next,prev=None):
			self.key = key
			self.next = next
			self.prev = prev
			
	def get_node(self,index):
		return self.list[index]
		
	def search(self,wanted_key):
		old = self.root
		if wanted_key == None:
			return self.init
		while old.next != None:
			new = self.get_node(old.next)
			if new.key == wanted_key:
				return old.next
			else:
				old = new
		return None
		
	def add_node(self,key):
		self.insert_node(key,None)
		
	#insert node after first instance of prev_key
	def insert_node(self, key, prev_key):
		prev = self.search(prev_key)
		next = self.get_node(prev).next
		new = self.Node(key,next)
		current=len(self.list)
		if self.double_linked:
			new.prev = prev
			if next != None:
				self.get_node(next).prev = current
		self.list.append(new)
		self.get_node(prev).next = current
		if prev == self.last:
			self.last = current
	#search to get the node before the node we want
	def search_prev(self,wanted_key):
		old = self.root
		oldest = None
		while old.next != None:
			new = self.get_node(old.next)
			if new.key == wanted_key:
				if oldest != None:
				#return old.next
					return oldest.next
				else:
					return self.init
			else:
				oldest = old
				old = new
	#delete a node
	def del_node(self,key):
		node_index=self.search(key)
		prev_index=self.search_prev(key)
		next_index = self.get_node(node_index).next
		self.get_node(prev_index).next = next_index
		out = self.list[node_index].key
		if self.double_linked and next_index != None:
			self.get_node(next_index).prev= prev_index
		self.list[node_index] = 0
		return out

def union(list1,list2,double_link):
	first_node1 = list1.get_node(list1.root.next)
	last_node2 = list2.get_node(list1.last)
	first_node1.prev = list1.last
	last_node2.next = list1.root.next
	
