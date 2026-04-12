# placeholder, say x and y are the Fix-point Numbers
x = 12.4321
y = 13.654321
# x and y gets split into integers a--->(x1.x2) can be changed
x1 = 12
x2 = "4321"
y1 = 13 
y2 = "654321"

def Add(x1, x2, y1, y2):
    """
    The function takes the integer and fractional parts of two fixed-point numbers and adds them together.

    Parameters: 
    x1 (int): integer part of first number
    x2 (str): fractional part of first number
    y1 (int): integer part of second number
    y2 (str): fractional part of second number
    
    Example:
    Operation to be processed: 12.34 + 567.789
    Call the function like this "Add(12, "34", 567, "789")"

    Returns:
    Fixedc1: integer part of the result
    Fixedc2: fractional part of the result
    """
    # calculation of whole part
    c1 = x1 + y1

    # calculation of fractional part, match their decimal place

    while len(x2) < len(y2):
        x2 += "0"
    while len(x2) > len(y2):
        y2 += "0"

    DecLen = len(x2) # Decimal Length, saved for later, (x2 can be y2, whichever is fine)

    c2 = int(x2) + int(y2) # Convert strings x2 and y2 into integer for addition
    PreOutputc2 = str(c2) # turn c2 into a string for slicing when carryover happens
    
    if len(PreOutputc2) > DecLen: # carryover has happened and c2 is longer than x2/y2
        Fixedc2 = PreOutputc2[1:]
        Fixedc1 = c1 + 1
    elif len(PreOutputc2) < DecLen: # c2 is shorter than x2/y2, add the missing leading 0s
        Fixedc2 = "0"*(DecLen-len(PreOutputc2)) + PreOutputc2
        Fixedc1 = c1
    else:                  # there is no carryover TO INTEGER PART
        Fixedc2 = PreOutputc2
        Fixedc1 = c1
    return(Fixedc1, Fixedc2)