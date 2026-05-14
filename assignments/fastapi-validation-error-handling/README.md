# 📘 Assignment: FastAPI Input Validation and Error Handling

## 🎯 Objective

Build a beginner-friendly FastAPI service that validates incoming data and returns clear error messages. By the end of this assignment, you will use Pydantic models, field constraints, and HTTP exceptions to make your API more reliable.

## 📝 Tasks

### 🛠️	Create a Validated Request Model

#### Description
Set up a FastAPI app and define a request model for a simple `Task` resource. Add field rules so invalid data is automatically rejected.

#### Requirements
Completed program should:

- Create a FastAPI app in `starter-code.py`.
- Define a Pydantic model named `TaskCreate` with fields `title` and `priority`.
- Enforce validation rules:
  - `title` must be at least 3 characters long.
  - `priority` must be an integer between 1 and 5.
- Implement `POST /tasks` that accepts valid input and returns the created task.


### 🛠️	Handle API Errors Clearly

#### Description
Add error handling so API responses are helpful when users send bad data or request a missing resource.

#### Requirements
Completed program should:

- Store tasks in memory using a dictionary.
- Implement `GET /tasks/{task_id}`.
- Return `404 Not Found` with a clear message when `task_id` does not exist.
- Return structured JSON responses for success and failure cases.
- Show one sample request and response for both success and error cases.

#### Example
```json
POST /tasks
{
  "title": "Study FastAPI",
  "priority": 3
}
```

```json
201 Created
{
  "id": 1,
  "title": "Study FastAPI",
  "priority": 3
}
```

```json
GET /tasks/999
```

```json
404 Not Found
{
  "detail": "Task not found"
}
```
