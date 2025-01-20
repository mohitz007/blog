# Simple Blog with CRUD Functionality

This project is a simple blogging platform that supports basic Create, Read, Update, and Delete (CRUD) functionality. Only authenticated users are allowed to update blogs.

## Features

- Create new blog posts.
- View a list of all blog posts.
- Update existing blog posts (authentication required).
- Delete blog posts.
- User authentication to restrict access to specific operations.

## Requirements

To run this project locally, you'll need:

- Python 3.9+
- Django 4.0+
- SQLite (default Django database)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/simple-blog.git
   cd simple-blog
   ```

2. Create a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run migrations to set up the database:

   ```bash
   python manage.py migrate
   ```

5. Create a superuser to access the admin panel:

   ```bash
   python manage.py createsuperuser
   ```

6. Start the development server:

   ```bash
   python manage.py runserver
   ```

## Usage

### Create a Blog Post

1. Navigate to the `/admin` URL and log in with your superuser credentials.
2. Add a new blog post from the admin interface.

### View Blog Posts

Visit the homepage (`/`) to see a list of all blog posts.

### Update a Blog Post

1. Ensure you are logged in as an authenticated user.
2. Navigate to the post you want to update and click the "Edit" button.

### Delete a Blog Post

1. Log in as an authenticated user.
2. Navigate to the post you want to delete and click the "Delete" button.

## Authentication

- Only logged-in users can access the update functionality.
- Registration and login pages are provided for user authentication.

## Project Structure

```plaintext
simple-blog/
├── blog/                # Blog app (CRUD functionality)
├── simple_blog/         # Project settings
├── templates/           # HTML templates
├── static/              # Static files (CSS, JS, images)
├── db.sqlite3           # SQLite database
├── manage.py            # Django management script
├── requirements.txt     # Project dependencies
```

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

Feel free to customize this README for your specific use case.

