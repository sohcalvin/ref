class Car :
    def __init__(self,color=None, capacity=4): # Constructor
        self.color=color
        self.capacity= capacity

    def __repr__(self): # This is the toString() method
         return "Car: color=" + str(self.color) + ", capacity=" +  str(self.capacity)

aCar1 = Car(capacity=5, color="red")
aCar2 = Car("blue", 7)
print(aCar1)
print(aCar2)

print(Car.__name__)
print(Car.__module__)
print(Car.__dict__)