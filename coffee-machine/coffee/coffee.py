
class Coffee:

    def __init__(self, coffee_type, size):
        self.coffee_type = str(coffee_type)
        self.size = str(size)

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "{coffee_type} {size}".format(coffee_type=self.coffee_type, size=self.size)
