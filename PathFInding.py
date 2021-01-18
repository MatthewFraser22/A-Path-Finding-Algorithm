#The Node class for A* pathfinding
class Node():
	def __init__(self,parent=None, position=None):
		self.parent = parent
		self.position = position 
		self.f = 0
		self.g = 0
		self.h = 0

	#returns true if 2 positions are equal to eachother 
	def __eq__(self,other):
		return self.position == other.position

#returns a list of the fastest path o the root
def A_Star(start,end,maze):

	#node being looked at 
	openList = []
	closedList = []

	#create a start node
	startNode = Node(None,start)
	startNode.f = startNode.g = startNode.h = 0

	#create end node
	endNode = Node(None, end)
	endNode.f = endNode.g = endNode.h = 0


	#add the start node to the opeb list
	openList.append(startNode)

	#loop ends once the end is found
	while len(openList) > 0:

		#gets the current node 
		current_ = openList[0]
		current_index = 0
		children = []
		

		#loops through index and item in open list and if f score is < than the current f score then we update the current
		for index, item in enumerate(openList):
			if item.f < current_.f:
				current_ = item
				current_index = index
				
		#removes at index and adds to closed list
		openList.pop(current_index)
		closedList.append(current_)


		#if the goal is found the path is added to the path list
		if current_ == endNode:
			path = []
			curr = current_

			while curr is not None:
				path.append(curr.position)
				curr = curr.parent
			#reversed the path
			return path[::-1]

		#generates children : border is set
		for new_pos in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
			#gets the nodes position
			nodePosition = (current_.position[0] + new_pos[0], current_.position[1] + new_pos[1])

			#checks to see if the values are within range
			if nodePosition[0] > (len(maze)-1) or nodePosition[0] < 0 or nodePosition[1] > (len(maze[len(maze)-1]) -1) or nodePosition[1] < 0:
				continue
			#make sure walkable terrain
			if maze[nodePosition[0]][nodePosition[1]] != 0:
				continue

			#creates a new node
			newNode = Node(current_,nodePosition)

			children.append(newNode)


		#loop the children list
		for child in children:
			#checks if the child is in the closed list
			for x in closedList:
				if child == x:
					continue
			#f,g,h values
			child.g = current_.g + 1
			child.h = ((child.position[0] - endNode.position[0]) ** 2) + ((child.position[1] - endNode.position[1]) ** 2)
			child.f = child.g + child.h

			#if the child is already n the open lsit
			for openNode in openList:
				if child == openNode and child.g > openNode.g:
					continue
			#then add the child to the open list 
			openList.append(child)


def MakePath(maze,path):
	#prints the path 
	for i in range(len(maze)):
		for j in range(len(maze)):
			if (i,j) in path:
				maze[i][j] = 3



if __name__ == "__main__":
	maze = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

	start = (0, 0)
	end = (9,6)

	print("Welcome to my A* search algorithm :) ")

	path = A_Star(start,end,maze)

	print("The shortest path starting at position {} is ...".format(start))
	print("Path: {}".format(path))
	print("The maze visual... ")
	
	#prints the path
	MakePath(maze,path)

	#prints the path
	for i in range(len(maze)):
		print(maze[i])
























