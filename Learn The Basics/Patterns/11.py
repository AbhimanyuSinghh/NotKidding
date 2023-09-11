'''
1
0 1
1 0 1
0 1 0 1
1 0 1 0 1

'''

def printTriangle(self, N):
        # Code here
        for i in range(0, N):
            for j in range(0, i+1):
                if (i+j)%2 == 0:
                    print('1', end = ' ')
                else:
                    print('0', end = ' ')
            print()