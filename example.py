#approaching the same problem using 
#1. funcational programming
#2. object oriented programming
def translate(point , translation):
    '''
    a function which takes a point and translates by the given translation
    input:
    point-[x,y]
    translation-[transx,transy]
    output:
    new point-[x,y]
    '''
    return [point[0]+translation[0] , point[1]+ translation[1]]

def show(point):
    print(point)    

#OOPS approach

class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def show(self):
        print(self.x,self.y)    



    def translate(self,translation):
        '''
        translation is also a list
        '''
        self.x=self.x + translation[0]
        self.y=self.y + translation[1]

            

class Line:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def show(self):
        print(self.point1, self.point2)

    def translate(self,translation):
        self.point1[0] = self.point1[0]+ translation[0]
        self.point1[1] = self.point1[1] + translation[1]
        self.point2[0] = self.point2[0] + translation[0]
        self.point2[1] = self.point2[1] + translation[1]        
    


class Rectangle:
    def __init__(self, point1, point3):
        '''
        point1 and point3 is an instance of class Point
        '''
        self.point1 = point1
        
        self.point3 = point3
        


    def show(self):
        self.point1.show()
        self.point3.show()
         

    def translate(self, translation):
        self.point1.translate(translation)
        self.point3.translate(translation)

        '''
        self.point1[0] = self.point1[0] + translation[0]
        self.point1[1] = self.point1[1] + translation[1]
        self.point3[0] = self.point3[0] + translation[0]
        self.point3[1] = self.point3[1] + translation[1]
        '''

    #def area(self, )    


class Circle:
    def __init__(self, point, radius):
        '''
       input:
        point: Point
        radius: int
        output: none
        '''
        self.radius = radius
        self.point = point


    def show(self):
        self.point.show()
        print(self.radius)   

    def translate(self, translation):
        self.point.translate(translation)
        '''
        self.point[0]=self.point[0]+translation[0]
        self.point[1]=self.point[1]+translation[1]    
        ''' 
  
    
    def area(self):
       area_of_circle =3.14*self.radius**2
       return area_of_circle
        




if __name__== "__main__":
    #result=  translate([2,3],[0,9])  
    
    #print(result)
    chd = Point(3,4)
    chd.show()
    chd.translate([10,10])
    chd.show()
    
    pointa=Point(2,2)
    pointb=Point(1,1)

    manali=Rectangle(pointa, pointb)
    manali.show()
    manali.translate([20000,20000])
    manali.show()

    circle_point=Point(3,4)
    kasoli=Circle(circle_point, 5)
    kasoli.show()
    kasoli.translate([20000,20000])
    kasoli.show()
    

