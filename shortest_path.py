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
		checked_grid[path[1]][path[2]] = -1
	return checked_grid 

#def expands(current_path, checked_grid): 


def search(grid, init, goal, cost):
    # Init values
    g_value = 0
    pos_x = init[0]
    pos_y = init[1]
    path_array = [[g_value, pos_x, pos_y]]
    checked_grid = grid

    # Check the already seen positions
    checked_grid = check_item(path_array, checked_grid)    
    print(checked_grid)

    return path_array

#print(search(grid, init, goal, cost))
search(grid, init, goal, cost)