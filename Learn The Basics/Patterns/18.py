'''
E
E D
E D C
E D C B
E D C B A

'''

def printTriangle(self, N):
        # Code here
        for i in range(0, N):
            for j in range(0, i+1):
                print(chr(65 + N -1 - j), end = ' ')
            print()
            