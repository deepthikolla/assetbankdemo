Feature: Login

Scenario: Login Success
Given I am on my Assetbank login page
And I enter a valid email for my server
And I enter associated valid password
When I opt to Login
Then I am logged in
When I opt to logout
Then I get logged out


Scenario: Login attempt wrong password
Given I am on my Assetbank login page
And I enter a valid email for my server
And I enter a valid incorrect password
When I opt to Login
Then I am told my details are incorrect