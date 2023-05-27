import colorama


def first_function():
    pass
class Human:
    pass
cl=colorama
first_f=first_function
nick=Human
print(colorama.__name__)
print(cl.__name__)
print(first_function.__name__)
print(first_f.__name__)
print(Human.__name__)
print(nick.__name__)


intro_list = []
for method in dir(intro_list):
    print(method)


data = "string"
print(hasattr(data, "reverse"))
print(hasattr(data, "index"))


data = "string"
print(getattr(data, "startswith"))
print(getattr(data, "startswith", None))
print(getattr(data, "reverse", None))


data="string"
def first_function():
    pass
print(callable(data))
print(callable(first_function))


class First_class:
    pass
class Second_class(First_class):
    pass
print(issubclass(First_class, Second_class))
print(issubclass(Second_class, First_class))


class First_class:
    pass
class Second_class(First_class):
    pass
obj_from_class_2=Second_class()
print(isinstance(obj_from_class_2, First_class))
print(isinstance(obj_from_class_2, Second_class))

