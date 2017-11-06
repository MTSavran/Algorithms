tree = {1:[2,3],2:[4],3:[5,6]}

#PRINTS BINARY TREE HORIZONTALLY
def levelorder(tree,root):
	q = [root]
	levels = {root:0}
	while len(q)!=0:
		node = q.pop(0)
		if node in tree:
			for child in tree[node]:
				q.append(child)
				levels[child] = levels[node]+1 
	reverse = {}
	for element in levels:
		if levels[element] not in reverse:
			reverse[levels[element]] = []
		if levels[element] in reverse:
			reverse[levels[element]].append(element)
	for element in reverse:
		print reverse[element]
print levelorder(tree,1)


#PRINT BINARY TREE VERTICALLY 
class Node(object):
	def __init__(self,value,left=None,right=None):
		self.left = left
		self.right = right
		self.value = value

root = Node(1,Node(2,Node(4),Node(5)),Node(3))

def columnorder(root):
	levelmap = {root:0}
	def recur(root,levelmap):
		if root is None:
			return levelmap
		if root.left:
			levelmap[root.left] = levelmap[root]-1
			recur(root.left,levelmap)
		if root.right:
			levelmap[root.right] = levelmap[root]+1
			recur(root.right,levelmap)
		return levelmap
	levelmap= recur(root,levelmap)
	answer = {}
	for node in levelmap:
		answer[node.value] = levelmap[node]
	return answer

# print columnorder(root)

ondort = Node(14)
on = Node(10)
oniki = Node(12,on,ondort)
dort = Node(4)
sekiz = Node(8,dort,oniki)
yirmiiki = Node(22)
yirmi = Node(20,sekiz,yirmiiki)


def kthsmallest(root,k):
	counter = 0 
	array = []
	def recur(root,array,counter):
		if root is None:
			return array
		if root.left:
			recur(root.left,array,counter+1)
		array.append(root)
		if root.right:
			recur(root.right,array,counter+1)
		return array
	cvp = recur(root,array,counter)
	an = []
	for i in cvp:
		an.append(i.value)
	return an[k], an


print kthsmallest(yirmi,3)



