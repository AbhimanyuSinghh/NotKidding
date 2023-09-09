'''
*********
 *******
  *****
   ***
    *

'''





def printTriangle(self, N):
        # Code here
        for i in range(0, N):
            for j in range(0, i):
                print(' ', end = '')
            for k in range(0, N-i):
            
                print('*', end = '')
            for l in range(0, N-i-1):
                print('*', end = '')
            print()