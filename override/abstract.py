from abc import ABCMeta, abstractmethod

#抽象类
class Animal(object, metaclass=ABCMeta):

    def __init__(self, nickname):
        self._nickname = nickname
    #抽象方法
    @abstractmethod
    def move(self):
 
        pass


class Dog(Animal):

    def move(self):
        print('%s is running' % self._nickname)


class Fish(Animal):

    def move(self):
        print('%s is swimming' % self._nickname)


def main():
    pets = [Dog('little dog'), Fish('big fish')]
    for pet in pets:
        pet.move()


if __name__ == '__main__':
    main()