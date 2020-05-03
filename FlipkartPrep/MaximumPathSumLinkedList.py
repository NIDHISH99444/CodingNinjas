# Python program to construct a Maximum Sum Linked List out of
# two Sorted Linked Lists having some Common nodes
class LinkedList(object):
	def __init__(self):
	# head of list
		self.head = None

	# Linked list Node
	class Node(object):
		def __init__(self, d):
			self.data = d
			self.next = None

	# Method to adjust pointers and print final list
	def finalMaxSumList(self, a, b):
		result = None
		# assigning pre and cur to head
		# of the linked list
		pre1 = a
		curr1 = a
		pre2 = b
		curr2 = b
		# Till either of current pointers is not null
		# execute the loop
		while curr1 != None or curr2 != None:
			# Keeping 2 local variables at the start of every
			# loop run to keep track of the sum between pre
			# and cur reference elements.
			sum1 = 0
			sum2 = 0
			# Calculating sum by traversing the nodes of linked
			# list as the merging of two linked list. The loop
			# stops at a common node
			while curr1 != None and curr2 != None and curr1.data != curr2.data:
				if curr1.data < curr2.data:
					sum1 += curr1.data
					curr1 = curr1.next
				else:
					sum2 += curr2.data
					curr2 = curr2.next
			# If either of current pointers becomes null
			# carry on the sum calculation for other one.
			if curr1 == None:
				while curr2 != None:
					sum2 += curr2.data
					curr2 = curr2.next
			if curr2 == None:
				while curr1 != None:
					sum1 += curr1.data
					curr1 = curr1.next
			# First time adjustment of resultant head based on
			# the maximum sum.
			if pre1 == a and pre2 == b:
				result = pre1 if (sum1 > sum2) else pre2
			else:
				# If pre1 and pre2 don't contain the head references of
				# lists adjust the next pointers of previous pointers.
				if sum1 > sum2:
					pre2.next = pre1.next
				else:
					pre1.next = pre2.next
			# Adjusting previous pointers
			pre1 = curr1
			pre2 = curr2
			# If curr1 is not NULL move to the next.
			if curr1 != None:
				curr1 = curr1.next
			# If curr2 is not NULL move to the next.
			if curr2 != None:
				curr2 = curr2.next

		while result != None:
			print (str(result.data))
			result = result.next
		print ('')

	# Utility functions
	# Inserts a new Node at front of the list.
	def push(self, new_data):
		# 1 & 2: Allocate the Node &
		# Put in the data
		new_node = self.Node(new_data)
		# 3. Make next of new Node as head
		new_node.next = self.head
		# 4. Move the head to point to new Node
		self.head = new_node

# Driver program
llist1 = LinkedList()
llist2 = LinkedList()

# Linked List 1 : 1->3->30->90->110->120->NULL
# Linked List 2 : 0->3->12->32->90->100->120->130->NULL

llist1.push(120)
llist1.push(110)
llist1.push(90)
llist1.push(30)
llist1.push(3)
llist1.push(1)


llist2.push(12)
llist2.push(3)
llist2.push(0)

llist1.finalMaxSumList(llist1.head, llist2.head)

# This code is contributed by BHAVYA JAIN
