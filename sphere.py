#Amanda Maglaras
#amanda.maglaras1@marist.edu
#Sphere surface area and radius 



import math

class Sphere:
    
    def __init__(self , radius):
        self.radius = radius
        self.surfaceArea = 4 * math.pi * self.radius ** 2
        self.volume = (4/3) * math.pi * self.radius ** 3
        
    def getRadius(self):
        return self.radius
        
    def getsurfaceArea(self):
        return self.surfaceArea
        
    def getvolume(self):
        return self.volume
        
def main():
    
    radius = float(input("Enter radius of the sphere: "))
    theSphere = Sphere(radius)
    print("Surface area of the sphere: " , theSphere.getsurfaceArea())
    print("Volume of the sphere: " , theSphere.getvolume())
    
if __name__ == '__main__':
    main()
