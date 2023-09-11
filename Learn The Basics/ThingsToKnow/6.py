## Note : For printing multiple values in one line, put them inside print separated by space.
## You can follow this syntax for printing values of two variables val1 and val2 separaetd by space -
## print(val1, " ", val2)
def sum(n):
    m = n
    sumE = 0
    sumO = 0
    while m!=0:
        dig = m%10
        if dig %2 == 0:
            sumE += dig
        else:
            sumO += dig
        m//=10
    print(sumE, " ", sumO)


number = int(input())
sum(number)