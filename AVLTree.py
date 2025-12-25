#id1:
#name1:
#username1:
#id2:
#name2:
#username2:


"""A class represnting a node in an AVL tree"""

class AVLNode(object):
	"""Constructor, you are allowed to add more fields. 
	
	@type key: int
	@param key: key of your node
	@type value: string
	@param value: data of your node
	"""
	def __init__(self, key: int, value: str):
		self.key = key
		self.value = value
		self.left = None
		self.right = None
		self.parent = None
		self.height = -1
		

	"""returns whether self is not a virtual node 

	@rtype: bool
	@returns: False if self is a virtual node, True otherwise.
	"""
	def is_real_node(self):
		return self.height != -1
	

	"""returns the balance factor of self by substracting the height of the right\
	subtree from the height of the left subtree
	
	@rtype: int
	@returns: the balance factor of self
	"""
	def get_bf(self):
		return self.left.height - self.right.height


	"""updates the height of self based on the heights of its children
	"""
	def update_height(self):
		self.height = max(self.left.height, self.right.height) + 1
	

	"""sets the left child of self to node and updates node's parent pointer

	@type node: AVLNode
	@param node: the new left child of self
	"""
	def set_left(self, node: AVLNode):
		self.left = node
		if node is not None:
			node.parent = self

	
	"""sets the right child of self to node and updates node's parent pointer
	
	@type node: AVLNode
	@param node: the new right child of self
	"""
	def set_right(self, node: AVLNode):
		self.right = node
		if node is not None:
			node.parent = self

"""
A class implementing an AVL tree.
"""

class AVLTree(object):

	"""
	Constructor, you are allowed to add more fields.
	"""
	def __init__(self, root = None, max = None, tree_size = 0):
		self.root = root
		self.max = max
		self.tree_size = tree_size
		if self.root is None:
			self.root = AVLNode(-1, "")


	"""returns the node with the maximal key in the dictionary

	@rtype: AVLNode
	@returns: the maximal node, None if the dictionary is empty
	"""
	def max_node(self):
		return self.max


	"""returns the number of items in dictionary 

	@rtype: int
	@returns: the number of items in dictionary 
	"""
	def size(self):
		return self.tree_size


	"""returns the root of the tree representing the dictionary

	@rtype: AVLNode
	@returns: the root, None if the dictionary is empty
	"""
	def get_root(self):
		return self.root


	"""helper function for in_order_traversal
	
	@type node: AVLNode
	@param node: the node to start the traversal from
	@type lst: list
	@param lst: the list to append the (key, value) touples to
	"""
	def in_order_traversal(self, node: AVLNode, lst: list):
		if node is None or node.is_real_node() == False:
			return
		self.in_order_traversal(node.left, lst)
		lst.append((node.key, node.value))
		self.in_order_traversal(node.right, lst)

	"""returns an array representing dictionary 

	@rtype: list
	@returns: a sorted list according to key of touples (key, value) representing the data structure
	"""
	def avl_to_array(self):
		arr = []
		self.in_order_traversal(self.root, arr)
		return arr


	"""searches for a node in the dictionary corresponding to the key (starting at node)

	@type node: AVLNode
	@param node: the node to start the search from
	@type key: int
	@param key: a key to be searched
	@rtype: (AVLNode,int)
	@returns: a tuple (x,e) where x is the node corresponding to key or the corresponding virtual node (if not found),
	and e is the number of edges on the path between the starting node and ending node+1.
	"""
	def search_from_node(self, node: AVLNode, key: int):
		if key == node.key or node.is_real_node() == False:
			# if we found the key or reached a virtual node
			return node, 0
		elif key < node.key:
			res_node, edges = self.search_from_node(node.left, key)
			return res_node, edges + 1
		else:
			res_node, edges = self.search_from_node(node.right, key)
			return res_node, edges + 1


	"""searches for a node in the dictionary corresponding to the key (starting at the root)
        
	@type key: int
	@param key: a key to be searched
	@rtype: (AVLNode,int)
	@returns: a tuple (x,e) where x is the node corresponding to key (or None if not found),
	and e is the number of edges on the path between the starting node and ending node+1.
	"""
	def search(self, key: int):
		if self.root is None:
			return None, -1
		node, edges = self.search_from_node(self.root, key)
		if node.is_real_node():
			return node, edges
		return None, -1


	"""searches for the biggest node in the dictionary smaller than key (starting at node)
	
	@type node: AVLNode
	@param node: the node to start the search from
	@type key: int
	@param key: a key to be searched
	@rtype: (AVLNode,int)
	@returns: a tuple (x,e) where x is the node corresponding to key (or None if not found),
	and e is the number of edges on the path between the starting node and ending node+1.
	"""
	def find_smaller_parent(self, node: AVLNode, key: int):
		temp_node = node
		edges = 0
		while temp_node.is_real_node() and temp_node.key >= key:
			temp_node = temp_node.parent
			edges += 1
		return temp_node, edges


	"""searches for a node in the dictionary corresponding to the key, starting at the max
        
	@type key: int
	@param key: a key to be searched
	@rtype: (AVLNode,int)
	@returns: a tuple (x,e) where x is the node corresponding to key (or None if not found),
	and e is the number of edges on the path between the starting node and ending node+1.
	"""
	def finger_search(self, key: int):
		if self.max is None:
			return None, -1
		parent, edges_1 = self.find_smaller_parent(self.max, key)
		if parent is None:
			return None, -1
		res_node, edges_2 = self.search_from_node(parent, key)
		if res_node.is_real_node():
			return res_node, edges_1 + edges_2
		return None, -1


	"""performs a left rotation on node
	
	@type node: AVLNode
	@param node: the node to perform the left rotation on
	"""
	def left_rotation(self, node: AVLNode):
		if node is None or not node.is_real_node():
			return

		u = node.right
		if u is None or not u.is_real_node():
			return

		parent = node.parent
		if parent is not None and parent.is_real_node():
			if parent.left is node:
				parent.set_left(u)
			else:
				parent.set_right(u)
		else:
			self.root = u
			u.parent = AVLNode(None, None)

		w = u.left
		u.set_left(node)
		node.set_right(w)

		node.update_height()
		u.update_height()


	def right_rotation(self, node: AVLNode):
		if node is None or not node.is_real_node():
			return

		u = node.left
		if u is None or not u.is_real_node():
			return

		parent = node.parent
		if parent is not None and parent.is_real_node():
			if parent.left is node:
				parent.set_left(u)
			else:
				parent.set_right(u)
		else:
			self.root = u
			u.parent = AVLNode(None, None)

		w = u.right
		u.set_right(node)
		node.set_left(w)

		node.update_height()
		u.update_height()


	def rotate(self, node: AVLNode):
		if node is None or not node.is_real_node():
			return

		bf = node.get_bf()

		if bf == -2:
			r = node.right
			if r.get_bf() in (-1, 0):
				self.left_rotation(node)
			else:  # bf = +1
				self.right_rotation(r)
				self.left_rotation(node)

		elif bf == 2:
			l = node.left
			if l.get_bf() in (1, 0):
				self.right_rotation(node)
			else:  # bf = -1
				self.left_rotation(l)
				self.right_rotation(node)

	"""fixes the AVL tree above node after an insertion or deletion
	
	@type node: AVLNode
	@param node: the node to start fixing from
	@type deletion: bool
	@param deletion: True if the fixing is after a deletion, False if after an insertion
	@rtype: int
	@returns: the number of promotions (aka. height increases) performed during the fixing"""
	def fix_above(self, node: AVLNode, deletion: bool):
		promotions = 0
		node = node.parent
		while node is not None and node.is_real_node():
			prev_height = node.height
			node.update_height()
			bf = node.get_bf()
			if abs(bf) <= 1:
				if node.height != prev_height:
					# height changed
					promotions += 1
				else:
					# height didn't change, stop fixing
					break
			else:
				# after rotation, heights are updated inside rotate function
				self.rotate(node)
				if deletion == False:
					# insertion case
					# after rotation, height of node decreases
					# so we stop fixing
					break
			node = node.parent
		return promotions

	"""creates a new AVLNode from a virtual node and gives it two children which are virtual nodes
	
	@type node: AVLNode
	@param node: a virtual node
	@type key: int
	@param key: key of the new node
	@type val: string
	@param val: value of the new node
	"""
	def create_node_from_virtual(self, v_node: AVLNode, key: int, val: str):
		v_node.key = key
		v_node.value = val
		v_node.set_left(AVLNode(-1, ""))
		v_node.set_right(AVLNode(-1, ""))
		v_node.update_height()
		return 


	"""given a virtual node, inserting the values into it and turning it to a real node

	@type v_node: AVLNode
	@param v_node: a virtual node
	@type key: int
	@param key: key of the new node
	@type val: string
	@param val: value of the new node
	@rtype: (AVLNode,int)
	@returns: a tuple (x,h) where x is the new node, and h is the number of PROMOTE cases during the AVL rebalancing
	"""
	def insert_node(self, v_node: AVLNode, key: int, val: str):
		self.create_node_from_virtual(v_node, key, val)
		if self.max is None or self.max.is_real_node() == False or key > self.max.key:
			self.max = v_node
		self.tree_size += 1
		promotions = self.fix_above(v_node, False)
		if self.root.parent is None:
			self.root.parent = AVLNode(None, None)
		return v_node, promotions
	

	"""inserts a new node into the dictionary with corresponding key and value (starting at the root)

	@type key: int
	@pre: key currently does not appear in the dictionary
	@param key: key of item that is to be inserted to self
	@type val: string
	@param val: the value of the item
	@rtype: (AVLNode,int,int)
	@returns: a 3-tuple (x,e,h) where x is the new node,
	e is the number of edges on the path between the starting node and new node before rebalancing,
	and h is the number of PROMOTE cases during the AVL rebalancing
	"""
	def insert(self, key: int, val: str):
		node, edges = self.search_from_node(self.root, key)
		inserted_node, promotions = self.insert_node(node, key, val)
		return inserted_node, edges, promotions


	"""inserts a new node into the dictionary with corresponding key and value, starting at the max

	@type key: int
	@pre: key currently does not appear in the dictionary
	@param key: key of item that is to be inserted to self
	@type val: string
	@param val: the value of the item
	@rtype: (AVLNode,int,int)
	@returns: a 3-tuple (x,e,h) where x is the new node,
	e is the number of edges on the path between the starting node and new node before rebalancing,
	and h is the number of PROMOTE cases during the AVL rebalancing
	"""
	def finger_insert(self, key: int, val: str):
		if self.max is None or self.max.is_real_node() == False:
			return self.insert(key, val)
		search_root, edges = self.find_smaller_parent(self.max, key)
		node, edges_2 = self.search_from_node(search_root, key)
		inserted_node, promotions = self.insert_node(node, key, val)
		return inserted_node, edges + edges_2, promotions

	
	"""returns the successor of a given node in the tree

	@type node: AVLNode
	@param node: the node to find its successor
	@rtype: AVLNode
	@returns: the successor of node, None if node has no successor
	"""
	def successor(self, node: AVLNode):
		if node.right.is_real_node():
			# going down to find the successor
			temp_node = node.right
			while temp_node.left.is_real_node():
				temp_node = temp_node.left
			return temp_node
		else:
			# going up to find the successor
			temp_node = node
			while temp_node.parent is not None and temp_node == temp_node.parent.right:
				temp_node = temp_node.parent
			return temp_node.parent
	

	"""deletes node physically from the dictionary

	@type node: AVLNode
	@pre: node is a real pointer to a node in self
	"""
	def delete_physically(self, node: AVLNode):
		# works even if both node's children are virtual
		assigned = None
		if node.right.is_real_node() == False:
			if node.parent.left == node:
				node.parent.set_left(node.left)
			else:
				node.parent.set_right(node.left)
			assigned = node.left
		elif node.left.is_real_node() == False:
			if node.parent.left == node:
				node.parent.set_left(node.right)
			else:
				node.parent.set_right(node.right)
			assigned = node.right
		
		if self.root == node:
			self.root = assigned
		return


	"""deletes node from the dictionary

	@type node: AVLNode
	@pre: node is a real pointer to a node in self
	"""
	def delete(self, node: AVLNode):
		self.tree_size -= 1
		if node.left.is_real_node() == False or node.right.is_real_node() == False:
			# node has at most one real child
			parent = node.parent
			self.delete_physically(node)
			self.fix_above(parent, True)
		else:
			# node has two real children
			u = self.successor(node)
			parent = u.parent
			self.delete_physically(u)
			if node.parent.left == node:
				node.parent.set_left(u)
			else:
				node.parent.set_right(u)
			
			# if parent == node:
			u.set_left(node.left)
			# if parent != node:
			u.set_right(node.right)
			u.update_height()
			
			if self.root == node:
				self.root = u

			self.fix_above(parent.left, True)
		


		# updating max if needed
		if self.max == node:
			if node.left.is_real_node():
				self.max = node.left
				while self.max.right.is_real_node():
					self.max = self.max.right
			else:
				self.max = node.parent

		return

	
	"""starting from root, finds the minimal node with height

	@type height: int
	@param height: the height to search for
	@rtype: AVLNode
	@returns: the minimal node with height height, None if such a node does not exist
	"""
	def find_minimal_by_height(self, height: int):
		if self.root is None or not self.root.is_real_node():
			return None

		stack = []
		node = self.root
		while node.is_real_node() or stack:
			while node.is_real_node():
				stack.append(node)
				node = node.left
			node = stack.pop()
			if node.height == height:
				return node
			node = node.right
		return None
	

	"""starting from root, finds the maximal node with height
	
	@type height: int
	@param height: the height to search for
	@rtype: AVLNode
	@returns: the maximal node with height height, None if such a node does not exist
	"""
	def find_maximal_by_height(self, height: int):
		if self.root is None or not self.root.is_real_node():
			return None

		stack = []
		node = self.root
		while node.is_real_node() or stack:
			while node.is_real_node():
				stack.append(node)
				node = node.right
			node = stack.pop()
			if node.height == height:
				return node
			node = node.left
		return None
	

	"""joins self with item and another AVLTree

	@type tree2: AVLTree 
	@param tree2: a dictionary to be joined with self
	@type key: int 
	@param key: the key separting self and tree2
	@type val: string
	@param val: the value corresponding to key
	@pre: all keys in self are smaller than key and all keys in tree2 are larger than key,
	or the opposite way
	"""
	def join(self, tree2: AVLTree, key: int, val: str):
		if self.root.is_real_node() == False:
			tree2.insert(key, val)
			self.root = tree2.root
			self.max = tree2.max
			return
		
		if tree2.root.is_real_node() == False:
			self.insert(key, val)
			return
		

		if tree2.root.height < self.root.height:
			t1 = tree2
			t2 = self
		else:
			t1 = self
			t2 = tree2
		
		if t1.root.key > t2.root.key:
			# t1's keys are larger than t2's keys
			maximal = t2.find_maximal_by_height(t1.root.height)
			new_node = AVLNode(key, val)
			if maximal.parent.left == maximal:
				maximal.parent.set_left(new_node)
			else:
				maximal.parent.set_right(new_node)
			new_node.set_left(maximal)
			new_node.set_right(t1.root)
			self.max = t1.max
			maximal.update_height()
		else:
			# t1's keys are smaller than t2's keys
			minimal = t2.find_minimal_by_height(t1.root.height)
			new_node = AVLNode(key, val)
			if minimal.parent.left == minimal:
				minimal.parent.set_left(new_node)
			else:
				minimal.parent.set_right(new_node)
			new_node.set_left(t1.root)
			new_node.set_right(minimal)
			self.max = t2.max
			minimal.update_height()

		# fixing the tree
		self.fix_above(new_node.parent, False)
		self.tree_size += tree2.size() + 1
		
		# making tree2 empty
		tree2.root = AVLNode(-1, "")
		tree2.max = None
		tree2.tree_size = 0
		return


	"""splits the dictionary at a given node

	@type node: AVLNode
	@pre: node is in self
	@param node: the node in the dictionary to be used for the split
	@rtype: (AVLTree, AVLTree)
	@returns: a tuple (left, right), where left is an AVLTree representing the keys in the 
	dictionary smaller than node.key, and right is an AVLTree representing the keys in the 
	dictionary larger than node.key.
	"""
	def split(self, node: AVLNode):
		t1 = AVLTree(node.left, None, node.left.size)
		t2 = AVLTree(node.right, self.max, node.right.size)

		temp_node = node
		while temp_node != self.root:
			parent = temp_node.parent
			if parent.left == temp_node:
				# temp_node is a left child
				new_tree = AVLTree(parent.right, None, parent.right.size)
				parent.set_right(AVLNode(-1, ""))
				self.fix_above(parent, True)
				t2.join(new_tree, parent.key, parent.value)
			else:
				# temp_node is a right child
				new_tree = AVLTree(parent.left, None, parent.left.size)
				parent.set_left(AVLNode(-1, ""))
				self.fix_above(parent, True)
				t1.join(new_tree, parent.key, parent.value)
			temp_node = parent
		# making self empty
		self.root = AVLNode(-1, "")
		self.max = None
		self.tree_size = 0
		return t1, t2
