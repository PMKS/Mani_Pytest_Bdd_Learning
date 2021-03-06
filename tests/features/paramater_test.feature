Feature: Basket
    We need to Test a Basket
    So that it will not spill out.

    Scenario: Add items to the Basket
        Given The Basket has "2" items

        When "4" items are added in to Basket

        Then The Basket contains in "6" Basket

    Scenario: Remove items from the Basket
        Given The Basket has "4" items

        When "2" items are removed from the Basket

        Then The Basket contains "2" items
