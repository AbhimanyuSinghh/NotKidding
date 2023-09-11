'''
A
AB
ABC
ABCD
ABCDE

'''





def printTriangle(self, N):
        # Code here
         letter = 'A'
         for i in range(0,N):
            for j in range(0,i+1):
                print(chr(ord(letter) + j),end="")
            print()