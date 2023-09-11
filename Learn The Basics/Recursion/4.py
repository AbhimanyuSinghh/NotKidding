def printNos(x: int):
    # Write your code here
    
    # Write your code here
    result = []
   
    if x<=0:
        return []
    result.append(x)
    printNos(x-1)
    
    return result