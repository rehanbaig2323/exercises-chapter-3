class Circle: 

    def __init__(self, centre, radius): 
        self.centre = centre 
        self.radius = radius 

    def __contains__(self, point): 
        print 
        return ((self.centre[0] - point[0]) ** 2 + (self.centre[1] - point[1]) ** 2 < (self.radius) ** 2)
    
c = Circle((11.2, -5.1), 2.8)
print((10.2, -3.11) in c)
