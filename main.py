from sets import Set
from itertools import chain
import random
import math
import MySQLdb

db=MySQLdb.connect(host="172.27.1.184", user="empowerpedia", passwd="empowerpedia", db="wikipedia")

def nodes(offset):
	cursor = db.cursor()
	cursor.execute("SELECT page.page_id FROM page WHERE page_namespace = 0 LIMIT %s,10000" % offset)
	return list(chain(*cursor.fetchall()))

def children(node):
	cursor = db.cursor()
	cursor.execute("SELECT page.page_id as children from pagelinks inner join page on pagelinks.pl_title = page.page_title and pagelinks.pl_namespace = page.page_namespace WHERE pagelinks.pl_from_namespace = 0 AND pagelinks.pl_from = %s" % node)

	data = cursor.fetchall()
	data = list(chain(*data))
	return data

def name(node):
	cursor = db.cursor()
	cursor.execute("SELECT page.page_title FROM page WHERE page.page_id = %s" % node)
	data = cursor.fetchall()
	return data[0][0]

def print_child_names(node):
	print name(node)
	namelist = []
	for child in children(node):
		namelist.append(name(child))
	print namelist



def empowerment(node, depth):
	number = 0
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
#nodes = range(10)
depth = 1
offset = 0
nodelist = nodes(offset)
while len(nodelist) > 0 and offset < 1e6:
	for node in nodes(0):
		visited = Set([])
		value = empowerment(node, depth, visited)
		empValues.append((name(node), value))
		empValues.sort(key=lambda x:x[1],reverse=1)
		empValues = empValues[0:10]
		#print "Empowerement for page %s is %s" % (name(node), value)
	offset += 10000
	nodelist = nodes(offset)
	print "Currently at %s" % offset

print empValues
