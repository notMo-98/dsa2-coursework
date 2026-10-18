import matplotlib.pyplot as plt
import numpy as np
import random as rdm
mazeimg = plt.imread ('maze(1).png') 
grid = mazeimg[5::10, 5::10, 0]


def get_neighbours (row, col):
    open_neighbours = []
    mvnt_directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for d_row, d_col in mvnt_directions:
        new_row = row + d_row
        new_col = col + d_col

        if new_col in range (0,21) and new_row in range (0,21):
            if grid[new_row, new_col] == 1:
                open_neighbours.append ((new_row,new_col))
    return open_neighbours


for row in grid:
    line = ""
    for cell in row:
        if cell == 0:
            line = line + "#"
        else:
            line = line + " "
    print(line)

start_col = int(np.where(grid[0] == 1)[0][0])
start = (0,start_col)
end_col = int(np.where(grid[-1] == 1)[0][0])
end = (20, end_col)


choice = input ('Which method would you like to use Las Vegas (L) or Backtracking (B) ? ').strip().upper()
while choice not in ("B", "L"):
    print ("Please choose which method to use")
    choice = input ('Which method would you like to use Las Vegas (L) or Backtracking (B) ? ').strip().upper()
print ("You have chosen method:", choice)

current_pos = (start)
row, col = current_pos
mvmnt_option = get_neighbours(row, col)
chosen_move = rdm.choice(mvmnt_option)


move_count = 0 
visited_blocks = [start]
current_pos = chosen_move
visited_blocks.append(chosen_move)
move_count = move_count + 1

print (current_pos,move_count,visited_blocks)