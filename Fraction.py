import math

class Fraction: 
    def __init__(self, num, den=1):     # Numerator and Denominator(can't be 0)
        if den == 0:
            raise ZeroDivisionError("Denominator cannot be zero")
           
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
            # Fractional exponent: symbolic root
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

    '''
    scale = 10**len(frac_str)
    if int_part >= 0:
        num = int(int_part) * scale + int(frac_str)
    else: 
        num = int(int_part) * scale - int(frac_str)
    return Fraction(num, scale)
    
def fixed_pow(base_int, base_frac, exp_int, exp_frac):
    base = fraconvert(base_int, base_frac)
    exponent = fraconvert(exp_int, exp_frac)
    
    return base.__pow__(exponent)