from validator import sudoku_validator

def get_candidates(grid, rownum, colnum):
        
    candidates = list(range(1, 10))

    # get row for rownum/colnum provided
    cur_row = [item for item in grid[rownum] if item > 0]
    
    # get column for rownum/colnum provided
    cur_column = [grid[i][colnum] for i in range(9) if grid[i][colnum] > 0]
    
    # get minigrid for rownum/colnum provided
    cur_rownums = [rownum // 3 * 3, rownum // 3 * 3 + 1, rownum // 3 * 3 + 2]
    cur_colnums = [colnum // 3 * 3, colnum // 3 * 3 + 1, colnum // 3 * 3 + 2]
    cur_minigrid = [grid[cur_rownum][cur_colnum] for cur_colnum in cur_colnums for cur_rownum in cur_rownums if grid[cur_rownum][cur_colnum] > 0]
    
    existing = set(cur_row + cur_column + cur_minigrid)
    candidates = [candidate for candidate in candidates if candidate not in existing]
    
    return candidates

def search(grid):
    
    if sudoku_validator(grid):
        return True
    
    for rownum, row in enumerate(grid):
            for colnum, item in enumerate(row):
                if item == 0:
                    for candidate in get_candidates(grid, rownum, colnum):
                        grid[rownum][colnum] = candidate
                        is_solved = search(grid)
                        if is_solved:
                            return True
                        else:
                            grid[rownum][colnum] = 0
                    return False
    return True
