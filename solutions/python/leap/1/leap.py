def leap_year(year):
    """
    if year % 4 == 0 and not (year % 100 == 0):
        return true
    elif year % 400 == 0:
        return true
    else:
        return false
    """
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)