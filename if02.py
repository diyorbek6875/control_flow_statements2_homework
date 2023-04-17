def main(a,b,c):
    """
    Find the smallest of the numbers.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    e=0
    if a<b<c or a<c<b:
        e=a
    
    if b<a<c or b<c<a:
        e=b
    
    if c<b<a or c<a<b:
        e=c


    return e
a=int(input("son kirit "))
b=int(input("son kirit "))
c=int(input("son kirit "))
print(main(a,b,c))