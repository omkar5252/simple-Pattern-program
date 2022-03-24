# Problem No : 6

for i in range(1,6):
    for j in range(i,8-2):
        if (i==1 or j==5 or i==j):
            print(j,end=" ")
        else:
            print(" ",end=" ")
    print()