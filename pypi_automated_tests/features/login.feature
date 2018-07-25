Feature: Login

Scenario: Login Success
Given I am on my Assetbank login page
And I enter a valid email for my server
And I enter associated valid password
When I opt to Login
Then I am directed to my Assetbank dashboard