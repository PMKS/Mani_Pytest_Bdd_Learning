# coding=utf-8
"""Basket feature tests."""


'''
In this Test file below listed improvemnst made
1. dict(Number=int) extratype is called in every parsers.cfparse hence , so defined out side as "EXTRA_TYPE" and
called "EXTRA_TYPE"  every time when required

2. from functools import partial class to elimninate "parsers.cfparse" function call and extra_types

3. @given input is common hence commented the second time

4. Use "scenarios" behalf of scenario function calling and gave teh path of the scenario file
'''

from basket_class import Basket
from pytest_bdd import (
    parsers,
    given,
    scenarios,
    then,
    when,
)
import pytest
from functools import partial
EXTRA_TYPE=dict(Number=int)

parse_data=partial(parsers.cfparse,extra_types=EXTRA_TYPE)
@pytest.fixture()
def basket4():
    return Basket(2)



scenarios('../features/paramater_test.feature')
# @pytest.mark.test_param_add
# @scenario('../features/paramater_test.feature', 'Add items to the Basket')
# def test_add_items_to_the_basket():
#     """Add items to the Basket."""
#     pass

@given(parse_data('The Basket has "{initial:Number}" items'))
#given('The Basket has "2" items')
def the_basket_has_initial_items(initial):
    """The Basket has "2" items."""
    return Basket(initial)


@when(parse_data('"{some:Number}" items are added in to Basket'))
def items_are_added_in_to_basket(basket4,some):
    """"4" items are added in to Basket."""
    basket4.addItem(some)


@then(parse_data('The Basket contains in "{final:Number}" Basket'))
def the_basket_contains_in_6_basket(basket4,final):
    """The Basket contains in "6" Basket."""
    assert basket4.count == final


#Scenario 2

@pytest.fixture()
def basket5():
    return Basket(4)

# @pytest.mark.test_param_remove
# @scenario('../features/paramater_test.feature', 'Remove items from the Basket')
# def test_Remove_items_from_the_Basket():
#     """Add items to the Basket."""
#     pass

# @given(parse_data('The Basket has "{initial:Number}" items'))
# #given('The Basket has "4" items')
# def the_basket_has_4_items(initial):
#     """The Basket has "2" items."""
#     return Basket(initial)


@when(parse_data('"{some:Number}" items are removed from the Basket'))
def items_are_removed_from_the_Basket(basket5,some):
    """"4" items are added in to Basket."""
    basket5.removeItem(some)


@then(parse_data('The Basket contains "{final:Number}" items'))
def the_basket_contains_2_Items(basket5,final):
    """The Basket contains in "6" Basket."""
    assert basket5.count == final