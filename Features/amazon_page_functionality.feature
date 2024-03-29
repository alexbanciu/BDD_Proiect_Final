Feature: Test the functionality of Amazon's page

  Background:
    Given Home page: I am on amazon homepage



  @T1
  Scenario Outline: Check that the user can make a simple search in the amazon homepage
    When Home page: I search for "<product_name>" from category "<category_name>"
    Then Home page: I have at least "<nr_of_results>" results returned

    @cell_phones
    Examples:
      | product_name | category_name | nr_of_results |
      | huawei       | Electronics   | 21            |
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

  @T2
  Scenario: Check the functionality of the "Sign In" button
    When Home page: I click on the Sign In button
    When Sign In page: I send email and password
    Then  I should get back to amazon homepage

  @T3
  Scenario: Verify if there is at least one product in the cart
    When Main Page: I type "iphone"
    Then Search results page: I select the any iphone from the search results
    When Cart page: I click on Add to Cart
    Then Cart page: I should see at least one item in the cart

  @T4
  Scenario: Change Currency from Dollar to Euro
    When Home page: I click on the currency dropdown
    When Home page: I select the currency as Euro
    Then Home page: The currency should be changed to EUR

 @T5
 Scenario: Verify Amazon Logo
    Then Home page: The Amazon logo should be displayed

  @T6
  Scenario: Verify Page Title is Displayed
    Then Home page: The page title "Amazon" should be displayed

  @T7
  Scenario:  Check that the user can make an advanced search for a product in Today's Deals topic
    When Home page: When I click on the Today's Deals
    When Today's Deals: I select Computers & Accessories department
    When Today's Deals: I choose the price
    When Today's Deals: I select average customer review rating
    When Today's Deals: I select the Discount that I want
    Then Today's Deals: I should be able to remove or modify any applied search filters easily

  @T8
  Scenario: I check the sign up error message functionality
    When sign_up: I click on sign up button
    When sign_up: I send my full name
    When sign_up: I enter my email
    When sign_up: I send the password
    When sign_up: I re-enter a wrong password
    When sign_up: I submit my personal info by clicking verify email
    Then sing_up: I should receive the message: Passwords must match

  @T9
  Scenario: Filter search results by price range
    When I search for "headphones"
    And I apply a filter for a price range of $50 to $100
    Then If the filter was applied I should be able to see the icon to close that price filter

  @T10
  Scenario: Check that the user can be redirected to Amazon free streaming music
    When Home page: I click on All button from top menu
    When Home page: I click on Amazon Music
    When Home page: I choose Free Streaming Music from the menu
    When Amazon music page: I click on listen now button
    Then Amazon streaming music: I should be redirected to Amazon streaming music page
    Then Home page: I should return to the home page