**Overview**

The Simple Note Taking API is a RESTful web service built using Django and Django REST Framework. It provides endpoints for creating, fetching, querying, and updating notes without user management. This README provides information on how to use the API, its endpoints, and other relevant details for developers.

**Getting Started**

Installation
1. Clone this repository to your local machine-

    git clone https://github.com/developer-py/Note-Taking-API.git
3. Install dependencies-

    pip install -r requirements.txt
5. Apply migrations:

    python manage.py migrate

7. Run the development server-

    python manage.py runserver
 

The API will be accessible at http://localhost:8000/


**API Endpoints**

The following endpoints are available:

    POST /notes/: Create a new note.

    GET /notes/: Fetch all note.
   
    GET /notes/<pk>/: Fetch a note by its primary key.

    GET /notes?title=<substring>: Search notes by title substring.

    PUT/PATCH /notes/<pk>/: Update an existing note.



**Usage**

   **Creating a Note**

     To create a new note, send a POST request to the /notes/ endpoint with the following JSON payload-

        {
          "title": "Note Title",
          "body": "Note Body"
        }

   **Fetching a Note**

    To fetch a note by its primary key, send a GET request to the /notes/<pk>/ endpoint, where <pk> is the primary key of the note.
  
  **Querying Notes by Title Substring**
  
    To Search notes by a substring present in the note's title, send a GET request to the /notes? endpoint with the title query parameter set to the desired substring.

  **Updating a Note**
   
   To update an existing note, send a PUT request to the /notes/<pk>/ endpoint with the updated note data in the request body.
  
**Testing**

 To run the test suite, use the following command-

  python manage.py test


**Error Handling**

The API returns appropriate HTTP status codes.



  

