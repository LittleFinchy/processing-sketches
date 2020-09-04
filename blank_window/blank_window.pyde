import random

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def is_in_circle(self):
        if sqrt(self.x - width//2 ** 2 + self.y - height//2 ** 2) < width//2:
            return True
        return False

total, inside = 0, 0

def setup():
    size(600,600)
    circle(width//2, height//2, width)

    
def draw():
    #background(0)
    temp_point = Point(random.randint(0, width), random.randint(0, height))
    stroke(0)
    strokeWeight(2)
    point(temp_point.x, temp_point.y)
    if temp_point.is_in_circle():
        inside += 1
    total += 1
    print(total/inside)
    
    
    
    
    
