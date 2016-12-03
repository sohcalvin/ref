array_of_objects = [
     { 'name' : "aaa" , 'age' : 10},
     { 'name' : "bbb" , 'age' : 9},
     { 'name' : "ccc" , 'age' : 8}
]

print("Before\n", array_of_objects)

sorted_cv_list = sorted(array_of_objects, key=lambda x: x['name'], reverse=True)

print("After\n", sorted_cv_list)