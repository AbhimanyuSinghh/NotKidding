'''
* 
* * 
* * * 
* * * * 
* * * * *
* * * *
* * *
* *
*

'''

def printTriangle(self, N):
        # Code here
        M= N-1
        for i in range(0, N):
            for j in range(0, i+1):
                print('*', end = ' ')
            print()
        for p in range(M, 0, -1):
            for q in range(0, p):
                print('*', end = ' ')
            print()