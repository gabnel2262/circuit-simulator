from components import Resistor, VoltageSource
from circuit import Circuit

circuit = Circuit()

battery = VoltageSource(9, "A", "C")
r1 = Resistor(220, "A", "B")
r2 = Resistor(330, "B", "C")

circuit.add_component(battery)
circuit.add_component(r1)
circuit.add_component(r2)

for component in circuit.components:
    print(type(component).__name__)

circuit.describe()
