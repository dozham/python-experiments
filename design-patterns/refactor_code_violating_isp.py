from abc import ABC, abstractmethod


def version_violating_isp():
    class Worker:
        def work(self):
            print("Working...")

        def eat(self):
            print("Eating...")

    class RobotWorker(Worker):
        def work(self):
            print("Working robotically...")

        def eat(self):
            raise NotImplementedError("Robots do not eat!")


# This example above violates the interface segregation principle as a child/client (Robot) that does not use a method is forced to implement it (eat())
def version1():
    class Worker(ABC):
        @abstractmethod
        def work(self):
            pass

    class HumanWorker(Worker):
        def work(self):
            print("Working humanly...")

        def eat(self):  # Potential for improvement if there are more types of workers that also eat; we could introduce an interface like Eater!
            print("Eating... A person needs food")

    class RobotWorker(Worker):
        def work(self):
            print("Working robatically...")


