# ----------
# User Instructions:
# 
# Define a function, search() that returns a list
# in the form of [optimal path length, row, col]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space

grid = [[0, 0, 1, 0, 0, 0],
		[0, 0, 1, 0, 0, 0],
		[0, 0, 0, 0, 1, 0],
		[0, 0, 1, 1, 1, 0],
		[0, 0, 0, 0, 1, 0]]
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1 # Cost of each mouvement

delta = [[-1, 0], # go up
		 [ 0,-1], # go left
		 [ 1, 0], # go down
		 [ 0, 1]] # go right

delta_name = ['^', '<', 'v', '>']

def check_item(current_path_array, checked_grid):
	for path in current_path_array:
		if(len(path) == 3): # If g_value among current_path_array
			checked_grid[path[1]][path[2]] = -1
		else:
			checked_grid[path[0]][path[1]] = -1
	return checked_grid

def get_neighbour(pos, grid): 
	"""
	:param pos - 1D array posx and posy
	:param grid - 2D array 
	:return the neighbour of (case that touch) pos if inside grid and if neighbour not already checked (== -1)
	"""
	posx = pos[0]
	posy = pos[1]

	result = []
	for i in range(len(delta)): 
		# Check surroundings 
		x2 = posx + delta[i][0] 
		y2 = posy + delta[i][1]

		# If surroundings are within the grid
		if( (x2 >= 0 and x2 < len(grid)) and (y2 >=0 and y2 < len(grid[0])) ):
			# If surroundings are not already checked
			if(grid[x2][y2] != -1 and grid[x2][y2] != -1):
				result.append([x2, y2])
				check_item(result, grid)
	return result, grid

	
def search(grid, init, goal, cost):
	# Init values
	g_value = 0
	pos_x = init[0]
	pos_y = init[1]
	path_array = [[g_value, pos_x, pos_y]]
	checked_grid = grid
	
	# Check the already seen positions
	checked_grid = check_item(path_array, checked_grid)
	#print(checked_grid)

	# Get the surroundings neighbour of the current position
	neighbours, checked_grid = get_neighbour([pos_x, pos_y], checked_grid)
	print(checked_grid)


	return path_array

result = search(grid, init, goal, cost)
#print(result)

