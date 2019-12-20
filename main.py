from __future__ import annotations
from abc import ABC, abstractmethod, abstractproperty
from typing import Any

class Builder(ABC):
  
    @abstractproperty
    def product(self):
        pass

    @abstractmethod
    def produce_part_a(self):
        pass

    @abstractmethod
    def produce_part_b(self):
        pass

    @abstractmethod
    def produce_part_c(self):
        pass


class Builder1(Builder):

    def __init__(self):
        self.reset()

    def reset(self):
        self._product = Product1()

    @property
    def product(self) -> Product1:
        product = self._product
        self.reset()
        return product

    def produce_part_a(self) -> None:
        self._product.add("PartA1")

    def produce_part_b(self) -> None:
        self._product.add("PartB1")

    def produce_part_c(self) -> None:
        self._product.add("PartC1")

class Product(ABC):
    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
        print(f"Product parts: {', '.join(self.parts)}", end="")
  
    @abstractmethod
    def operation(self) -> str:
        pass


class Product1(Product):
    def operation(self) -> str:
        return "{Product1}"


class Product2(Product):
    def operation(self) -> str:
        return "{Product2}"

class Director:
   
    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> Builder:
        return self._builder

    @builder.setter
    def builder(self, builder: Builder) -> None:
        self._builder = builder

    def build_minimal_product(self) -> None:
        self.builder.produce_part_a()

    def build_full_product(self) -> None:
        self.builder.produce_part_a()
        self.builder.produce_part_b()
        self.builder.produce_part_c()

class Creator(ABC):
 
    @abstractmethod
    def factory_method(self):
        pass

    def some_operation(self) -> str:
        product = self.factory_method()
        result = f"Created: {product.operation()}"
        return result

class Creator1(Creator):

    def factory_method(self) -> Product1:
        return Product1()


class Creator2(Creator):
    def factory_method(self) -> Product2:
        return Product2()

def create_product(creator: Creator) -> None:
    print(creator.some_operation())


if __name__ == "__main__":
    create_product(Creator1())
    print("\n")
    create_product(Creator2())
    print("\n")
    director = Director()
    builder = Builder1()
    director.builder = builder

    print("Standard basic product: ")
    director.build_minimal_product()
    builder.product.list_parts()
    print("\n")
    print("Standard full featured product: ")
    director.build_full_product()
    builder.product.list_parts()

    print("\n")

    print("Custom product: ")
    builder.produce_part_a()
    builder.produce_part_b()
    builder.product.list_parts()