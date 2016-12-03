class MySingleton() :

    name = "123"

    def __init__(self, name):
       self.name = name

    def __str__(self):
        return self.name

s1 = MySingleton("xyz")
print(s1)
print(s1.name)
print(MySingleton.name)