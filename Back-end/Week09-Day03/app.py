# Task 1 =======================================

from abc import ABC, abstractclassmethod
from typing import AbstractSet

class Device(ABC):

    @abstractclassmethod
    def turn_on(self):
        pass

    @abstractclassmethod
    def turn_off(self):
        pass


class Computer(Device):

    def turn_on(self):
        print('Press the button to start the computer')

    def turn_off(self):
        print('Press the "Shut down" option to shut down the computer')

class Phone(Device):

    def turn_on(self):
        print('Touch the screen to turn on the phone')

    def turn_off(self):
        print('Double-tap the screen to turn off the phone')

#==========

computer = Computer()
phone = Phone()


# TURN ON
computer.turn_on()
phone.turn_on()

# TURN OFF 
computer.turn_off()
phone.turn_off()

# Task 2 =======================================

class Animal(ABC):

    @abstractclassmethod
    def food(self):
        pass



class Lion(Animal):

    def food(self):
        print('I eat meat')

class Sheep(Animal):

    def food(self):
        print('I eat grass')

class Monkey(Animal):
    
    def food(self):
        print('I eat fruits')

lion = Lion()
sheep = Sheep()
monkey = Monkey()

# FOOD

lion.food()
sheep.food()
monkey.food()