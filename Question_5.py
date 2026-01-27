import math

def percentOfAreaOfLargerCircleThatSmallerCircleCovers(radiusOfCircle1, radiusOfCircle2):
    if radiusOfCircle1 > 0 and radiusOfCircle2 > 0: # validates both radii are positive integers
        areaOfCircle1 = math.pi*(radiusOfCircle1**2) # comuptes area of circle1
        areaOfCircle2 = math.pi*(radiusOfCircle2**2) # comuptes area of circle2
        percentOfCircleCovered = None
        if areaOfCircle1 > areaOfCircle2: # checks which circle is larger
            percentofCircleCovered = areaOfCircle2 / areaOfCircle1
        else:
            percentofCircleCovered = areaOfCircle1 / areaOfCircle2
        return percentofCircleCovered # returns percent of area covered
    else:
        return "ERROR: one or more of the provided radii are not positive integers" # returns meaningful message

percentOfAreaOfLargerCircleThatSmallerCircleCovers(10,8)