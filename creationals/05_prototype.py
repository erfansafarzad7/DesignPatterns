"""
    Prototype
    - Allows creating copies of existing objects without making the code dependent on their classes.
    This approach is useful when object creation is expensive or complex.
"""
import copy


class Prototype:
    def __init__(self):
        self._objects = {}

    def register(self, name, obj):
        self._objects[name] = obj

    def unregister(self, name):
        del self._objects[name]

    def clone(self, name, **kwargs):
        """
            Clones a registered object and updates its attributes.
        """
        cloned_obj = copy.deepcopy(self._objects.get(name))
        cloned_obj.__dict__.update(kwargs)
        return cloned_obj


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# ==============================================


def client_prototype(name, obj, **kwargs):
    prototype = Prototype()
    prototype.register(name, obj)
    return prototype.clone(name, **kwargs)


if __name__ == "__main__":
    p = Person('erfan', 30)

    # Clone the original object with modifications
    p_clone = client_prototype(name='p1', obj=p, age=23)
    print(p.__dict__)
    print(p_clone.__dict__)
