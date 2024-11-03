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
        lizst = list(self.coefficients) 
        tring = ""
        for i in range(len(lizst)):
            coef = str(lizst[i])
            if lizst[i] != 0:
                if i == 0:
                    tring = tring + coef
                elif i == 1:
                    tring = tring + " + " + coef + "x"
                else:
                    tring = tring + " + " + coef + "x^" + str(i)
        return tring
            
