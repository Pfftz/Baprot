# Alpha and Omega: Django CRUD Library Management System

Alpha and Omega is a simple Django project that demonstrates CRUD (Create, Read, Update, Delete) operations for a library management system. 
This project provides a web-based interface for managing books and their borrowing status.

## Features

- User authentication
- CRUD operations for books
- Book borrowing functionality
- Admin interface for managing the library inventory

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed
- pip (Python package manager) installed

## Install pipenv

In this project i use pipenv, so you need to install it first using this command:

    pip install pipenv

## Install Required Packages

To install it use the following command:

    pipenv install

## Activate the virtual environment

To run it:

    pipenv shell

## Before running the application we need to create the needed DB tables:

    ./manage.py migrate

## Now you can run the development web server:

    ./manage.py runserver

## Creating an Admin User

To access the admin interface and the `books_fbv_admin` section, you need to create a superuser:

    ./manage.py createsuperuser

## Usage

- Access the admin interface at `http://127.0.0.1:8000/admin/`
- Use the created superuser credentials to log in
- Navigate to the `books_fbv_admin` section to manage books

## Project Structure

- `apps`: Contains the main Django application
- `theme`: Handles basic features like login, register, logout, about, home, and contact form
- `books_fbv_admin`: Provides CRUD functionality for books
