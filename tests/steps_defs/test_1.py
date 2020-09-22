# coding=utf-8
"""Basket feature tests."""

import pytest
from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)

from basket_class import Basket

#Note: Needs to Override the fixture as its mandatory
@pytest.fixture
def basket():
    return Basket(2)

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


#Note: Needs to Override the fixture as its mandatory
@pytest.fixture
def basket2():
    return Basket(4)


@scenario('../features/basket.feature', 'Remove items from the Basket')
def test_remove_items_from_the_basket():
    """Remove items from the Basket."""
    pass


@given('The Basket has 4 items')
def the_basket_has_4_items():
    """The Basket has 4 items."""
    return Basket(4)


@when('2 items are Removed from the Basket')
def items_are_removed_from_the_basket(basket2):
    """2 items are Removed from the Basket."""
    basket2.removeItem(2)


@then('The Basket contains 2 Basket only')
def the_basket_contains_2_basket_only(basket2):
    """The Basket contains 2 Basket only."""
    assert basket2.count==2




@pytest.fixture
def basket3():
    return Basket(0)

@scenario('../features/basket.feature', 'Add items when No items in the Basket')
def test_add_items_when_no_items_in_the_basket():
    """Add items when No items in the Basket."""
    pass


@given('The Basket has 0 items')
def the_basket_has_0_items():
    """The Basket has 0 items."""
    return Basket(0)


@when('2 items are added in to Basket')
def items_are_added_in_to_basket(basket3):
    """2 items are added in to Basket."""
    basket3.addItem(2)

@then('The Basket contains 2 items')
def the_basket_contains_2_items(basket3):
    """The Basket contains 2 items."""
    assert basket3.count == 2


@pytest.fixture
def basket4():
    return Basket(0)


@scenario('../features/basket.feature', 'Remove Items when No items in the the Basket')
def test_remove_items_when_no_items_in_the_the_basket():
    """Remove Items when No items in the the Basket."""
    pass


@given('The Basket has 0 items')
def the_basket_has_0_items():
    """The Basket has 0 items."""
    return Basket(0)


@when('Try to remove 2 items from the Basket')
def try_to_remove_2_items_from_the_basket(basket4):
    """Try to remove 2 items from the Basket."""
    basket4.removeItem(2)


@then('Not allowed to Remove')
def not_allowed_to_remove(basket4):
    """Not allowed to Remove."""
    #Need to understand how to Validate Expetion

    with pytest.raises(ValueError) as e:
        assert "Trying to remove item when Basket is Empty" in e.value





