'''
1
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5
'''

def printTriangle(self, N):
        # Code here
        for i in range(0, N):
            for j in range(0, i+1):
                print(i+1, end = ' ')
            print()