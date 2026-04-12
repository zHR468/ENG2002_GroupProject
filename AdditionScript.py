def Add(x1, x2, y1, y2):
    """
    Adds two fixed-point numbers given as integer and fractional parts.
    Works with both positive and negative inputs.

    Parameters:
    x1 (int): integer part of first number
    x2 (str): fractional part of first number
    y1 (int): integer part of second number
    y2 (str): fractional part of second number

    Returns:
    (int_part, frac_str): tuple of integer and fractional parts of the result
    """

    # calculation of fractional part, match their decimal place

    while len(x2) < len(y2):
        x2 += "0"
    while len(x2) > len(y2):
        y2 += "0"
        
    DecLen = len(x2) # Decimal Length, saved for later, (x2 can be y2, whichever is fine)
    scale = 10**DecLen

    ScaledX = abs(x1) * scale + int(x2)
    ScaledY = abs(y1) * scale + int(y2)
    
    if x1 < 0:
        ScaledX = -ScaledX
    if y1 < 0:
        ScaledY = -ScaledY
        
    PreOutput = ScaledX + ScaledY

    # Split back into integer and fractional parts
    int_part = PreOutput // scale  
    remainder = PreOutput % scale
    # Since // rounds down and doesn't work properly with negative numbers
    if PreOutput < 0 and remainder != 0:
        int_part += 1
        frac_part = scale - remainder
    else:
        frac_part = remainder
    frac_str = "0"*(DecLen-len(str(frac_part))) + str(frac_part)
    return int_part, frac_str

#Tests
#print(Add(12, "34", 567, "789"))     # 12.34 + 567.789  = (580, '129')
#print(Add(-12, "34", 567, "789"))    # -12.34 + 567.789 = (555, '449')
#print(Add(12, "34", -567, "789"))    # 12.34 - 567.789  = (-555, '449')
#print(Add(-12, "34", -567, "789"))   # -12.34 - 567.789 = (-580, '129')