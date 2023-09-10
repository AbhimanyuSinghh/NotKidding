def countDigits(n: int) -> int:
    count = 0
    num = n
    while(num!=0):
        p= num%10
        if(p!=0 and n%p==0):
            count+=1
        num//=10
    return count