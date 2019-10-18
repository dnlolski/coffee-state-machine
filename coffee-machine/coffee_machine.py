from states.states import SelectionState
from coffee.coffee import Coffee


class CoffeeMachine(object):
    def __init__(self):
        self.state = SelectionState()
        self.resources = {'water': 100,
                          'milk': 100}
        self._coffee_type = ['americana', 'flat white', 'white', 'latte', 'espresso']
        self._coffee_size = ['small', 'medium', 'large']

    def resource_change(self, water=0, milk=0):
        if 0 != water:
            if self.resources['water'] - water < 0:
                print("Not enough water! Refilling...")
                self.resources['water'] = 100
            self.resources['water'] = self.resources['water'] - water

        if 0 != milk:
            if self.resources['milk'] - milk < 0:
                print("Not enough milk! Refilling...")
                self.resources['milk'] = 100
            self.resources['milk'] = self.resources['milk'] - milk
        print(self.resources)

    def picking(self):
        self.state = self.state.picking()
        return self._coffee_type, self._coffee_size

    def brewing(self, coffee_type, coffee_size):
        self.state = self.state.brewing(coffee_type, coffee_size)

        if coffee_type in ['flat white', 'white', 'latte']:
            self.resource_change(milk=10)
        if coffee_size == 'medium':
            self.resource_change(water=20)
        if coffee_size == 'large':
            self.resource_change(water=40)
        if coffee_size == 'small':
            self.resource_change(water=10)

        print(coffee_size, coffee_type)
        return Coffee(coffee_type, coffee_size)

    def serving(self, coffee):
        self.state = self.state.serving(coffee)
        return coffee

    def transition(self, event):
        self.state = self.state.transition(event)
