# coding=utf-8
"""Basket feature tests."""
from basket_class import Basket
from pytest_bdd import (
    parsers,
    given,
    scenario,
    then,
    when,
)
import pytest


@pytest.fixture()
def basket4():
    return Basket(2)


@pytest.mark.test_param_add
@scenario('../features/paramater_test.feature', 'Add items to the Basket')
def test_add_items_to_the_basket():
    """Add items to the Basket."""
    pass

@given(parsers.cfparse('The Basket has "{initial:Number}" items',extra_types=dict(Number=int)))
#given('The Basket has "2" items')
def the_basket_has_2_items(initial):
    """The Basket has "2" items."""
    return Basket(initial)


@when(parsers.cfparse('"{some:Number}" items are added in to Basket',extra_types=dict(Number=int)))
def items_are_added_in_to_basket(basket4,some):
    """"4" items are added in to Basket."""
    basket4.addItem(some)


@then(parsers.cfparse('The Basket contains in "{final:Number}" Basket',extra_types=dict(Number=int)))
def the_basket_contains_in_6_basket(basket4,final):
    """The Basket contains in "6" Basket."""
    assert basket4.count == final


#Scenario 2

@pytest.fixture()
def basket5():
    return Basket(4)

@pytest.mark.test_param_remove
@scenario('../features/paramater_test.feature', 'Remove items from the Basket')
def test_Remove_items_from_the_Basket():
    """Add items to the Basket."""
    pass

@given(parsers.cfparse('The Basket has "{initial:Number}" items',extra_types=dict(Number=int)))
#given('The Basket has "4" items')
def the_basket_has_4_items(initial):
    """The Basket has "2" items."""
    return Basket(initial)


@when(parsers.cfparse('"{some:Number}" items are removed from the Basket',extra_types=dict(Number=int)))
def items_are_removed_from_the_Basket(basket5,some):
    """"4" items are added in to Basket."""
    basket5.removeItem(some)


@then(parsers.cfparse('The Basket contains "{final:Number}" items',extra_types=dict(Number=int)))
def the_basket_contains_2_Items(basket5,final):
    """The Basket contains in "6" Basket."""
    assert basket5.count == final