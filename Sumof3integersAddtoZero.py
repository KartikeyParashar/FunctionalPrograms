l = [1, -1, 2, -3, 4, -5, -2, 6, -6, 7]
for i in l:
  for j in l:
    for k in l:
      if i + j + k == 0:
        print(f"{i},{j},{k}")