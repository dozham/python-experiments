from abc import ABC, abstractmethod
from typing import override


def violating_dip():
    class LightBulb:
        def turn_on(self):
            print("LightBulb: turned on")

        def turn_off(self):
            print("LightBulb: turned off")

    class Switch:
        def __init__(self, bulb: LightBulb):
            self.bulb = bulb

        def operate(self):
            self.bulb.turn_on()
            print("Switch: operating")

    # Usage
    bulb = LightBulb()
    switch = Switch(bulb)
    switch.operate()



# # This is not what I need to achieve to fix Dependency Inversion issue above! Switch is actually relying on LightBulb (and it's methods) still (creation of a light bulb was not even a concern here as it was already passed as a parameter, hence dependency INJECTION is also already applied)
# def version1():
#     class LightBulb:
#         def turn_on(self):
#             print("LightBulb: turned on")
#
#         def turn_off(self):
#             print("LightBulb: turned off")
#
#     class Switch:
#         def __init__(self):
#             pass
#
#         def operate(self, bulb: LightBulb):
#             bulb.turn_on()
#             print("Switch: operating")
#
#     # Usage
#     bulb = LightBulb()
#     switch = Switch()
#     switch.operate(bulb)
#

# Up to now, Switch is dependent on LightBulb and cannot be used for a SmartBulb, or a Heater etc. We want to achieve that flexibility and extensibility
def version2():
    class Switchable(ABC):
        @abstractmethod
        def turn_on(self):
            pass
        @abstractmethod
        def turn_off(self):
            pass

    class LightBulb(Switchable):
        @override
        def turn_on(self):
            print("LightBulb is turned on")

        @override
        def turn_off(self):
            print("LightBulb is turned off")

    class SmartBulb(Switchable):
        @override
        def turn_on(self):
            print("SmartBulb is turned on")

        @override
        def turn_off(self):
            print("SmartBulb is turned off")

    class Switch:
        def __init__(self, device: Switchable) -> None:
            self.device: Switchable = device

        def operate(self):
            self.device.turn_on()

