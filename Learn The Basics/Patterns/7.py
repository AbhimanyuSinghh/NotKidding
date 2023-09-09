'''
    *
   ***  
  *****
 *******
*********

'''







def printTriangle(self, N):
        # Code here
        for i in range(0, N):
            for j in range(0, N-i-1):
                print(' ', end = '')
            for k in range(0, i+1):
                print('*', end = '')
            for l in range(0, i):
                print('*', end="")
            print()