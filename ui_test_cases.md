## UI Tests: Manager Page Tests

## Test Case 1: Add Customer

1. Navigate to addCust page
2. Fill in post code, name, last name
3. Submit new customer
4. Check alert with message "Customer added successfully"
5. Navigate to customers list
6. Check if new customer is added

**Expected Results:**
 - After submitting the customer, an alert should be displayed with the message "Customer added successfully."
 - After navigating to the customers list, the new customer should appear in the list with the correct details (post code, name, last name).

## Test Case 2: Sort customers by name in asc order

1. Navigate to customers list page
2. Click Name link in table head
3. Check if list is sorted

**Expected Results:**
 - The customers list should be sorted by name in ascending alphabetical order (e.g., A-Z).

## Test Case 3: Delete a customer based on name length
1. Navigate to customers list page
2. Search for a name based on math condition
3. Hit delete button
4. Verify deletion

**Expected Results:**
 - The correct customer should be identified based on the name length condition.
 - After hitting the delete button, the customer should be removed from the customers list.