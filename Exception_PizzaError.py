# Example of classes as Exceptions at work, PizzaError

class PizzaError(Exception):

    def __init__(self, pizza = 'unkown', msj = 'There is no such pizza here'):
        Exception.__init__(self, msj)
        self.pizza = pizza


class TooMuchCheese(PizzaError):

    def __init__(self, pizza = 'desconocido', cheese = '>100', msj = 'That\'s just too much cheese'):
        PizzaError.__init__(self, pizza, msj)
        self.cheese = cheese


def makePizza(pizza, cheese):

    if pizza not in ['margherita', 'capricciosa', 'calzone']:
        raise PizzaError(pizza)
    
    if cheese > 100:
        raise TooMuchCheese (pizza, cheese)
    
    print('The pizza is ready!')


for pz,ch in [('calzone', 0), ('margherita', 110), ('mafia', 20)]:

    try:
        makePizza(pz, ch)

    except TooMuchCheese as TMC:
        print(TMC, ':', TMC.cheese)

    except PizzaError as PE:
        print(PE, ':', PE.pizza)
    
