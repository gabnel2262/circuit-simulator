class Circuit:
    def __init__(self):
        self.components = []

    def add_component(self, component):
        self.components.append(component)

    def describe(self):
        for component in self.components:
            print(component.describe())
