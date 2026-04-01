# placeholder, say x and y are the userinputs
x = 12.4321
y = 13.654321
# x and y gets split into integers a--->(x1.x2) can be changed
x1 = 12
x2 = 4321
y1 = 13 
y2 = 654321

def Add(x1, x2, y1, y2):
    # calculation of whole part
    c1 = x1 + y1

    # calculation of fractional part, match their decimal place

    if len(str(x2)) < len(str(y2)):
        x2 *= 10**(len(str(y2))-len(str(x2)))
    elif len(str(x2)) > len(str(y2)):
        y2 *= 10**(len(str(x2))-len(str(y2)))

    ODL = len(str(x2)) # Original Decimal Length, saved for later, (x2 can be y2, whichever is fine)

    c2 = x2 + y2
    PreOutputc2 = str(c2) # turn c2 into a string for slicing when carryover happens
    
    if len(str(c2)) > ODL: # carryover has happened and c2 is longer than x2/y2
        Fixedc2 = PreOutputc2[1:]
        Fixedc1 = str(c1 + 1)
    else:                  # carryover has NOT happened and c2 is NOT longer than x2/y2
        Fixedc2 = PreOutputc2
        Fixedc1 = str(c1)
    return(Fixedc1, Fixedc2)