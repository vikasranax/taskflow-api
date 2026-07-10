# TaskFlow - Test Plan

## What we're testing
The TaskFlow REST API - task creation, retrieval, updating, and deletion.

## Endpoints in scope
- GET /api/tasks
- POST /api/tasks
- PUT /api/tasks/{task_id}
- DELETE /api/tasks/{task_id}

## Test types

### 1. Positive tests 
Confirm the API works correctly with valid, expected input.

### 2. Negative tests
Confirm the API handles bad input gracefully instead of crashing.

### 3. Edge cases
Boundary conditions - empty strings, missing fields, non-existent IDs.

## Known risk areas (things likely to break)
- No validation on `title` - can it be empty?
- No check on task_id type - what if someone sends "abc" instead of a number?
- Data is stored in memory - is state consistent across requests?
- Updating/deleting a task that doesn't exist - does it crash or respond gracefully?