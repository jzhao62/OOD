import abc

from abc import ABC, abstractmethod


# 主要是decorator design pattern
class CoffeeMaker(object):
    def __init__(self, coffeePack, kindOfCoffee):
        self.coffee = None
        if kindOfCoffee == "DarkRoast":
            self.coffee = DarkRoast()
        elif kindOfCoffee == "Expresso":
            self.coffee = Expresso()
        for _ in range(coffeePack.needMilk):
            self.coffee = WithMilk(self.coffee)
        for _ in range(coffeePack.needSugar):
            self.coffee = WithSugar(self.coffee)
        print(self.coffee)


class CoffeePack(object):
    def __init__(self, needMilk, needSugar):
        self.needMilk = needMilk
        self.needSugar = needSugar


class Coffee(ABC):
    def __init__(self, cost=1.99):
        self.cost = cost

    @abstractmethod
    def get_cost(self):
        pass

    @abstractmethod
    def getIngredients(self):
        pass


class DarkRoast(Coffee):
    def __init__(self):
        self.cost = 1.99

    def get_cost(self):
        return self.cost

    def getIngredients(self):
        return "DarkRoast"


class Expresso(Coffee):
    def __init__(self):
        self.cost = 2.99

    def get_cost(self):
        return self.cost

    def getIngredients(self):
        return "Expresso"


class CoffeeDecorator(Coffee):
    def __init__(self, coffee):
        self.coffee = coffee

    @abstractmethod
    def get_cost(self):
        return self.cost


class WithMilk(CoffeeDecorator):
    def get_cost(self):
        return self.coffee.get_cost() + 0.2

    def getIngredients(self):
        return self.coffee.getIngredients() + ", Milk"


class WithSugar(CoffeeDecorator):
    def get_cost(self):
        return self.coffee.get_cost() + 0.5

    def getIngredients(self):
        return self.coffee.getIngredients() + ", Sugar"





p1 = CoffeePack(2, 2)
d1 = CoffeeMaker(p1, "Expresso")
print(d1.coffee.getIngredients())
print(d1.coffee.get_cost())
