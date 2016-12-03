class AClass() :

    svar = 1;

    def __init__(self):
        self.svar=2
        pass

    def __str__(self):
        return str(AClass.svar)


c = AClass()
# c.svar =3

print(c.svar)

