# Famous Women API

[Youtube](https://youtu.be/mVnHv9U0YKk)
## Description
This Django Rest Framework API serves information about famous women throughout history. It provides endpoints to access details such as biographical information, achievements, and contributions of notable women.

## Features
- Retrieve a list of famous women
- Get detailed information about a specific woman
- Add new entries of famous women
- Update existing entries
- Delete entries

## Installation
1. Clone this repository to your local machine:
`https://github.com/kaydurgu/midbackend.git`
2. Navigate to the project directory:
```cd midbackend```
3. Create a virtual environment:
```python -m venv env```
4. Activate the virtual environment:
- On Windows:
  ```
  .\env\Scripts\activate
  ```
- On macOS and Linux:
  ```
  source env/bin/activate
  ```
5. Install dependencies:
```pip install -r requirements.txt```
6. Apply migrations:
```python manage.py migrate```
7. Run the development server:
```python manage.py runserver```

## Endpoints

### Category Update Data
- **PUT** `/catergory_update_data/{id}`
  - **Description:** Update data for a specific category.
  - **View Function:** `catergory_update_data_update`

- **PATCH** `/catergory_update_data/{id}`
  - **Description:** Partially update data for a specific category.
  - **View Function:** `catergory_update_data_partial_update`

### Category List
- **GET** `/catergorylist/`
  - **Description:** Retrieve a list of categories.
  - **View Function:** `catergorylist_list`

- **POST** `/catergorylist/`
  - **Description:** Create a new category.
  - **View Function:** `catergorylist_create`

### Women Detail
- **GET** `/womendetail/{id}/`
  - **Description:** Retrieve details of a specific woman.
  - **View Function:** `womendetail_read`

- **PUT** `/womendetail/{id}/`
  - **Description:** Update details of a specific woman.
  - **View Function:** `womendetail_update`

- **PATCH** `/womendetail/{id}/`
  - **Description:** Partially update details of a specific woman.
  - **View Function:** `womendetail_partial_update`

- **DELETE** `/womendetail/{id}/`
  - **Description:** Delete a specific woman.
  - **View Function:** `womendetail_delete`

### Women List
- **GET** `/womenlist/`
  - **Description:** Retrieve a list of women.
  - **View Function:** `womenlist_list`

- **POST** `/womenlist/`
  - **Description:** Create a new woman.
  - **View Function:** `womenlist_create`

### Women List Update Data
- **PUT** `/womenlist_update_data/{id}/`
  - **Description:** Update data for a specific woman in the list.
  - **View Function:** `womenlist_update_data_update`

- **PATCH** `/womenlist_update_data/{id}/`
  - **Description:** Partially update data for a specific woman in the list.
  - **View Function:** `womenlist_update_data_partial_update`
## Models

### Category
```json
{
  "name": {
    "type": "string",
    "title": "Name",
    "maxLength": 255,
    "minLength": 1
  }
}
```
### Women
```json
{
  "title": {
    "type": "string",
    "title": "Title",
    "maxLength": 255,
    "minLength": 1
  },
  "content": {
    "type": "string",
    "title": "Content",
    "minLength": 1
  },
  "time_create": {
    "type": "string",
    "format": "date-time",
    "title": "Time create",
    "readOnly": true
  },
  "time_update": {
    "type": "string",
    "format": "date-time",
    "title": "Time update",
    "readOnly": true
  },
  "is_published": {
    "type": "boolean",
    "title": "Is published",
    "default": true
  },
  "cat_id": {
    "type": "integer",
    "title": "Cat id"
  }
}
```
