def countDigits(n: int) -> int:
    '''
    count = 0
    num = n
    while(num!=0):
        p= num%10
        if(p!=0 and n%p==0):
            count+=1
        num//=10
    return count
    '''
    count = 0
    num = str(n)
    for i in num:
        i = int(i)
        num = int(num)
        if i!=0 and num%i==0:
            count+=1
    return count