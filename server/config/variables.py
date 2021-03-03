import os

os.environ['HOST'] = '0.0.0.0'
os.environ['PORT'] = '5000'
os.environ['SQL_DATABASE'] = 'postgresql'
os.environ['DATABASE_USER'] = 'postgres'
os.environ['DATABASE_PASSWORD'] = 'docker'
os.environ['DATABASE_NAME'] = 'flask_luby_test'
os.environ['DATABASE_HOST'] = '192.168.15.6'
os.environ['DATABASE_PORT'] = '5434'
os.environ['FLASK_ENV'] = 'development'
os.environ['SECRET_KEY'] = 'flask/7c4ed787-e708-4fe1-837d-6beb3320697f'
os.environ['MAIL_SERVER'] = 'smtp.mailtrap.io'
os.environ['MAIL_PORT'] = '2525'
os.environ['MAIL_USERNAME'] = 'e67f4bf7c074a1'
os.environ['MAIL_PASSWORD'] = '6f26693be07364'
os.environ['S3_BUCKET'] = 'pythonlubytest'
os.environ['S3_ACCESS_KEY'] = 'AKIAIS5QHZPSJQIQXLPA'
os.environ['S3_SECRET_ACCESS_KEY'] = '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'


HOST = os.environ.get('HOST')
PORT = os.environ.get('PORT')
DEBUG = True
SQL_DATABASE = os.environ.get('SQL_DATABASE')
DATABASE_USER = os.environ.get('DATABASE_USER')
DATABASE_PASSWORD = os.environ.get('DATABASE_PASSWORD')
DATABASE_NAME = os.environ.get('DATABASE_NAME')
DATABASE_HOST = os.environ.get('DATABASE_HOST')
DATABASE_PORT = os.environ.get('DATABASE_PORT')
FLASK_ENV = os.environ.get('FLASK_ENV')
SECRET_KEY = os.environ.get('SECRET_KEY')
MAIL_SERVER = os.environ.get('MAIL_SERVER')
MAIL_PORT = os.environ.get('MAIL_PORT')
MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
MAIL_USE_TLS = True
MAIL_USE_SSL = False
S3_BUCKET = os.environ.get('S3_BUCKET')
S3_ACCESS_KEY = os.environ.get('S3_ACCESS_KEY')
S3_SECRET_ACCESS_KEY = os.environ.get('S3_SECRET_ACCESS_KEY')
S3_LOCATION = f'http://{S3_BUCKET}.s3.amazonaws.com/'
