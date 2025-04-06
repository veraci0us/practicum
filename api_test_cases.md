## API Test Cases

## Test Case 1: Create Entity

**Preconditions:**
- A valid payload is provided for the creation of a new entity.

Steps:

1. Send a POST request to create a new entity.

2. Check if the response code is 200 OK.

3. Retrieve the created entity by its ID.

4. Check if the fields of the created entity match the expected values.

5. Check if the entity matches the initial payload.

6. Clean up by deleting the entity.

**Expected Results:**

 - After sending the POST request, the entity should be created successfully.

 - The retrieved entity should have the correct fields (matching the initial payload).

 - The created entity should match the initial payload, including the ID.

 - The entity should be deleted successfully after the test.


## Test Case 2: Delete Entity

**Preconditions:**
- Create a test entity.

Steps:

1. Send a DELETE request to remove the entity using its ID.

2. Check if the response code is 204 No Content, indicating the entity was successfully deleted.

3. Attempt to retrieve the deleted entity using the same ID.

4. Check if the response code for retrieving the entity is 500 Internal Server Error.

5. Ensure the error message indicates that no entity was found (e.g., "no rows in result set").


**Expected Results:**

 - The entity should be successfully deleted after sending the DELETE request.

 - The response code should be 204 No Content, indicating the entity was deleted.

 - Attempting to retrieve the deleted entity should result in an error code (500 Internal Server Error).

 - The error message should indicate that no entity exists for the provided ID.

 - The entity should no longer exist in the database after the test.


## Test Case 3: Get All Entities
**Preconditions:**

Multiple entities are created in the database beforehand.

Steps:

1. Send a GET request to retrieve all entities from the database.

2. Check if the response code is 200 OK.

3. Convert the retrieved entities from the database into EntityModel objects.

4. Convert the list of test entities into EntityModel objects.

5. Compare the list of test entity models with the list of all entities from the database.

6. Delete the test entities after the test (cleanup).

**Expected Results:**

- The response code should be 200 OK, indicating that the entities were successfully retrieved.

- The list of created test entities should match the list of all entities retrieved from the database.

- The entities created for the test should be cleaned up after the test.

## Test Case 4: Get Entity
**Preconditions:**

Create a test entity.

Steps:

1. Send a GET request to retrieve the entity from the database using the entity ID.

2. Check if the response code is 200 OK.

3. Verify that the fields of the retrieved entity match the expected values.

4. Check if the id of the retrieved entity matches the entity ID used to fetch it.

5. Delete the test entity after the test.

**Expected Results:**

- The response code should be 200 OK, indicating that the entity was successfully retrieved.

- The fields of the retrieved entity should match the expected values.

- The id of the retrieved entity should match the ID used to retrieve it.

- The entity should be cleaned up after the test.

## Test Case 5: Update Entity
**Preconditions:**

Create a test entity.

Steps:

1. Send a PATCH request to update the entity with the provided update_payload.

2. Check if the response code is 204 No Content, indicating that the entity was successfully updated.

3. Retrieve the updated entity using the entity ID.

4. Verify that the fields of the retrieved entity match the updated values.

5. Check if the updated entity matches the original update payload (with the entity ID included).

6. Delete the test entity after the test 

**Expected Results:**

- The response code should be 204 No Content, indicating that the entity was successfully updated.

- The retrieved entity should have the updated fields as expected.

 - The updated entity should match the provided update payload, including the correct ID.

 - The entity should be cleaned up after the test.