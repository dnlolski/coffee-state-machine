from state import State


class SelectionState(State):
    def picking(self):
        return self

    def brewing(self, coffee_type, coffee_size):
        raise RuntimeError("Cant brew yet, pick coffee")

    def serving(self, coffee):
        raise RuntimeError("Cant serve yet, pick coffee")

    def transition(self, event):

        if event == 'coffee_picked':
            return PreparingState()

        return self


class PreparingState(State):

    def picking(self):
        raise RuntimeError("Already picked")

    def brewing(self, coffee_type, coffee_size):
        return self

    def serving(self, coffee):
        raise RuntimeError("Cant serve yet, brew coffee")

    def transition(self, event):
        if event == 'serve':
            return CoffeeIsReadyState()
        if event == 'back':
            return SelectionState()

        return self


class CoffeeIsReadyState(State):

    def picking(self):
        raise RuntimeError("Already picked")

    def brewing(self, coffee_type, coffee_size):
        raise RuntimeError("Already brewed")

    def serving(self, coffee):
        return self

    def transition(self, event):
        if event == 'back':
            return SelectionState()

        return self

