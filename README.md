# Movie-Review-API

Functionality
The API provides the following key features:

User Management:

Register, Login, and Logout: Users can sign up with a unique username, email, and password. Once registered, users can log in to create, update, or delete their reviews.
CRUD Operations for Users: Users can manage their profiles by updating or deleting their account details.
Authentication: The API uses token-based authentication (JWT) for secure access. Only authenticated users can create or modify their own reviews.
Review Management (CRUD):

Create a Review: Users can post reviews for any movie by submitting the movie title, review content, and a rating (1-5 stars).
Read Reviews: Users can view reviews of any movie. The API supports pagination and sorting to make it easier to browse reviews, especially for popular movies with many reviews.
Update and Delete Reviews: Authenticated users can update or delete only the reviews they have submitted. Permission checks ensure that no user can modify or delete another user's reviews.
Search and Filtering:

Search Reviews by Movie Title: Users can search for reviews of specific movies using movie titles.
Filter by Rating: Users can filter reviews based on ratings (e.g., show only 4-star or 5-star reviews).
Database Management:

Django ORM: The application uses Django's Object-Relational Mapping (ORM) to handle database operations. The review and user data is stored in a database managed by Django.
Deployment:

The API is deployed to Heroku, using Gunicorn as the WSGI server for running the application. Heroku manages the static files and database connection for the production environment.
Key Files and Code Structure
models.py: Defines the Review and User models, which handle the structure of review data and user information.
serializers.py: Converts Review and User model instances into JSON format to be sent to the frontend, and validates incoming data for creating or updating reviews.
views.py: Contains the core logic of the API, such as handling user authentication, review management (CRUD operations), and filtering reviews based on user input.
urls.py: Maps URL patterns to the views, ensuring that each API endpoint works as intended.
settings.py: Contains the configuration for both the development and production environments, including database setup, installed applications, and middleware.