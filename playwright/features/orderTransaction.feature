Feature: Order Transaction
  Tests related to Order Transactions


  Scenario Outline: Verify order success message shown in details page
    Given place the item order with <username> and <password>
    And user is on landing page
    When I login to portal with <username> and <password>
    And navigate to orders page
    And select the orderId
    Then order message is successfully displayed
    Examples:
      | username        | password |
      | asddsa@asd.com  | Pa55word |