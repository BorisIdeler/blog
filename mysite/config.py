import os


class Config:

    # Secret key
    SECRET_KEY = os.environ.get('BLOG_SECRET_KEY') or ''

    # Recaptcha key
    GOOGLE_RECAPTCHA_SECRET_KEY = os.environ.get(
        'BLOG_GOOGLE_RECAPTCHA_SECRET_KEY') or ''

    # Debug
    DEBUG = bool(os.environ.get('BLOG_DEBUG') or True)

    # Database
    BLOG_DB_HOST = os.environ.get('BLOG_DB_HOST') or ''
    BLOG_DB_NAME = os.environ.get('BLOG_DB_NAME') or ''
    BLOG_DB_PORT = os.environ.get('BLOG_DB_PORT') or ''
    BLOG_DB_USER = os.environ.get('BLOG_DB_USER') or ''
    BLOG_DB_PASSWORD = os.environ.get('BLOG_DB_PASSWORD') or ''

    # Celery
    BLOG_REDIS_URL = os.environ.get('BLOG_REDIS_URL') or ''
