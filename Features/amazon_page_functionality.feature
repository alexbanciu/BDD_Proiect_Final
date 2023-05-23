Feature: Test the functionality of Amazon's page

  Background:
    Given Home page: I am on amazon homepage

  @T1 @regression @BDD
  Scenario Outline: Check that the user can make a simple search in the amazon homepage
    When Home page: I search for "<product_name>" from category "<category_name>"
    Then Home page: I have at least "<nr_of_results>" results returned

    @cell_phones
    Examples:
      | product_name | category_name | nr_of_results |
      | iphone       | Electronics   | 21            |
      | samsung      | Electronics   | 33            |

    @computers
    Examples:
      | product_name | category_name | nr_of_results |
      | mouse        | Computers     | 10            |
      | keyboards    | Computers     | 11            |

    @software
    Examples:
      | product_name | category_name | nr_of_results |
      | antivirus    | Software      | 2             |
      | windows      | Software      | 3             |

    @automotive
    Examples:
      | product_name | category_name | nr_of_results |
      | car holder   | Automotive    | 12            |
      | car charger  | Automotive    | 7             |


  @T2 @functional @BDD
  Scenario:  Check that the user can make an advanced search for a product
    When Home page: When I click on the Today's Deals
    When Today's Deals: I select Computers & Accessories department
    When Today's Deals: I choose the price
    When Today's Deals: I select average customer review rating
    When Today's Deals: I select the Discount that I want
    Then Today's Deals: I should be able to remove or modify any applied search filters easily


    @T3 @functional @BDD
  Scenario: I check the sign up error message functionality
    When sign_up: I click on sign up button
    When sign_up: I send my full name
    When sign_up: I enter my email
    When sign_up: I send the password
    When sign_up: I re-enter a wrong password
    When sign_up: I submit my personal info by clicking verify email
    Then sing_up: I should receive the message: Passwords must match