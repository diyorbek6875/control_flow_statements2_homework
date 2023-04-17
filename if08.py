def main(number):
    """
    Return the days of the week, return the days of the week according to the numbers 1 to 7.
    Use the elif statments.
    1: "Monday"
    2: "Tuesday"
    3: "Wednesday"
    4: "Thursday"
    5: "Friday"
    6: "Saturday"
    7: "Sunday"
    Args:
        number: Number of the day.
    Returns:
        str: return answer.
    """
    if number==1:
        a ="Monday"
    elif number==2:
        a="Tuesday"
    elif number==3:
        a="Wednesday"
    elif number==4:
        a="Thursday"
    elif number==5:
        a="Friday"
    elif number==6:
        a="Saturday"
    elif number==7:
        a="Sunday"
    return a
number=int(input())
print(main(number))