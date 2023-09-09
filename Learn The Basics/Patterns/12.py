'''
1                 1
1 2             2 1
1 2 3         3 2 1
1 2 3 4     4 3 2 1
1 2 3 4 5 5 4 3 2 1

'''





def printTriangle(self, N):
        # Code here
        for i in range(0, N):
            for j in range(0, i+1):
                print(j+1, end = ' ')
            for k in range(0, N-i-1):
                print(' ', end= ' ')
            for l in range(0, N-i-1):
                print(' ', end = ' ')
            for m in range(i+1, 0, -1):
                print(m, end= ' ')
            print()