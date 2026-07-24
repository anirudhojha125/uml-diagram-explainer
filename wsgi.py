from app import app

# WSGI entry point - Gunicorn expects 'application'
application = app

if __name__ == "__main__":
    application.run()