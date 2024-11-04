from numbers import Number # noqa f401


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
            todo = min(len(self.coefficients), len(other.coefficients)) 
            if len(self.coefficients) >= len(other.coefficients): 
                lizst1 = list(self.coefficients) 
                lizst2 = list(other.coefficients) 
            else: 
                lizst1 = list(other.coefficients)
                lizst2 = list(self.coefficients) 
            for i in range(todo): 
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
        return self - other


a = Polynomial((-1, -1, -1))
b = Polynomial((2, 2, 2))
print(b - a)

