def main(a,b,c):
    """
    Find the largest of the numbers.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    e=0
    if a>b>c:
        e==a
    if b>a>c:
        e==b
    if c>a>b:
        e==c


    return c
a=int(input("son kirit "))
b=int(input("son kirit "))
c=int(input("son kirit "))
print(main(a,b,c))