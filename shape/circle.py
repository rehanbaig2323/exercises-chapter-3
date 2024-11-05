class Circle: 

    def __init__(self, centre, radius): 
        self.centre = centre 
        self.radius = radius 

    def __contains__(self, point): 
        return ((self.centre[0] - point[0]) ** 2 + (self.centre[1] - point[1]) ** 2 < self.radius)
    
c = Circle((1., 0.), 2)
print((0.5, 0.5) in c)
