class fixNum:

    """
    The core idea is to represent the number as a fixed-point number with a certain number of fractional digits.
    In function,
    a will be the integer part,
    and b will be the fractional part.
    b_len stores how many digits b has (for aligning decimals when adding later).
    """
    
    def __init__(self, a, b):
        # force a and b to be integers
        self.a = int(a)
        self.b = str(b) #stored as a string to handle leading 0s later

        # length of b as a digit string (for decimal alignment)
        self.b_len = len(str(abs(self.b)))

        # In the assignment: if a is non-zero, b must be positive.
        if self.a != 0:
            self.b = abs(self.b)

    def __str__(self):
        # format will be "a.b"
        a_part = str(self.a)
        b_part = str(abs(self.b))

        # catch the special negative zero case (e.g., -0.48)
        if self.a == 0 and self.b < 0:
            return "-" + a_part + "." + b_part
        else:
            return a_part + "." + b_part