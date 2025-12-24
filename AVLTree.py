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
	def Search_from_node(self, node: AVLNode, key: int):
		if key == node.key or node.is_real_node() == False:
			# if we found the key or reached a virtual node
			return node, 0
		elif key < node.key:
			res_node, edges = self.Search_from_node(node.left, key)
			return res_node, edges + 1
		else:
			res_node, edges = self.Search_from_node(node.right, key)
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
		node = self.search_from_node(self.root, key)
		if node[0].is_real_node():
			return node
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
		return None, -1


	"""searches for a node in the dictionary corresponding to the key, starting at the max
        
	@type key: int
	@param key: a key to be searched
	@rtype: (AVLNode,int)
	@returns: a tuple (x,e) where x is the node corresponding to key (or None if not found),
	and e is the number of edges on the path between the starting node and ending node+1.
	"""
	def finger_search(self, key: int):
		return None, -1


	"""performs a left rotation on node
	
	@type node: AVLNode
	@param node: the node to perform the left rotation on
	"""
	def left_rotation(self, node: AVLNode):
		return


	"""performs a right rotation on node
	
	@type node: AVLNode
	@param node: the node to perform the right rotation on
	"""
	def right_rotation(self, node: AVLNode):
		return


	"""performs the appropriate rotation(s) on node to rebalance the tree
	
	@type node: AVLNode
	@param node: the node to perform the rotation(s) on
	"""
	def rotate(self, node: AVLNode):
		return


	"""fixes the AVL tree above node after an insertion or deletion
	
	@type node: AVLNode
	@param node: the node to start fixing from
	@type deletion: bool
	@param deletion: True if the fixing is after a deletion, False if after an insertion
	@rtype: int
	@returns: the number of promotions (aka. height increases) performed during the fixing"""
	def fix_above(self, v_node: AVLNode, deletion: bool):
		return -1

	"""creates a new AVLNode from a virtual node and gives it two children which are virtual nodes
	
	@type node: AVLNode
	@param node: a virtual node
	@type key: int
	@param key: key of the new node
	@type val: string
	@param val: value of the new node
	"""
	def create_node_from_virtual(self, node: AVLNode, key: int, val: str):
		return 


	"""given a virtual node, inserting the values into it and turning it to a real node

	@type v_node: AVLNode
	@param v_node: a virtual node
	@type key: int
	@param key: key of the new node
	@type val: string
	@param val: value of the new node
	"""
	def insert_node(self, v_node: AVLNode, key: int, val: str):
		return
	

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
		return None, -1, -1


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
		return None, -1, -1

	
	"""returns the successor of a given node in the tree

	@type node: AVLNode
	@param node: the node to find its successor
	@rtype: AVLNode
	@returns: the successor of node, None if node has no successor
	"""
	def successor(self, node: AVLNode):
		return None
	

	"""deletes node physically from the dictionary

	@type node: AVLNode
	@pre: node is a real pointer to a node in self
	"""
	def delete_physically(self, node: AVLNode):
		return


	"""deletes node from the dictionary

	@type node: AVLNode
	@pre: node is a real pointer to a node in self
	"""
	def delete(self, node: AVLNode):
		return	

	
	"""starting from root, finds the minimal node with height

	@type height: int
	@param height: the height to search for
	@rtype: AVLNode
	@returns: the minimal node with height height, None if such a node does not exist
	"""
	def find_minimal_by_height(self, height: int):
		return None
	

	"""starting from root, finds the maximal node with height
	
	@type height: int
	@param height: the height to search for
	@rtype: AVLNode
	@returns: the maximal node with height height, None if such a node does not exist
	"""
	def find_maximal_by_height(self, height: int):
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
	def join(self, tree2, key: int, val: str):
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
		return None, None
