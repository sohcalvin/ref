from mongoengine import *

connect("abc")

class User(Document):
    email = StringField(required=True)
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)

    def getName(self):
        return self.first_name + self.last_name


# ross = User(email='calvin@example.com', first_name='Ross', last_name='Lawley')
#
# ross.save()

results = User.objects(email="ross@example.com")
for r in results :
    print(r)
    print(r.getName())