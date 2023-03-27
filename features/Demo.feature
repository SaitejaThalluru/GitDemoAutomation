Feature: Hero logo
  Scenario: opening URL
    Given launch browser
    When enter URL
    Then page should open
    And wait for sometime
    And Tap on chat icon
    And Close the browser
