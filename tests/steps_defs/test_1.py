# coding=utf-8
"""Basket feature tests."""


from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)

from basket_class import Basket


@scenario('../features/basket.feature', 'Add items to the Basket')
def test_add_items_to_the_basket():
    """Add items to the Basket."""
    pass



@given('The Basket has 2 items')
def the_basket_has_2_items():
    """The Basket has 2 items."""
    return Basket(2)


@when('4 items are added in to Basket')
def items_are_added_in_to_basket(basket):
    """4 items are added in to Basket."""
    basket.addItem(4)


@then('The Basket contains in 6 Basket')
def the_basket_contains_in_6_basket(basket):
    """The Basket contains in 6 Basket."""
    return basket.count == 6

