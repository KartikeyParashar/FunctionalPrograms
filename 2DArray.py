rows = int(input("Enter number of Rows: "))
columns = int(input("Enter number of columns: "))

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