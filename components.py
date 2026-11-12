class Resistor:
    def __init__(self, resistance, node1, node2):
        if not isinstance(resistance, (int, float)):
            raise TypeError("Resistance must be a number.")

        if resistance <= 0:
            raise ValueError("Resistance must be positive.")

        if node1 == node2:
            raise ValueError("A resistor cannot connect a node to itself.")

        self.resistance = resistance
        self.node1 = node1
        self.node2 = node2
    
    def describe(self):
        return (
            f"Resistor: {self.resistance} ohms, "
            f"connected between {self.node1} and {self.node2}"
        )

class VoltageSource:
    def __init__(self, voltage, positive_node, negative_node):
        self.voltage = voltage
        self.positive_node = positive_node
        self.negative_node = negative_node

    def describe(self):
        return (
            f"Voltage source: {self.voltage} V, "
            f"positive at {self.positive_node}, "
            f"negative at {self.negative_node}"
        )


