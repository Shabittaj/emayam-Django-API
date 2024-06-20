"""
WSGI config for myproject project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# Set the Django settings module for the application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

# Get the WSGI application
application = get_wsgi_application()

# Optional: Specify the port if needed
port = os.getenv('PORT', default='8000')  # Default port is 8000, adjust as necessary

# Make the application callable with the specified port
def application_with_port(environ, start_response):
    environ['SERVER_PORT'] = port
    return application(environ, start_response)

# Set the application variable to the callable application with port
application = application_with_port
