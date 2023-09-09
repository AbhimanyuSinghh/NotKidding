'''
**********
****  ****
***    ***
**      **
*        *
*        *
**      **
***    ***
****  ****
**********

'''


def printTriangle(self, N):
        # Code here
        n=N
        for i in range(0, n):
            for j in range(n-i, 0, -1):
                print('*', end= '')
            for a in range(0, i):
                print(' ', end='')
            for k in range(0,i):
                print(' ', end='')
            for l in range(n-i, 0 , -1):
                print('*', end='')
            print()
        for t in range(0, n):
            
            for d in range(0, t+1):
                print('*', end ='')
            
            for e in range(0, n-t-1):
                print(' ', end='')
            for f in range(0, n-t-1):
                print(' ', end='')
            for g in range(0, t+1):
                print('*', end ='')
            print()