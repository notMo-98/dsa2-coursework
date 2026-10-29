import matplotlib.pyplot as plt
import numpy as np
import random as rdm
mazeimg = plt.imread ('maze(1).png') 
grid = mazeimg[5::10, 5::10, 0]


def get_neighbours (row, col): # Checks the nearest open neighbours to the current position in the maze  
    open_neighbours = []
    mvnt_directions = [(1, 0), (0, -1), (-1,0), (0, 1)]
    for d_row, d_col in mvnt_directions:
        new_row = row + d_row
        new_col = col + d_col

        if new_col in range (0,21) and new_row in range (0,21): # sets a restriction on where the the new nearest neighbour could be and checks if it exists - 

            if grid[new_row, new_col] == 1: # checks the new square is inside the maze because row -1 is read as the last row of the grid and row 21 would crash 
                open_neighbours.append ((new_row,new_col))
    return open_neighbours

def las_vegas():
    current_pos = (start)
    row, col = current_pos
    move_count = 0 
    visited_blocks = [start]
    while move_count < 200 and current_pos != end: # keeps going  while ensuring 200 moves is never exceeded and the current position should not be at the end 
        row, col = current_pos
        mvmnt_option = get_neighbours(row,col)
        chosen_move = rdm.choice(mvmnt_option) # rdm used to allow the solver to use a random movement square to attempt to finish the maze
        current_pos = chosen_move
        visited_blocks.append(chosen_move) # adds the chosen move to the list of visited blocks 
        move_count = move_count + 1 #movement counter increments 
    sucess_run = current_pos == end
    return sucess_run,move_count, visited_blocks # returns the three values needed for creating the visual maze,checking if the solver was succesful and how many moves it needed 

def backtracking():
    step_count = 0 # steps are set at 0 first due to no moves being done
    mvmnt_path = [start] # sets where the solver starts the maze from 
    visited_blocks = [start] # adds the starting block to list of visited blocks 
    while mvmnt_path[-1] != end: # loop created until the end block is added to array
        current_block = mvmnt_path[-1] 
        row, col = current_block # sets the current block as the row and col it is currently at 
        mvmnt_options = get_neighbours(row,col)
        step_count = step_count + 1
        fresh_steps = []  #kept empty until further down where if the move has not been done before it gets added to this list 
        for item in mvmnt_options:
            if item not in visited_blocks:
                fresh_steps.append(item)
    
        if fresh_steps: # this bit of code checks if there is anywhere new for the solver to go 
            next_step = fresh_steps[0] # this decides which direction the solver should move in which is the first square in the list | steps are down, left, up, right
            mvmnt_path.append(next_step) # adds the next step to the movement path (route the solver is going in) which comes from get neighbour function
            visited_blocks.append(next_step) # adds the step taken to the list of visited blocks 
        else: #runs if there isnt anywhere new for the solver to go and does a 1 step back track then goes back to the while statement at the top
            mvmnt_path.pop() # removes the last move from the current route the solver is going in and take it back to the previous block
    sucess_run = mvmnt_path[-1] == end # success condition when the movement path is at the end block
    return sucess_run, step_count, visited_blocks # returns the three values needed for creating the visual maze,checking if the solver was succesful and how many moves it needed 


# creates the maze using the Hash symbol and the grid array which was created above
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





def methodology():
    choice = input ('Which method would you like to use Las Vegas (L) or Backtracking (B) ? ').strip().upper()
    while choice not in ("B", "L"): # keep asking until the user types B or L
        print ("Please choose which method to use")
        choice = input ('Which method would you like to use Las Vegas (L) or Backtracking (B) ? ').strip().upper() # asks again after a bad answer and stores the cleaned answer back into choice

    print ("You have chosen method:", choice) 

# using the three results below allows the solver in the test function to run 
    if choice == 'L':
        success, steps, visited = las_vegas() # calls the las vegas method function and runs the maze solver using that methodology

    else:
       success, steps, visited = backtracking() # calls the backtrack method function and runs the maze solver using that methodology


    if success:
        print ("The exit was found with... " , steps , "steps")
    else:
        print ("Run out of steps")
    plot_grid = grid.copy()
    for rows, cols in visited:
        plot_grid[rows,cols] = 2 # values 1 and 0 are used for the path and wall respectively hence 2 is used for the coloured visted squares 
       
    # creates the maze image and places the path taken ontop of this 
    plt.imshow(plot_grid) 
    plt.show()
    


#test funtion - runs both methods 10000 times and then gives a percentage of how successful each method is
def testruns(solver): #solver is a function that passed in and runs either of the functions added at the bottom 
    counter = 0 # set to 0 and increments with each sucessful run
    for i_ in range (10000):
        success, steps, visited = solver() # all three values are needed to be added here for the code to run without a crash otherwise only Sucess value is used
        if success: # condtion to increase counter when a run has completed sucessfully
            counter = counter + 1 # increment of the counter 
    return counter / 10000 * 100 # Percentage of sucessful runs 
print("Las Vegas success rate:", testruns(las_vegas)) # shows the the Las vegas sucess rate
print("Backtracking success rate:", testruns(backtracking)) # shows the back track sucess rate 

methodology()