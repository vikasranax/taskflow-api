# TaskFlow — Test Cases

## TC-01: Create a task with valid data
**Steps:**
1. Send POST /api/tasks with title="Buy groceries", description="Milk, eggs, bread"
**Expected:** Task created, returns id, title, description, completed=false
**Status:** ✅ Pass

## TC-02: Get all tasks
**Steps:**
1. Send GET /api/tasks
**Expected:** Returns array of all created tasks
**Status:** ✅ Pass

## TC-03: Create a task with empty title
**Steps:**
1. Send POST /api/tasks with title="", description="test"
**Expected:** Should be rejected with a validation error
**Actual:** Task gets created anyway with empty title
**Status:** ❌ FAIL — this is a real bug

## TC-04: Update a task that doesn't exist
**Steps:**
1. Send PUT /api/tasks/9999 (an id that was never created)
**Expected:** Should return a clear 404 "not found" error
**Actual:** Returns {"error": "Task not found"} but with HTTP 200 status instead of 404
**Status:** ❌ FAIL — wrong status code, hard for other systems to detect this as an error

## TC-05: Delete a task that doesn't exist
**Steps:**
1. Send DELETE /api/tasks/9999
**Expected:** Should return 404
**Actual:** Same issue as TC-04 — returns 200 with an error message inside the body
**Status:** ❌ FAIL

## TC-06: Send task_id as text instead of a number
**Steps:**
1. Send PUT /api/tasks/abc
**Expected:** Should return a clear validation error (422)
**Actual:** FastAPI correctly rejects it — "Value must be an integer"
**Status:** ✅ Pass — type validation on path params works automatically

## TC-07: Create task with missing description field
**Steps:**
1. Send POST /api/tasks with only title, no description
**Expected:** Should be rejected since description is required
**Actual:** Returns 422 with "Field required" — description is a mandatory field
**Status:** ✅ Pass — Pydantic correctly enforces required fields