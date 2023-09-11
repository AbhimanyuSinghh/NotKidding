def printNos(x: int): 
    # Write your code here
   
    if x == 0:
        return []
    result = printNos(x-1)
    result.append(x)
    return result