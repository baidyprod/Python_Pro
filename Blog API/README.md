# DRF Project by baidy

This is a Django REST Framework (DRF) project that provides an API for managing publications and comments. The project allows authenticated users to create, view, update, and delete publications, as well as add comments to publications.

## Installation

1. Clone the repository:

```shell
git clone https://github.com/your/repository.git
```

2. Install the project dependencies. It is recommended to use a virtual environment:

```shell
cd project-directory
python -m venv venv
source venv/bin/activate  # For Unix/Linux
venv\Scripts\activate  # For Windows
pip install -r requirements.txt
```

3. Create an environmental variable SECRET_KEY (just a huge password):

```shell
export SECRET_KEY="wcnou34chg874cg4yg74ycgowrg49rf38fr87dvy7238hvhsudvsj"
```

4. Apply the database migrations:

```shell
python manage.py migrate
```

5. Create two users (e.g. superusers): run this command twice:

```shell
python manage.py createsuperuser
```

6. Run the development server:

```shell
python manage.py runserver
```

The project should now be running on `http://localhost:8000/`.

## API Endpoints

### Publications

- `GET /publications/` - Retrieves a list of all publications.
- `POST /publications/` - Creates a new publication.
- `GET /publications/{id}/` - Retrieves a specific publication by its id.
- `PUT /publications/{id}/` - Updates a specific publication by its id.
- `DELETE /publications/{id}/` - Deletes a specific publication by its id.

### Comments

- `GET /comments/` - Retrieves a list of all comments.
- `POST /comments/` - Creates a new comment.
- `GET /comments/{id}/` - Retrieves a specific comment by its id.
- `PUT /comments/{id}/` - Updates a specific comment by its id.
- `DELETE /comments/{id}/` - Deletes a specific comment by its id.

## Authentication and Permissions

- The API uses token, session-based, and basic authentication. Users can authenticate using their username and password.
- To obtain a token, make a POST request to `/api-token-auth/` with valid credentials. The response will include a token that can be used for subsequent requests.
- Only authenticated users can create, update, and delete publications or add comments.
- Publications and comments can only be modified or deleted by their respective authors.

## Pagination

By default, the API uses page number pagination with a page size of 10. This can be adjusted in the `settings.py` file.

## Serializers

- The project uses serializers to convert model instances to JSON format and vice versa.
- The `PublicationSerializer` is responsible for serializing/deserializing the `Publication` model.
- The `CommentSerializer` is responsible for serializing/deserializing the `Comment` model.

## Models

The project includes the following models:

- `Publication`: Represents a publication with a title, description, author, and creation timestamp.
- `Comment`: Represents a comment associated with a publication, including the author, text, and creation timestamp.

## Permissions

The project includes a custom permission class, `IsOwnerOrReadOnly`, which allows read access to all users but only allows modification or deletion by the author of the publication or comment.

___Feel free to explore and have fun!___