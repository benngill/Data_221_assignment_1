def secondsSinceMidnightToStandard12HourTime(secondsSinceMidnight):
    if type(secondsSinceMidnight) != int or secondsSinceMidnight <0: # checks input and returns error if invalid
        return "ERROR: input must be a positive integer"
    AMorPM = "AM"
    hours = secondsSinceMidnight//3600 # seconds to hours
    if hours > 12: # AM or PM toggle
        hours = hours - 12
        AMorPM = "PM"
    hoursRemainder = secondsSinceMidnight%3600
    minutes = hoursRemainder//60 # remaining seconds to minutes
    minutesRemainder = hoursRemainder%60
    seconds = minutesRemainder # remaining seconds
    twelveHourTime = f"{hours}:{minutes}:{seconds}:{AMorPM}" # formats string for return
    return twelveHourTime

seconds = 3600*6+60*52+19
secondsSinceMidnightToStandard12HourTime()