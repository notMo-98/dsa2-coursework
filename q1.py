import matplotlib.pyplot as plt
import numpy as np
mazeimg = plt.imread ('maze(1).png') 
grid = mazeimg[5::10, 5::10, 0]
print(grid.shape)

for row in grid:
    line = ""
    for cell in row:
        if cell == 0:
            line = line + "#"
        else:
            line = line + " "
    print(line)

print(grid[0])
np.where(grid[0] == 1)

start_col = int(np.where(grid[0] == 1)[0][0])
print(start_col)
start = (0,start_col)
print (start)
end_col = int(np.where(grid[-1] == 1)[0][0])
end = (20, end_col)
print(end_col)
print(end)

