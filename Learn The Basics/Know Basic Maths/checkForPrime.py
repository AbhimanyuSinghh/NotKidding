
def sumOfAllDivisors(n: int) -> int:
    # Write your code here
    
    totalSum = 0
    
    for i in range(1, n+1):
        divisorSum = 0
        for j in range(1, i+1):
            if(i%j==0):
                divisorSum += j
        totalSum += divisorSum

    return totalSum