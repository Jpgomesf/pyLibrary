# pyLibrary

pyLibrary is a Python-based REST API for managing a bookstore. This project aims to integrate OpenAI's language model to recommend books from the local library based on user preferences. The API is built with Flask, SQLAlchemy, PostgreSQL, and Docker.

## Features

- User management (CRUD)
- Book management (CRUD)
- Book recommendations based on user preferences
- Swagger API documentation

## Project Structure

\`\`\`
bookstore-api/
├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── controllers/
│   │   ├── book_controller.py
│   │   └── user_controller.py
│   ├── services/
│   │   ├── book_service.py
│   │   └── user_service.py
│   ├── repositories/
│   │   ├── book_repository.py
│   │   └── user_repository.py
│   ├── models/
│   │   ├── book.py
│   │   └── user.py
│   ├── routes.py
├── migrations/
├── db-data/
├── venv/
├── .gitignore
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
├── run.py
└── seeder.py
\`\`\`

## Getting Started

### Prerequisites

- Python 3.8+
- Docker
- PostgreSQL

### Installation

1. **Clone the repository**:
   \`\`\`sh
   git clone https://github.com/your-username/pyLibrary.git
   cd pyLibrary
   \`\`\`

2. **Set up the virtual environment**:
   \`\`\`sh
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   # or
   venv\Scripts\activate  # On Windows
   \`\`\`

3. **Install dependencies**:
   \`\`\`sh
   pip install -r requirements.txt
   \`\`\`

4. **Set up the database**:
   Make sure your PostgreSQL service is running. You can use Docker to run PostgreSQL:
   \`\`\`sh
   docker-compose up -d db
   \`\`\`

5. **Run database migrations**:
   \`\`\`sh
   flask db upgrade
   \`\`\`

6. **Seed the database with initial data**:
   \`\`\`sh
   python seeder.py
   \`\`\`

### Running the Application

1. **Run the Flask application**:
   \`\`\`sh
   flask run
   \`\`\`

2. **Access the application**:
   Open your browser and go to [http://127.0.0.1:5000](http://127.0.0.1:5000).

3. **Access Swagger documentation**:
   Open your browser and go to [http://127.0.0.1:5000/apidocs](http://127.0.0.1:5000/apidocs).

### API Endpoints

- **Books**
  - \`GET /books\`: Get all books
  - \`POST /books\`: Add a new book
  - \`GET /books/<id>\`: Get a book by ID
  - \`PUT /books/<id>\`: Update a book by ID
  - \`DELETE /books/<id>\`: Delete a book by ID

- **Users**
  - \`GET /users\`: Get all users
  - \`POST /users\`: Add a new user
  - \`GET /users/<id>\`: Get a user by ID
  - \`PUT /users/<id>\`: Update a user by ID
  - \`DELETE /users/<id>\`: Delete a user by ID
  - \`GET /users/<id>/recommendations\`: Get book recommendations for a user

## Integration with OpenAI

To integrate OpenAI's language model for book recommendations, follow these steps:

1. **Install OpenAI SDK**:
   \`\`\`sh
   pip install openai
   \`\`\`

2. **Set up OpenAI configuration**:
   Add your OpenAI API key to your environment variables or configuration file.

3. **Update the recommendation service**:
   Modify the \`recommend_books\` method in \`user_service.py\` to use OpenAI's API for generating recommendations.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
