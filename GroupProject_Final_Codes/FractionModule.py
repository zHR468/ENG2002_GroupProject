"""

prepared by :
MARY GORETTI ABWOOLI BIRUNGI (25100607D)
ELIF IREM TANIR(25088642d)
LI YUEN KIK (25087058D) - LAVISSE
HE YOUBIN(25091865D)  
"""
import math

class Fraction: 
    def __init__(self, num, den=1):    # Numerator and Denominator(can't be 0)
        if den == 0:
            raise ZeroDivisionError("Denominator cannot be zero")

        
        # Auto-Simplification for root definition
        # Utilizes math.gcd to help maintain accuracy without forced truncation.
        # This defines the exact intended root (e.g., 6th power, 5th root).
    
        g = math.gcd(num, den)  # Simplification
        self.num = num // g
        self.den = den // g   

        if self.den < 0:  # Keep denominator positive
            self.num = -self.num
            self.den = -self.den

    def __str__(self):
        if self.den != 1:
            return f"{self.num}/{self.den}"
        else:
            return str(self.num)

    def __repr__(self):  # Makes print() work properly
        return self.__str__()

    def __mul__(self, other):   # Multiply with another fraction
        return Fraction(self.num * other.num, self.den * other.den)

    def __pow__(self, exp):
        '''
        Calculates fraction to the power of another fraction
        Outputs tuple
        '''
        if exp.den == 1:  # Integer exponent
            n = exp.num
            if n >= 0:
                return Fraction(self.num**n, self.den**n)
            else:
                # negative integer exponent: reciprocal
                return Fraction(self.den**(-n), self.num**(-n))
        else:
            #  Root Management & Symbolic Output
            # Isolates the root and outputs it as a clean, symbolic string.
            # This helps mitigate non-terminating decimals and avoids floating-point estimation.
            n = exp.num
            d = exp.den
            if n >= 0:
                return (Fraction(self.num**n, self.den**n),"to the power of 1/{}".format(d))
            else:
                # negative fractional exponent: reciprocal root
                return (Fraction(self.den**(-n), self.num**(-n)),"to the power of 1/{}".format(d))


def fraconvert(int_part, frac_str):
    '''
    Converts a fixed-point number into fractions

    Parameters:
    int_part (int): integer part of number
    frac_str (str): fractional part of number

    Returns:
    Fraction(num, scale): Fraction object representing a rational number
    '''
    # Pure Algebraic Conversion
    # Scales the decimal to create an exact, error-free initial fraction.
    # Aims to preserve the original structural precision of the complex decimal before operations.
    scale = 10**len(frac_str)
    if int_part >= 0:
        num = int(int_part) * scale + int(frac_str)
    else: 
        num = int(int_part) * scale - int(frac_str)
    return Fraction(num, scale)
    
def fixed_pow(base_int, base_frac, exp_int, exp_frac):
    
    # Safely trap the complex decimals inside pure fractions first
    base = fraconvert(base_int, base_frac)
    exponent = fraconvert(exp_int, exp_frac)
    
    # Execute the power logic with stable symbolic root management
    return base.__pow__(exponent)