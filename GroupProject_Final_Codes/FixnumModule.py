"""
prepared by :
MARY GORETTI ABWOOLI BIRUNGI (25100607D)
ELIF IREM TANIR(25088642d)
LI YUEN KIK (25087058D) - LAVISSE
HE YOUBIN(25091865D)
Purpose: 
Standard floating-point arithmetic introduces microscopic inaccuracies due to 
binary representation limits in computer architecture. This module engineers a 
rigorous fixed-point data structure. By decoupling the integer and fractional 
components and storing both strictly as pure integers, we bypass standard float 
limitations. The system utilizes dynamic scaling factors and structural memory 
to achieve mathematically lossless arithmetic operations (Addition and Power).
"""
import math

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
        #Prevent empty strings or standalone minus signs from breaking conversion
        b_len_start = b_len_start.rstrip('0')
        if b_len_start == "" or b_len_start == "-":

            b_len_start += "0"

        # Record the exact decimal length.
        # If negative, we subtract 1 to mathematically ignore the '-' icon.
        if b_len_start[0] == "-":
            self.b_original_len = len(b_len_start) - 1
        else:
            self.b_original_len = len(b_len_start)
            
        # force a and b to be integers
        self.a = int(a)
        self.b = int(b_len_start)
 
        # If the integer part (a) is non-zero, 
        # the fractional part (b) must be mathematically stored as absolute (positive).
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

        Parameters:
        fixNum object self
        fixNum object other

        Returns:
        fixNum(int_part, frac_str): fixNum object representing a fixed-point number
        """
        # get fractional parts as strings, padded with leading zeros that were lost during __init__
        x2 = "0" * (self.b_original_len - len(str(abs(self.b)))) + str(abs(self.b))
        y2 = "0" * (other.b_original_len - len(str(abs(other.b)))) + str(abs(other.b))
 
        # match decimal places by adding trailing zeros to the shorter one
        while len(x2) < len(y2):
            x2 += "0"
        while len(x2) > len(y2):
            y2 += "0"
 
        DecLen = len(x2)                 # number of decimal places (after padding)
        scale = 10 ** DecLen             # scaling factor to convert the fixed-point numbers into integers for addition
 
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
 
        # Since integer division rounds towards negative infinity, results need to be adjusted if PreOutput is negative
        if PreOutput < 0 and remainder != 0:
            int_part += 1                        # integer division rounds down, add 1 to offset error
            frac_part = scale - remainder        # Fix modulus result when input is negative
            if int_part == 0:
                frac_part = -frac_part
        else:
            frac_part = remainder
 
        frac_str = "0" * (DecLen - len(str(abs(frac_part)))) + str(abs(frac_part))
        if frac_part < 0:
            frac_str = "-" + frac_str
        return fixNum(int_part, frac_str)#result is then returned

    def power(self, n):
        """
        Raises the fixed-point number to integer power n.
        """

        if self.a == 0 and int(str(self.b).lstrip('-')) == 0:#checks if number is 0. we cannot raise 0 to any power
            return "Error: 0 cannot be raised to any power"

        k = len(str(self.b).lstrip('-'))# k is the length of b, the number of decimal places in the fixed-point number
        is_negative = (self.a < 0) or (self.a == 0 and str(self.b).startswith('-'))#we check if the original number is negative

        clean_b = str(self.b).lstrip('-')#we remove the negative sign from the decimal part for clean combination
        base = int(str(abs(self.a)) + clean_b)#we combine a and b into a single integer (we flatten it) eg 2.16 becomes 216

        if is_negative:#apply the negative sign if the number was initially a negative
            base *= -1

        if n == 0:#any number raised to the power of 0 is 1
            return fixNum(1, "0")

        # n is a positive power
        if n > 0:
            num = base ** n#we raise the base to power n
            den = 10 ** (k * n)#scaling factor to restore decimal places
            final_len = k * n #number of decimal places in the final answer

           # we split the number into integer a and decimal part b by using floor division and modulo respectively
            new_a = num // den 
            new_b = abs(num % den)

            #we convert the fractional part back into a string to handle leading 0s if needed
            new_b_str = str(new_b)
            #we add leading 0s if the new length of new_b is less than final_len
            while len(new_b_str) < final_len:
                new_b_str = '0' + new_b_str

            return fixNum(new_a, new_b_str)#result is then returned

        # n is a negative power
        else:
            abs_n = abs(n)#convert n to positive

            precision = k#controls the number of decimal places in the result

            #we scale the numerator to prevent the result from becoming 0
            num = (10 ** (k * abs_n)) * (10 ** precision)
            #the denominator is the base raised to the absolute power n
            den = base ** abs_n

            total_result = num // den#we perform integer division

            #we split the result into the inegral part a and the decimal part b
            new_a = total_result // (10 ** precision)
            new_b = total_result % (10 ** precision)

            #we convert the fractional part back into a string to handle leading 0s if needed
            new_b_str = str(new_b)
            #we add leading 0s if the new length of new_b is less than precision
            while len(new_b_str) < precision:
                new_b_str = '0' + new_b_str

            return fixNum(new_a, new_b_str)#result is then returned
