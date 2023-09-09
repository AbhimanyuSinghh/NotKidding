'''
ABCDE
ABCD
ABC
AB
A

'''


def printTriangle(self, N):
        # Code here
        letter = 'A'
        for i in range(0, N):
            for j in range(0, N-i):
                print(chr(ord(letter) + j),end="")
            print()
