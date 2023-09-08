'''
1 2 3 4 5
1 2 3 4
1 2 3 
1 2  
1 

'''

def printTriangle(self, N):
        # Code here
        for i in range(N, 0 , -1):
            for j in range(i):
                print(j+1, end = ' ')
            print()
