def reverse(self, x: int) :
        strg = str(abs(x))
        if x>0:
            rev = int(strg[::-1])
        else:
            rev = -1 * int(strg[::-1])
        mini = -2**31
        maxi = 2**31 -1
        if rev not in range(mini, maxi):
            return 0
        else:
            return rev