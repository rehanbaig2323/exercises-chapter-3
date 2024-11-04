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
