from sets import Set

def children:
	pass

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

def main():

	for node in nodes:
		visited = Set([])
		empowerment(node, 2, visited)