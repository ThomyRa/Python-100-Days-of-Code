
def add(*args):
    accumulated = 0
    for n in args:
        accumulated += n
    print(accumulated)


# add(1, 2, 3, 4, 5, 6)
# add(1, 2)
# add()


# def calculate(n, **kwargs):
#     print(kwargs)
    # for key, value in kwargs.items():
    #     print(key, value)
    # print(kwargs["add"])
#     n += kwargs["add"]
#     n *= kwargs["multiply"]
#     print(n)
#
#
# calculate(2, add=3, multiply=5)


class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("color")
        self.seats = kw.get("seats")


my_car = Car(make="Nissan", color="red")
print(my_car.make)
print(my_car.model)
print(my_car.color)
