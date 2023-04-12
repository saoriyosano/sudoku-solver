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


                        