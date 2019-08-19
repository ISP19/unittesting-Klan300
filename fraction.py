import math

class Fraction:
    """A fraction with a numerator and denominator and arithmetic operations.

    Fractions are always stored in proper form, without common factors in 
    numerator and denominator, and denominator >= 0.
    Since Fractions are stored in proper form, each value has a
    unique representation, e.g. 4/5, 24/30, and -20/-25 have the same
    internal representation.
    """
    
    def __init__(self, numerator, denominator=1):
        """Initialize a new fraction with the given numerator
           and denominator (default 1).
        """
        #TODO write this (and remove this TODO comment)
        self.numerator = numerator
        self.denominator = denominator
        

    #TODO Write the __add__ method, and remove this TODO comment.
    def __add__(self, frac):
        """Return the sum of two fractions as a new fraction.
           Use the standard formula  a/b + c/d = (ad+bc)/(b*d)
        """
        numerator = ((self.numerator * frac.denominator) + (frac.numerator * self.denominator))
        denominator = self.denominator * frac.denominator
        
        return Fraction(numerator, denominator)

    #TODO write __mul__ and __str__.  Verify __eq__ works with your code.
    #Optional have fun and overload other operators such as 
    # __sub__ for f-g
    # __gt__  for f > g
    # __neg__ for -f (negation)

    def __mul__(self,frac):
        """Multiply 2 fraction 
        """
        numerator = self.numerator * frac.numerator
        denominator = self.denominator * frac.denominator

        return Fraction(numerator,denominator)

    def __str__(self):
        gcd = math.gcd(self.numerator,self.denominator)
        self.numerator = int(self.numerator/gcd)
        self.denominator = int(self.denominator/gcd)
        frac = self.numerator/self.denominator
        
        if abs(self.denominator) == 1:
            result = f"{int(self.numerator/self.denominator)}"
        else:
            if frac == 0:
                result = "0"
            elif frac < 0 and self.denominator < 0:
                result = f"{int(-self.numerator)}/{int(-self.denominator)}"
            else:
                if self.denominator < 0:
                    result = f"{int(-self.numerator)}/{int(-self.denominator)}"
                else:
                    result = f"{int(self.numerator)}/{int(self.denominator)}"
        return result



    def __eq__(self, frac):
        """Two fractions are equal if they have the same value.
           Fractions are stored in proper form so the internal representation
           is unique (3/6 is same as 1/2).
        """
        return self.__str__() == frac.__str__()

