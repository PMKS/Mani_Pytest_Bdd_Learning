Feature: Basket
    We need to Test a Basket
    So that it will not spill out.

    Scenario Outline: Add items to the Basket
        Given The Basket has "<initial>" items

        When "<some>" items are added in to Basket

        Then The Basket contains in "<total>" Basket

    Examples: Values
        | initial | some | total |
        | 2       | 4    | 6     |
        | 2       | 1    | 3     |
        | 2       | 7    | 9     |

    Scenario: Remove items from the Basket
        Given The Basket has "4" items

        When "2" items are removed from the Basket

        Then The Basket contains "2" items
