class Solution:
    def isArmstrong(self, n: int):
        strg = str(abs(n))
        c = 0
        for i in strg:
            c+=1
        arm = 0
        for i in strg:
            arm = arm + (int(i))**c
        if n==arm:
            return True

        else:
            return False
        