# Homework problem
'''
        *
      *   *
    *       *
  *           *
* * * * * * * * *
'''
for i in range(5):
    for j in range(9):
        if (i==4) or (i+j==4) or (j-i==4):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

