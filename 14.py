'''
*           *
* *       * *
* * *   * * *
* * * * * * *
'''
for row in range(4):
    for col in range(7):
        if row==3 or col==6 or col==0 or (col==1 and row>0 and row<3) or (col==5 and row>0 and row<3) or (col==2 and row>1 and row<3) or (col==4 and row>1 and row<3):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
