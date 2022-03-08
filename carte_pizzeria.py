"""Module Carte Pizzeria
"""

class CartePizzeriaException(Exception):
    """Exception dedicated to CartePizzeria
    """


class CartePizzeria:
    """Carte Pizzeria Class
    """

    def __init__(self):
        self.__pizzas = []

    @property
    def pizzas(self):
        """Returns pizzas.
        """
        return self.__pizzas

    def is_empty(self):
        """Return True if the CartePizzeria is empty, False otherwise.
        """
        return len(self.pizzas) == 0

    def nb_pizzas(self):
        """Return the number of pizzas
        """
        return len(self.pizzas)

    def add_pizza(self, pizza):
        """Add a new pizza
        """
        self.pizzas.append(pizza)

    def remove_pizza(self, name):
        """Remove a pizza
        """
        found = False
        for pos, inner_pizza in enumerate(self.pizzas):
            if inner_pizza.name == name:
                found = True
                break
        if not found:
            raise CartePizzeriaException(f"pizza {name} is not registered")
        del self.pizzas[pos]
