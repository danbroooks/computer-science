
def f(x):
    import math
    return 10*math.e**(math.log(0.5)/5.27 * x)

def radiationExposure(start, stop, step):
    '''
    Computes and returns the amount of radiation exposed
    to between the start and stop times. Calls the 
    function f (defined for you in the grading script)
    to obtain the value of the function at any point.
 
    start: integer, the time at which exposure begins
    stop: integer, the time at which exposure ends
    step: float, the width of each rectangle. You can assume that
      the step size will always partition the space evenly.

    returns: float, the amount of radiation exposed to 
      between start and stop times.
    '''
    pos = start
    amount = 0
    while (pos < stop):
        r = f(pos)
        amount += (step*r)
        pos += step

    return amount

def check(val, eq):
    return round(val, 2) == round(eq, 2)

print(check(
    radiationExposure(0, 5, 1),
    39.10318784326239
))

print(check(
    radiationExposure(5, 11, 1),
    22.94241041057671
))

print(check(
    radiationExposure(0, 11, 1),
    62.0455982538
))

print(check(
    radiationExposure(40, 100, 1.5),
    0.434612356115
))
