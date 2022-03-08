"""Test Carte Pizzeria Class
"""
from mock import Mock, patch, PropertyMock
from carte_pizzeria import CartePizzeria

# Setup de l'environnement de test en modifiant directement l'attribut
# privé via l'attribut _CartePizzeria__pizzas
# pylint: disable=W0212
def test_carte_pizza_is_empty():
    """Test carte pizza is empty without patch
    """
    carte = CartePizzeria()
    carte._CartePizzeria__pizzas = []
    assert carte.is_empty()

# Setup de lenvironnement de test en utilisant un patch
@patch('carte_pizzeria.CartePizzeria.pizzas', new_callable=PropertyMock)
def test_carte_pizza_is_empty_with_patch(mock_pizzas):
    """Test carte pizza is empty with patch
    """
    carte = CartePizzeria()
    mock_pizzas.return_value = []
    assert carte.is_empty()

# pylint: disable=W0212
def test_carte_pizza_is_not_empty():
    """Test carte pizza is not empty without patch
    """
    carte = CartePizzeria()
    pizza = Mock()
    carte._CartePizzeria__pizzas = [pizza]
    assert not carte.is_empty()

@patch('carte_pizzeria.CartePizzeria.pizzas', new_callable=PropertyMock)
def test_carte_pizza_is_not_empty_with_patch(mock_pizzas):
    """Test carte pizza is not empty with patch
    """
    carte = CartePizzeria()
    pizza = Mock()
    mock_pizzas.return_value = [pizza]
    assert not carte.is_empty()
