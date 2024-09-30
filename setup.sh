#!/bin/bash

# Create project directories
mkdir -p project-directory/templates project-directory/static

# Create necessary files
touch project-directory/app.py
touch project-directory/templates/login.html
touch project-directory/static/style.css

# Print instructions
echo "Project structure created. Now populate the files as needed."
echo "Use 'python app.py' to run your Flask application."
