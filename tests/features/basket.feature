Feature: Basket
    We need to Test a Basket
    So that it will not spill out.

    Scenario: Add items to the Basket
        Given The Basket has 2 items

        When 4 items are added in to Basket

        Then The Basket contains in 6 Basket

    Scenario: Remove items from the Basket
        Given The Basket has 4 items

        When 2 items are Removed from the Basket

        Then The Basket contains 2 Basket only

    Scenario: Add items when No items in the Basket
        Given The Basket has 0 items

        When 2 items are added in to Basket

        Then The Basket contains 2 items

    Scenario: Remove Items when No items in the the Basket
        Given The Basket has 0 items

        When Try to remove 2 items from the Basket

        Then Not allowed to Remove


