#Term Project
#Achilles Ecos
#Graph Theory


#Cite Pseudo code from Wikipedia
#https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm

class Graph:

	def __init__(self):
		#dictionary of nodes to its neighboring nodes where key is node and 
		#value is array of neighboring nodes
		self.graph = {}
		self.weight = {}

	#add the "line" from a node to another node
	def addEdge(self, start, end, distance):
		#normal order
		if start not in self.graph:
			self.graph[start] = [end]
		else:
			self.graph[start].append(end)
		#Reverse order
		if end not in self.graph:
			self.graph[end] = [start]
		else:
			self.graph[end].append(start)

		self.weight[(start,end)] = distance
		self.weight[(end,start)] = distance

	#returns an array of nodes that neighbor a node
	def getNeighbors(self, node):
		return self.graph[node]


	#returns the distasnce between two nodes
	def getWeight(self, node1, node2):
		return self.weight[(node1, node2)]


def dijkstra(graph, initial, target):
	#array of different nodes to check
	que = []
	#distance from initial start to node 
	distance = {}
	#the previous nodes checked
	previous = {}
	distance[initial] = 0
	#inital has no previous node
	previous[initial] = None
	que.append(initial)
	#check through all the nodes
	while len(que) != 0:
		#access first node from que
		node = que.pop(0)
		#more efficient
		if node == target:
			break	
		#check neighbor nodes
		for neighbor in graph.getNeighbors(node):
			tmpDist = distance[node] + graph.getWeight(neighbor, node)
			#if tempDistance is less than previous distance, update distance
			#when checking distance of new node, also update distance
			if neighbor not in distance or tmpDist < distance[neighbor]:
				que.append(neighbor)
				distance[neighbor] = tmpDist
				previous[neighbor] = node
	return distance, previous


graph = Graph()

graph.addEdge(1,2,7)
graph.addEdge(1,3,9)
graph.addEdge(1,6,14)
graph.addEdge(2,3,10)
graph.addEdge(2,4,15)
graph.addEdge(6,3,2)
graph.addEdge(6,5,9)
graph.addEdge(3,4,11)
graph.addEdge(4,5,6)

dist, prev = dijkstra(graph,1,5)
# print(prev)
# print(graph.graph)
# print(dist)


print(dijkstra(graph,1,5))













