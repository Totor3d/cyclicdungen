class Vector2:

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, vector):
        return Vector2(vector.x + self.x, vector.y + self.y)
    
    def __sub__(self, vector):
        return Vector2(vector.x - self.x, vector.y - self.y)
    
    def __mul__(self, scalar):
        return Vector2(scalar * self.x, scalar * self.y)

    def distance(self, vector):
        return ((self.x - vector.x)**2+(self.y - vector.y)**2)**0.5

class Body:

    def __init__(self, x, y, id, powerInfluence = 1):
        self.id = id
        self.position = Vector2(x, y)
        self.speed = Vector2(0, 0)
        self.force = Vector2(0, 0)
        self.powerInfluence = powerInfluence

    def update(self, delta):
        self.position = self.position + (self.speed * delta)
        self.speed = self.speed + (self.force * delta)

    def addImpulses(self, impulse):
        self.speed = self.speed + impulse * self.powerInfluence

    def distance(self, body):
        return self.position.distance(body.position)

class Rectangle:
    
    def __init__(self, position, size):
        self.position = position
        self.size = size
    
    def isItColliding(self, rectangle):

        if abs(rectangle.position.x - self.position.x) < rectangle.size.x/2 + self.size.x/2 and abs(rectangle.position.y - self.position.y) < rectangle.size.y/2 + self.size.y/2:
            return True
        
        return False

def addGravityForces(bodies, power = 1):
    for b in bodies:
        for b1 in bodies:
            if b != b1:
                b.addImpulses((b.position - b1.position)*(power/b.distance(b1)))