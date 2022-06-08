#Abstract Factory

#O método Abstract Factory contém um ou mais métodos de fábrica para criar uma família de objetos relacionados.
#Usa composição para delegar a responsabilidade de criar objetos de outra classe.
#O método Abstract Factory diz respeito a criar famílias de produtos relacionados.

#Quando usar?
#Pode ser utilizado quando precisamos criar uma família de objetos relacionados sem especificar a classe concreta.

#Enquanto o Factory Method adia a criação da instância para as subclasses, o objetivo do método Abstract Factory é criar famílias de objetos relacionados.

from abc import ABCMeta, abstractmethod


class PizzaFactory(metaclass=ABCMeta):
    @abstractmethod
    def create_veg_pizza(self):
        pass

    @abstractmethod
    def create_non_veg_pizza(self):
        pass


class IndianPizzaFactory(PizzaFactory):
    def create_veg_pizza(self):
        return DeluxeVeggiePizza()

    def create_non_veg_pizza(self):
        return ChickenPizza()


class USPizzaFactory(PizzaFactory):
    def create_veg_pizza(self):
        return MexicanVegPizza()

    def create_non_veg_pizza(self):
        return HamPizza()


class VegPizza(metaclass=ABCMeta):
    @abstractmethod
    def prepare(self, veg_pizza):
        pass


class NonVegPizza(metaclass=ABCMeta):
    @abstractmethod
    def serve(self, veg_pizza):
        pass


class DeluxeVeggiePizza(VegPizza):
    def prepare(self):
        print('Prepare', type(self).__name__)


class ChickenPizza(NonVegPizza):
    def serve(self, veg_pizza):
        print(
            type(self).__name__,
            'is served with Chicken on',
            type(veg_pizza).__name__,
        )


class MexicanVegPizza(VegPizza):
    def prepare(self):
        print('Prepare', type(self).__name__)


class HamPizza(NonVegPizza):
    def serve(self, veg_pizza):
        print(
            type(self).__name__,
            'is served with Ham on',
            type(veg_pizza).__name__,
        )


class PizzaStore:
    def make_pizzas(self):
        for factory in [IndianPizzaFactory(), USPizzaFactory()]:
            non_veg_pizza = factory.create_non_veg_pizza()
            veg_pizza = factory.create_veg_pizza()
            veg_pizza.prepare()
            non_veg_pizza.serve(veg_pizza)


if __name__ == '__main__':
    pizza = PizzaStore()
    pizza.make_pizzas()