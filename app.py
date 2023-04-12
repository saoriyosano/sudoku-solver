import streamlit as st
import pandas as pd
from helper import input_to_grid, grid_to_input, get_rows, get_columns, get_mini_grids
from solver import get_candidates, search
from validator import sudoku_validator

st.title("Sudoku Solver :sleuth_or_spy:")

tab1, tab2 = st.tabs(["Solve our sample Sudoku", "Solve your own Sudoku"])

with tab2:
    st.markdown("""
        1. Type in numbers where numbers are fixed in Sudoku. Leave blank squares empty
        2. Press "Solve!" button
        3. The solution will appear at the bottom of the page
    """)
    
    solve = st.button("Solve!", key="own_solve")
    
    col0, col1, col2, col3, col4, col5, col6, col7, col8 = st.columns(9)
    
    with col0:
        # col0_values = [st.number_input("", min_value=1, max_value=9, step=1, format="%d", key=f"row_{x}_col_0") for x in range(9)]
        col0_values = [
            st.text_input("", value="", max_chars=1, key=f"row_{x}_col_0",) for x in range(9)
        ]
    with col1:
        col1_values = [
            st.text_input("", value="", max_chars=1, key=f"row_{x}_col_1",) for x in range(9)
        ]
    with col2:
        col2_values = [
            st.text_input("", value="", max_chars=1, key=f"row_{x}_col_2",) for x in range(9)
        ]
    with col3:
        col3_values = [
            st.text_input("", value="", max_chars=1, key=f"row_{x}_col_3",) for x in range(9)
        ]
    with col4:
        col4_values = [
            st.text_input("", value="", max_chars=1, key=f"row_{x}_col_4",) for x in range(9)
        ]
    with col5:
        col5_values = [
            st.text_input("", value="", max_chars=1, key=f"row_{x}_col_5",) for x in range(9)
        ]
    with col6:
        col6_values = [
            st.text_input("", value="", max_chars=1, key=f"row_{x}_col_6",) for x in range(9)
        ]
    with col7:
        col7_values = [
            st.text_input("", value="", max_chars=1, key=f"row_{x}_col_7",) for x in range(9)
        ]
    with col8:
        col8_values = [
            st.text_input("", value="", max_chars=1, key=f"row_{x}_col_8",) for x in range(9)
        ]
    
    if solve:
        grid = input_to_grid(
            col0_values, col1_values, col2_values, col3_values, col4_values, 
            col5_values,col6_values, col7_values, col8_values
        )
        search(grid)
        
        st.text("")
        st.text("")
        st.header(":bulb: Solution")
        st.table(grid)
    
with tab1:
    
    st.markdown("""
        1. Select sample Sudoku from the radio buttons below
        2. Press "Solve!" button
        3. The solution will appear at the bottom of the page
    """)

    sample_sudoku = st.radio(
        "Sudokus", 
        (1, 2, 3),
        horizontal = True
    ) - 1
    
    solve = st.button("Solve!", key="sample_solve")
    
    test_sudoku_1 = [
        [0,9,1,  3,0,0,  0,0,2],
        [0,2,0,  0,0,8,  9,4,0],
        [0,4,5,  0,0,9,  1,7,8],

        [4,0,9,  5,0,6,  0,3,0],
        [0,0,2,  0,0,7,  8,0,0],
        [5,3,8,  0,0,0,  4,0,7],

        [9,0,0,  8,0,5,  7,0,4],
        [6,8,0,  0,0,0,  0,1,0],
        [0,0,0,  7,0,1,  0,0,6]
    ]
    
    test_sudoku_2 = [
        [6,0,0,  0,0,0,  7,0,0],
        [0,4,0,  0,3,0,  0,6,5],
        [0,0,1,  0,0,8,  0,0,0],

        [0,6,0,  0,5,0,  0,3,9],
        [4,0,0,  6,0,0,  0,0,0],
        [0,0,0,  0,0,0,  0,2,0],

        [8,0,0,  0,0,3,  0,9,7],
        [0,0,0,  0,7,0,  4,0,0],
        [0,9,0,  0,0,0,  2,0,0]
    ]
    
    test_sudoku_3 = [
        [7,0,0,  0,0,0,  0,0,6],
        [0,0,0,  6,0,0,  0,4,0],
        [0,0,2,  0,0,8,  0,0,0],

        [0,0,8,  0,0,0,  0,0,0],
        [0,5,0,  8,0,6,  0,0,0],
        [0,0,0,  0,2,0,  0,0,0],

        [0,0,0,  0,0,0,  0,1,0],
        [0,4,0,  5,0,0,  0,0,0],
        [0,0,5,  0,0,7,  0,0,4]
    ]
    
    grids = [test_sudoku_1, test_sudoku_2, test_sudoku_3]
    input = grid_to_input(grids[sample_sudoku])
    print(input)
      
    col0, col1, col2, col3, col4, col5, col6, col7, col8 = st.columns(9)
    
    with col0:
        # col0_values = [st.number_input("", min_value=1, max_value=9, step=1, format="%d", key=f"row_{x}_col_0") for x in range(9)]
        col0_values = [
            st.text_input("", value=f"{input[0][x]}", max_chars=1, key=f"sample_row_{x}_col_0",) for x in range(9)
        ]
    with col1:
        col1_values = [
            st.text_input("", value=f"{input[1][x]}", max_chars=1, key=f"sample_row_{x}_col_1",) for x in range(9)
        ]
    with col2:
        col2_values = [
            st.text_input("", value=f"{input[2][x]}", max_chars=1, key=f"sample_row_{x}_col_2",) for x in range(9)
        ]
    with col3:
        col3_values = [
            st.text_input("", value=f"{input[3][x]}", max_chars=1, key=f"sample_row_{x}_col_3",) for x in range(9)
        ]
    with col4:
        col4_values = [
            st.text_input("", value=f"{input[4][x]}", max_chars=1, key=f"sample_row_{x}_col_4",) for x in range(9)
        ]
    with col5:
        col5_values = [
            st.text_input("", value=f"{input[5][x]}", max_chars=1, key=f"sample_row_{x}_col_5",) for x in range(9)
        ]
    with col6:
        col6_values = [
            st.text_input("", value=f"{input[6][x]}", max_chars=1, key=f"sample_row_{x}_col_6",) for x in range(9)
        ]
    with col7:
        col7_values = [
            st.text_input("", value=f"{input[7][x]}", max_chars=1, key=f"sample_row_{x}_col_7",) for x in range(9)
        ]
    with col8:
        col8_values = [
            st.text_input("", value=f"{input[8][x]}", max_chars=1, key=f"sample_row_{x}_col_8",) for x in range(9)
        ]

    if solve:
        grid = grids[sample_sudoku]
        search(grid)
        
        st.text("")
        st.text("")
        st.header(":bulb: Solution")
        st.table(grid)