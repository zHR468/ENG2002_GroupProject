class fixNum:
 
    """
    The core idea is to represent the number as a fixed-point number with a certain number of fractional digits.
    In function,
    a will be the integer part,
    and b will be the fractional part.
    b_len stores how many digits b has (for aligning decimals when adding later).
    """
    
    def __init__(self, a, b):
        #read the very original length of b
        b_len_start = str(b)
 
        """
         count the number of digits in b, store as self.b_original_len
         if b is negative, it would start with '-', then the length would count the icon '-';
         so we need to make it length minus 1 in order to count the numbers correctly
        """
        
        
        #remove the extra zeros that do not need
        b_len_start = b_len_start.rstrip('0')
        if b_len_start == "" or b_len_start == "-":

            b_len_start += "0"


        if b_len_start[0] == "-":
            self.b_original_len = len(b_len_start) - 1
        else:
            self.b_original_len = len(b_len_start)
            
        # force a and b to be integers
        self.a = int(a)
        self.b = int(b_len_start)
 
        # In the assignment: if a is non-zero, b must be positive.
        if self.a != 0:
            self.b = abs(self.b)
        
    def __str__(self):
        # format will be "a.b"
        a_part = str(self.a)
        b_str = str(abs(self.b))
 
        #add the zeros b_part lost when set into int value
        b_part = "0" * (self.b_original_len - len(b_str)) + b_str
        # catch the special negative zero case (e.g., -0.48)
        if self.a == 0 and self.b < 0:
            return "-" + a_part + "." + b_part
        else:
            return a_part + "." + b_part
 
    def add(self, other):
        """
        Adds this fixed-point number with another fixed-point number.
        Returns the result as a new fixNum object.
        """
        # get fractional parts as strings, padded with leading zeros
        x2 = "0" * (self.b_original_len - len(str(abs(self.b)))) + str(abs(self.b))
        y2 = "0" * (other.b_original_len - len(str(abs(other.b)))) + str(abs(other.b))
 
        # match decimal places by adding zeros to the shorter one
        while len(x2) < len(y2):
            x2 += "0"
        while len(x2) > len(y2):
            y2 += "0"
 
        DecLen = len(x2)
        scale = 10 ** DecLen
 
        # combine integer and fractional parts into one scaled integer
        ScaledX = abs(self.a) * scale + int(x2)
        ScaledY = abs(other.a) * scale + int(y2)
 
        # apply the sign
        if self.a < 0 or (self.a == 0 and self.b < 0):
            ScaledX = -ScaledX
        if other.a < 0 or (other.a == 0 and other.b < 0):
            ScaledY = -ScaledY
 
        PreOutput = ScaledX + ScaledY
 
        # split back into integer and fractional parts
        int_part = PreOutput // scale
        remainder = PreOutput % scale
 
        # handle negative results
        if PreOutput < 0 and remainder != 0:
            int_part += 1                        # integer division rounds down, add 1 to offset error
            frac_part = scale - remainder
            if int_part == 0:
                frac_part = -frac_part
        else:
            frac_part = remainder
 
        frac_str = "0" * (DecLen - len(str(abs(frac_part)))) + str(abs(frac_part))
        if frac_part < 0:
            frac_str = "-" + frac_str
        return fixNum(int_part, frac_str)

    def power(self, n):
        """
        Raises this fixed-point number to integer power n.
        Returns the result as a new fixNum object.
        """
        # get fractional parts as strings, padded with leading zeros
        x2 = "0" * (self.b_original_len - len(str(abs(self.b)))) + str(abs(self.b))
 
        DecLen = len(x2)
        scale = 10 ** DecLen
 
        # combine integer and fractional parts into one scaled integer
        ScaledX = abs(self.a) * scale + int(x2)
 
        # apply the sign
        if self.a < 0 or (self.a == 0 and self.b < 0):
            ScaledX = -ScaledX
 
        PreOutput = ScaledX ** n
        scale = scale ** n
 
        # split back into integer and fractional parts
        int_part = PreOutput // scale
        remainder = PreOutput % scale
 
        # handle negative results
        if PreOutput < 0 and remainder != 0:
            int_part += 1
            frac_part = scale - remainder
            if int_part == 0:
                frac_part = -frac_part
        else:
            frac_part = remainder
 
        frac_str = "0" * (len(str(scale)) - 1 - len(str(abs(frac_part)))) + str(abs(frac_part))
        if frac_part < 0:
            frac_str = "-" + frac_str
        return fixNum(int_part, frac_str)