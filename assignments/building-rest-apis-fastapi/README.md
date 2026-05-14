# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to design and implement RESTful APIs using the FastAPI framework in Python. By the end of this assignment, you will have built a simple API with endpoints for creating, reading, updating, and deleting resources.

## 📝 Tasks

### 🛠️	Set Up FastAPI Project

#### Description
Initialize a new FastAPI project and set up the basic application structure.

#### Requirements
Completed program should:

- Install FastAPI and Uvicorn.
- Create a main application file (e.g., `main.py`).
- Start a development server and verify a basic root endpoint returns a welcome message.


### 🛠️	Implement CRUD Endpoints

#### Description
Add endpoints to your FastAPI app to support Create, Read, Update, and Delete (CRUD) operations for a simple resource (e.g., items, users, or books).

#### Requirements
Completed program should:

- Define a Pydantic model for your resource.
- Implement endpoints for POST (create), GET (read), PUT (update), and DELETE (delete).
- Return appropriate status codes and JSON responses for each operation.
- (Optional) Store data in-memory using a Python dictionary.

#### Example
```python
# Example: GET /items/1
{
  "id": 1,
  "name": "Sample Item"
}
```
