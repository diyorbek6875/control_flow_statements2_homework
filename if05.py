def main(n):
    """
    Find the largest digit of the five-digit number.
    Args:
        n: Five-digit number.
    Returns:
        int: return answer.
    """
    "78945"
    a=n//10000
    b=n//1000%10
    c=n//100%100%10
    d=n%1000//10%10
    e=n%10000%1000%100%10
    m=a
    if b>m:
        m=b
    if c>m:
        m=c
    if d>m:
        m=d
    if e>m:
        m=e
    return m
n=int(input("5 xonali son  "))
print(main(n))