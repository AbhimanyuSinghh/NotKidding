'''
A
BB
CCC
DDDD
EEEEE

'''

def printTriangle(self, N):
        # Code here
        for i in range(0, N):
            for j in range(0, i+1):
                print(chr(65+i), end = '')
            print()