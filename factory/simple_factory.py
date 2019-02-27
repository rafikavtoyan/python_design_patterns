from abc import ABCMeta, abstractmethod


class Animal(metaclass=ABCMeta):
    @abstractmethod
    def do_say(self):
        pass


class Dog(Animal):
    def do_say(self):
        print("Bhow Bhow!!")


class Cat(Animal):
    def do_say(self):
        print("Meow Meow!!")


# forest factory defined
class ForestFactory(object):
    def make_sound(self, cls):
        return cls().do_say()

# client code
if __name__ == '__main__':
    ff = ForestFactory()
    ff.make_sound(Dog)
    ff.make_sound(Cat)