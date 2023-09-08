'''
1
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5
'''





def printTriangle(self, N):
        for i in range(0, N):
            for j in range(0, i+1):
                print(j+1, end = ' ')
            print()
