Feature: Create property scenarios in Expert
  Scenario Outline: Verify create&update sale property works as expected
    Given I generate token for Expert "eg"
    When I send POST request with "expertApi" for creating sale property "<category>" "<propertyType>" "eg" "null"
    Then I validate status code is 201
    When I send GET request for property by id "null"
    Then I validate status code is 200
    And I verify response with property details
    When I update sale property with "expertApi" "<propertyType>" "updated title - API AUTOMATION" "eg" "null"
    Then I verify response is updated "updated title - API AUTOMATION" in "eg"
    Examples:
      | category    | propertyType |
      | residential | 1            |
      | residential | 5            |
      | residential | 4            |
      | residential | 8            |
      | residential | 9            |
      | residential | 10           |
      | residential | 11           |
      | residential | 31           |
      | residential | 32           |
      | residential | 37           |
      | residential | 58           |
      | residential | 59           |
      | residential | 60           |
      | residential | 61           |
      | commercial  | 13           |
      | commercial  | 16           |
      | commercial  | 18           |
      | commercial  | 19           |
      | commercial  | 20           |
      | commercial  | 23           |
      | commercial  | 24           |
      | commercial  | 27           |
      | commercial  | 62           |
      | commercial  | 63           |
      | commercial  | 48           |
      | commercial  | 34           |
      | commercial  | 25           |