def fib(self, n: int):
        if n<=1:
            return n
        
        #return self.fib(n-1) + self.fib(n-2)

        seq = [0]*(n+1)
        seq[1]= 1
        for i in range(2, n+1):
            seq[i] = seq[i-1] + seq[i-2]
        return seq[n]
        