def main(a,b,c):
    """
    Determine the number between large and small.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    e=0
    if a>b>c or c>b>a:
        e=b
    if a>c>b or b>c>a:
        e=c
    if b>a>c or c>a>b:
        e=a
    return e
a=int(input())
b=int(input())
c=int(input())

print(main(a,b,c))