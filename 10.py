# Homework problem
'''
* * * * * * * * *
  *           *
    *       *
      *   *
        *
'''
for i in range(5):
    for j in range(9):
        if (i==0) or (i==j) or (j+i==8):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

