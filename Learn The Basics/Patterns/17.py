'''
   A
  ABA
 ABCBA
ABCDCBA

'''




def printTriangle(self, N):
        # Code here
        for i in range(0, N):
            for j in range(0, N-i-1):
                print(' ', end = '')
            for k in range(0, i+1):
                print(chr(65 + k), end = '')
            for l in range(i, 0, -1):
                print(chr(65 + l -1), end = '')
            print()