import copy

class Prototype:
    def __init__(self) -> None:
        self._objects = {}

    def register_object(self, name, obj):
        self._objects[name] = obj

    def unregister_object(self, name):
        del self._objects[name]

    def clone(self, name, **kwargs):
        new_obj = copy.deepcopy(self._objects.get(name))
        new_obj.__dict__.update(kwargs)
        return new_obj


class Car:
    def __init__(self) -> None:
        self.model = 'Tesla S'
        self.color = 'Black'
        self.options = 'I001'

    def __str__(self) -> str:
        return '{} | {} | {}'.format(self.model, self.color, self.options)


# Construct car and prototype
c = Car()
p = Prototype()
p.register_object('Tesla', c)

# Clone tesla into new variable
c1 = p.clone('Tesla')
print(c1)
