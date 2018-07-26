from abc import ABC, abstractmethod


class AbstractClass(ABC):

    def __init__(self):
        print("This is abstract class")

    @abstractmethod
    def do_something(self):
        pass


class ImplClass(AbstractClass):

    def do_something(self):
        print("Method overridden")


obj = ImplClass()
obj.do_something()
