Feature: Test the search functionality in the homepage of amazon

  Background:
    Given Home page: I am on amazon homepage

  @T1 @regression @BDD
  Scenario Outline: Check that the user can make a simple search in the amazon homepage
    When Home page: I search for "<product_name>" from category "<category_name>"
    Then Home page: I have at least "<nr_of_results>" results returned

    @cell_phones   !!!!!!
    Examples:
      | product_name | category_name | nr_of_results |
      | iphone       | Electronics   | 100           |
      | samsung      | Electronics   | 100           |


  @T2 @functional @BDD
  Scenario:  Check that the user can make an advanced search for a product
    When Home page: When I click on the Today's Deals
    When Today's Deals: I select Computers & Accessories department
    When Today's Deals: I choose the price
    When Today's Deals: I select average customer review rating
    When Today's Deals: I select the Discount that I want
    Then Today's Deals: I should be able to click on the first result of the customized search