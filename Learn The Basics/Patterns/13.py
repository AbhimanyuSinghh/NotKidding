'''
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15

'''


def printTriangle(self, N):
        # Code here
        count = 1
        for i in range(0, N):
            for j in range(0, i+1):
                print(count, end = ' ')
                count+=1
            print()
