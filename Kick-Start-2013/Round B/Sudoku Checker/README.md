# Sudoku 
#
# First
#Since the initial t value tells us how many inputs we have, we loop that value. 
#
# Second 
#We ensure that the desired value of n is obtained in the loop, we set the sentence that can give the desired output and add the Solution function to it.
#
# Now let's write the function 
# First
#Let's create a value for the 2 dimensional list to be entered. 
#Let's create a for loop to get the inputs of the 2D array. And let's add input to add data to this array. 
#Let's set the loop to rotate the square of the value N    because as it says in the question, every 4 sides are n2.
#To split these initial value rows into columns, we need to add .split() to input() .
#Let's get the 2d list by adding this entry we have prepared to array.append().
#
# Second
#Here we create the variable x, which will be useful below.
#To understand that the numbers in the 2D list are sudoku appropriate, we create 2 nested loops.
#In condition blocks, we stipulate that the value must be between 0 and (n ^ 2) +1, otherwise the variable X will be "true".
#(n ^ 2) +1 says that the value of n in the question varies between 3 and 6, so the numbers that will be inside can also go from 1 to 10 or from 1 to 36
#
# Third
#Now we continue from row 12 for row column control.
#We open a loop to rotate each row or column.
#We create hbox and vbox lists for rows and columns 
#We create the array2d-list to check inside small squares with N sides.
#We open a loop to extract the data in the row and column.
#Here we add the data to the x and y lists.
#We get out of the inner loop and create another loop. Here we are looking at each variable to control the numbers in the row and column.
#Then, with the condition block, we check if the variable is more than 1 in the list, 
#if it is more than 1, we ask X to return "true" and break its loop.
#We're leaving the main loop
#
# Fourth
