def main(n):
    """
    Find the index of the largest digit of the five-digit number.
    Args:
        n: Five-digit number.
    Returns:
        int: return answer.
    """
    a=n//10000
    b=n//1000%10
    c=n//100%100%10
    d=n%1000//10%10
    e=n%10000%1000%100%10
    m=a
    index =5
    if b>m:
        m=b
        index =4

    if c>m:
        m=c
        index = 3

    if d>m:
        m=d
        index=2
    if e>m:
        m=e
        index=1
    return index
n=int(input("5 xonali son  "))
print(main(n))




