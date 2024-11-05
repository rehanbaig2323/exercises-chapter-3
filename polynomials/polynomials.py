from numbers import Number # noqa f401
from numbers import Integral # noqa f401


class Polynomial:
    """Using polynomials."""

    def __init__(self, coefs):
        """Initialise method."""
        self.coefficients = coefs

    def degree(self):
        """Determine the degree of polynomial."""
        return (len(self.coefficients) - 1)

    def __str__(self): 
        """Allow polynomial to be represented normally."""
        lizst = list(self.coefficients) 
        lizst.reverse() 
        tring = ""
        for i in range(len(lizst)):
            coef = str(lizst[i])
            if lizst[i] != 0:
                if lizst[i] == 1: 
                    if i == len(lizst) - 1:
                        tring = tring + " + " + coef
                    elif i == len(lizst) - 2:
                        tring = tring + " + " + "x"
                    elif i == 0: 
                        tring = tring + "x^" + str(len(lizst) - i - 1)
                    else:
                        tring = tring + " + " + "x^" + str(len(lizst) - i - 1)
                    continue
                elif i == len(lizst) - 1:
                    tring = tring + " + " + coef
                elif i == len(lizst) - 2:
                    tring = tring + " + " + coef + "x"
                elif i == 0: 
                    tring = tring + coef + "x^" + str(len(lizst) - i - 1)
                else:
                    tring = tring + " + " + coef + "x^" + \
                        str(len(lizst) - i - 1)
        return tring

    def __repr__(self):
        """Allow for polynomial production."""
        return type(self).__name__ + "(" + repr(self.coefficients) + ")"

    def __eq__(self, other):
        """Ensure polynomials are found equal."""
        return isinstance(other, Polynomial) and \
            self.coefficients == other.coefficients

    def __add__(self, other):
        """Add polynomials together."""
        if isinstance(other, Number):
            lizst = list(self.coefficients)
            lizst[0] = lizst[0] + other
            return Polynomial(tuple(lizst))

        elif isinstance(other, Polynomial):
            todo = min(self.degree(), other.degree()) 
            if len(self.coefficients) >= len(other.coefficients): 
                lizst1 = list(self.coefficients) 
                lizst2 = list(other.coefficients) 
            else: 
                lizst1 = list(other.coefficients)
                lizst2 = list(self.coefficients) 
            for i in range(todo + 1): 
                lizst1[i] = lizst1[i] + lizst2[i] 
            return Polynomial(tuple(lizst1))

        else:
            return NotImplemented

    def __radd__(self, other):
        """Allow for reverse addition."""
        return self + other

    def negafy(self): 
        """Multiply a polynomial by -1."""
        lizst = self.coefficients 
        lizst1 = []
        for coef in lizst: 
            lizst1.append(-1 * coef)
        return Polynomial(tuple(lizst1))

    def __sub__(self, other): 
        """Subtract polynomials from each other."""
        if isinstance(other, Number):
            lizst = list(self.coefficients)
            lizst[0] = lizst[0] - other
            return Polynomial(tuple(lizst))

        elif isinstance(other, Polynomial):
            return (self + other.negafy())

        else:
            return NotImplemented

    def __rsub__(self, other):
        """Allow for reverse subtraction."""
        p = self - other 
        return p.negafy()
    
    def __mul__(self, other): 
        """Multiply polynomials together."""
        if isinstance(other, Number):
            lizst = list(self.coefficients)
            lizst1 = [other * coef for coef in lizst]
            return Polynomial(tuple(lizst1))
        elif isinstance(other, Polynomial):
            masterlist = []
            for i in range(len(self.coefficients)):
                prelist1 = self.coefficients[i] * other
                prelist2 = list(prelist1.coefficients)
                for k in range(i):
                    prelist2.reverse()
                    prelist2.append(0) 
                    prelist2.reverse()
                masterlist.append(Polynomial(tuple(prelist2)))
            firstpoly = masterlist[0]
            for i in range(1, len(masterlist)): 
                firstpoly = firstpoly + masterlist[i]
            return firstpoly
        else:
            return NotImplemented

    def __rmul__(self, other):
        """Allow for reverse multiplication."""
        return self * other

    def __pow__(self, other): 
        """Allow for polyomial exponentiation."""
        if isinstance(other, Integral):
            copy = self
            for i in range(other - 1): 
                copy *= self
            return copy
        else:
            return NotImplemented

    def __call__(self, other):
        """Allow for substitution into the polynomial."""
        constant = self.coefficients[0]
        output = constant
        for i in range(1, len(self.coefficients)):
            output += self.coefficients[i] * (other**i)
        return output
    
    def dx(self): 
        """Differentiate a polynomial."""
        lizst = []
        for i in range(1, len(self.coefficients)): 
            lizst.append(i * self.coefficients[i]) 
        return Polynomial(tuple(lizst)) 

def derivative(poly): 
    return poly.dx()

