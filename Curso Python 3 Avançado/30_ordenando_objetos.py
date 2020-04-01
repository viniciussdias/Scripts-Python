# Ordenando objetos

class Objeto:
    def __init__(self, obj_id):
        self.obj_id = obj_id
    
    def __repr__(self):
        return str(self.obj_id)

objetos = [Objeto(12), Objeto(48), Objeto(8)]
obj_sorted = sorted(objetos, key=lambda obj: obj.obj_id) # ordenando com lambda
print(obj_sorted)

from operator import attrgetter

obj_sorted = sorted(objetos, key=attrgetter('obj_id')) # ordenando com attrgetter
print(obj_sorted)
