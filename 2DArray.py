# 2D Array
# a. Desc ­> A library for reading in 2D arrays of integers, doubles, or booleans from
# standard input and printing them out to standard output.
# b. I/P ­> M rows, N Cols, and M * N inputs for 2D Array. Use Java Scanner Class
# c. Logic ­> create 2 dimensional array in memory to read in M rows and N cols
# d. O/P ­> Print function to print 2 Dimensional Array. In Java use PrintWriter with
# OutputStreamWriter to print the output to the screen.

try:
  rows = int(input("Enter number of Rows: "))
  columns = int(input("Enter number of columns: "))
except ValueError:
  print("plz enter valid input")
def twoD_array(rows, columns):
  array = []
  for i in range(rows):
    row = []
    for j in range(columns):
      value = int(input("Enter the value: "))
      row.append(value)
    array.append(row)
  return array

print(twoD_array(rows,columns))    
