class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print('eating...')
    def breathe(self):
        print('breathing...')

class Dog(Animal):
    def sound(self):
        print('Barking...')

class Cat(Animal):
    def sound(self):
        print('Meow...')

dog1 = Dog('Jack')
dog1.eat()
dog1.sound()

cat1 = Cat('Jill')
cat1.eat()
cat1.sound()