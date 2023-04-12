import itertools

def get_rows(grid):
    return [row for row in grid]

def get_columns(grid):
    return [[row[i] for row in grid] for i in range(9)]

def get_mini_grids(grid):
    smallgrids = []
    num_x = 0
    num_y = 3
    index = 0
    for i in range(len(grid)):
        smallgrid= []
        for i in range(3):
            smallgrid.append(grid[index][num_x:num_y])
            index += 1
        smallgrid = list(itertools.chain(*smallgrid))
        smallgrids.append(smallgrid)
        if index == 9:
            num_x += 3
            num_y += 3
            index = 0
            
    return smallgrids

def input_to_grid(*args):
    ret = []
    # columns to rows
    for i in range(9):
        ret.append([0 if arg[i]=="" else int(arg[i]) for arg in args])
    return ret

def grid_to_input(grid):
    ret = []
    # rows to columns
    for i in range(9):
        ret.append(["" if row[i]==0 else row[i] for row in grid])
    return ret        