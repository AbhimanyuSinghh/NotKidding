'''
    *
   * *
  * * *
 * * * *
* * * * *
* * * * *
 * * * *
  * * *
   * *
    *

'''


def printDiamond(self, N):
        self.print_upper_stars(N)
        self.print_lower_stars(N)
        # Code here
def print_upper_stars(self,N):
        for i in range(0,N):
            # space
            for j in range(N-i-1):
                print(" ",end="")
                
            # stars
            for k in range(i+1):
                print("*",end=" ")
                
            # space
            # for j in range(N-i):
            #     print(" ",end=" ")
                
            print()
    
            
def print_lower_stars(self,N):
        # space
        for i in range(N,0,-1):
            # space
            for j in range(N-i):
                print(" ",end="")
                
            # stars
            for k in range(i):
                print("*",end=" ")
                
            print()