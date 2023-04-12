from helper import get_rows, get_columns, get_mini_grids

def check_complete(grid):
    nums = list(range(1, 10))
    while len(nums) > 0:
        for num in grid:
            if num in nums:
                nums.remove(num)
            else:
                return False
    return True

def sudoku_validator(grid):
    # check rows
    rows = check_complete(get_rows(grid))

    # check columns
    columns = check_complete(get_columns(grid))

    # check 3x3 grids
    minigrids = check_complete(get_mini_grids(grid))
    
    if rows and columns and minigrids:
        return True
    else:
        return False