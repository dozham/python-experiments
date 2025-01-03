from abc import ABC, abstractmethod
from typing import override


def version_violating_lsp():
    class Bird:
        def fly(self):
            print("Flying...")

    class Sparrow(Bird):
        def fly(self):
            print("Sparrow flying...")

    class Penguin(Bird):
        def fly(self):
            raise NotImplementedError("Penguins can't fly!")

# Problem with previous version is that penguins cannot be substituted in place of Birds because they raise exceptions if fly is called
# Let's fix that
def version1():
    class Bird(ABC):
        @abstractmethod
        def move(self):
            pass

    class FlyingBird(Bird):
        @override
        def move(self):
            print("Flying...")

    class Sparrow(FlyingBird):
        @override
        def move(self):
            print("Sparrow flying...")

    class Penguin(Bird):
        def move(self):
            print("The penguin is waddling even if it cannot fly ...")

