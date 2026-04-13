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
        
        if self.b_len_start[0] == "-":
            self.b_original_len = len(b_len_start) - 1
        else:
            self.b_original_len = len(b_len_start)
            
        # force a and b to be integers
        self.a = int(a)
        self.b = int(b)

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
