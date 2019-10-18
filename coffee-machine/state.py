
class State(object):

    def __init__(self):
        print(str(self))

    def picking(self):
        raise NotImplementedError

    def brewing(self, coffee_type, coffee_size):
        raise NotImplementedError

    def serving(self, coffee):
        raise NotImplementedError

    def transition(self, event):
        raise NotImplementedError

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return self.__class__.__name__
