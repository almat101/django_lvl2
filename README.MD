# MODELS

### In Django, models are Python classes that represent the structure of your database tables. They define the fields (columns) and relationships between different tables. By defining models, you essentially create a blueprint for your database.

When you have created a model u have to apply this changes into django with migrations

Migrations are a powerful tool in Django that allows you to manage changes to your database schema. They track modifications made to your models and automatically generate the necessary SQL statements to apply those changes to your database.

```bash
python3 manage.py makemigration
```
+ Purpose: This command looks at the models.py file in your Django apps and detects any changes(like new models or changes to existing models). It generates a migration file that contains instructions for applying those changes to your database.
+ Output: It creates a migration file in the migrations directory of your app (e.g., 0001_initial.py for the first migration).
+ Required: Yes, this is necessary for Django to understand what changes need to be applied to the database.

```bash
python3 manage.py sqlmigrate news 0001
python3 manage.py sqlmigrate <app_name> <migration_number>
```
+ Purpose: This command takes a specific migration file (e.g., 0001) and shows the raw SQL that Django will execute when applying the migration to the database.
+ Example: python3 manage.py sqlmigrate news 0001 will show the SQL that corresponds to the migration file 0001 for the news app.
+ Importance:
This command is optional. It's primarily for debugging or learning purposes to understand what SQL will be executed.
You do not need to run this to apply migrations to your database.
+ When to use: If you're curious or want to ensure the migration is doing what you expect before running it.

```bash
python3 manage.py migrate
```
+ Purpose: This command actually applies the migrations to your database. It executes the SQL commands defined in the migration files (generated by makemigrations).
+ Required: Yes, this is essential to apply changes to the database and ensure your project is in sync with the models.

## VIEWS

### In Django, views are Python functions that handle incoming requests, process data, and return HTTP responses. They are the heart of your web application, responsible for defining the logic and behavior of your website.

## How Views Interact with Models:

1. **Fetching Data:**
 - Views can query the database using Django's ORM to retrieve data from models.
 - This data can be used to populate templates or return directly as JSON responses.
2. **Processing Data:**
 - Views can process the retrieved data, perform calculations, or apply filters.
 - This might involve data validation, formatting, or other transformations.
3. **Rendering Templates:**
 - Views can render HTML templates using data from the database.
 - Django's template engine allows you to dynamically generate HTML content.
4. **Returning Responses:**
- Views can return various types of HTTP responses, including:
  - HTML responses (rendered templates)
  - JSON responses (for API endpoints)
  - Redirect
  - Error responses

## TEMPLATES

### Templates in Django are HTML files with special syntax that allow you to dynamically generate HTML content. They provide a way to separate the presentation layer from the application logic, making your code more maintainable and reusable.

### How to Use Templates:

1. **Create a Template File:**
    - Create an HTML file in your project's `templates` directory.
    - Use the `.html` extension for template files.
2. **Define Template Variables:**
    - Use template tags like `{{ variable_name }}` to define placeholders for dynamic content.
    - These placeholders will be replaced with actual values when the template is rendered.
3. **Use Template Tags and Filters:**
    - Django provides a variety of template tags and filters to control the flow of your template and format the output.
    - For example, you can use `{% if %}`, `{% for %}`, and `{% with %}` tags to control conditional logic and loops.
    - You can use filters to format dates, numbers, and text.
4. **Render the Template:**
    - In your view, use the `render()` function to render the template and pass the necessary context data.
    - The context data is a dictionary that maps variable names to values. These values will be used to populate the template variables.
