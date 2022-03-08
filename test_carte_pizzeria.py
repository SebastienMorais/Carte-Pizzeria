from mock import Mock, patch, PropertyMock
from carte_pizzeria import CartePizzeria, CartePizzeriaException

# Setup de l'environnement de test en modifiant directement l'attribut
# privé via l'attribut _CartePizzeria__pizzas
def test_carte_pizza_is_empty():
    c = CartePizzeria()
    c._CartePizzeria__pizzas = []
    assert c.is_empty()

# Setup de lenvironnement de test en utilisant un patch
@patch('carte_pizzeria.CartePizzeria.pizzas', new_callable=PropertyMock)
def test_carte_pizza_is_empty_with_patch(mock_pizzas):
    c = CartePizzeria()
    mock_pizzas.return_value = []
    assert c.is_empty()

def test_carte_pizza_is_not_empty():
    c = CartePizzeria()
    pizza = Mock()
    c._CartePizzeria__pizzas = [pizza]
    assert not c.is_empty()

@patch('carte_pizzeria.CartePizzeria.pizzas', new_callable=PropertyMock)
def test_carte_pizza_is_not_empty_with_patch(mock_pizzas):
    c = CartePizzeria()
    pizza = Mock()
    mock_pizzas.return_value = [pizza]
    assert not c.is_empty()

