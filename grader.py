
import math

def polysum(n, s):
    """
        input: 1. n - no. of sides of polygon
               2. s - length of sodes of polygon
               
        output : 3. sum - sum of area and square of perimeter of polygon where
                        area - (0.25*n*s*s)/(tan(p1/n))
                        perimeter - n*s
                        
    """
    area = (0.25 * n * (s ** 2)) / (math.tan(math.pi / n))
    perimeter = n * s
    sum = area + (perimeter ** 2)
    # round(value, rounding_digits) - to round of to given decimal digits
    return round(sum, 4)