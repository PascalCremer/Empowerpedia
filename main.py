from sets import Set

def children(node):
	if node <= 3:
		return [node*2+1, node*2+2]
	elif node == 4:
		return [9]
	else:
		return []

def empowerment(node, depth, visited):
	queue = []
	for child in children(node):
		if child not in visited:
			visited.add(child)
			queue.append(child)

	if depth > 1:
		for child in queue:
			empowerment(child, depth-1, visited)
	return len(visited)

empValues = []
nodes = range(10)
for node in nodes:
	visited = Set([])
	value = empowerment(node, 3, visited)
	empValues.append((node, value))

empValues.sort(key=lambda x:x[1],reverse=1)
print empValues[0:10]