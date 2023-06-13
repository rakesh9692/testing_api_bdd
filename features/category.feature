Feature: Category

  Scenario: Verify Category details
    Given I have category 6327
    When I request the category details with "category=false"
    Then It should return json with the following details
      | Field     | Value          |
      | Name      | Carbon credits |
      | CanRelist | True           |
    Then It should return json with the following category promotions
      | Name    | Description               |
      | Gallery | Good position in category |
