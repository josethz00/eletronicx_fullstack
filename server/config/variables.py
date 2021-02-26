import os

os.environ['HOST'] = '0.0.0.0'
os.environ['PORT'] = '5000'
os.environ['SQL_DATABASE'] = ''
os.environ['DATABASE_USER'] = ''
os.environ['DATABASE_PASSWORD'] = ''
os.environ['DATABASE_NAME'] = ''
os.environ['DATABASE_HOST'] = ''
os.environ['DATABASE_PORT'] = ''
os.environ['FLASK_ENV'] = ''
os.environ['SECRET_KEY'] = ''
os.environ['MAIL_SERVER'] = ''
os.environ['MAIL_PORT'] = ''
os.environ['MAIL_USERNAME'] = ''
os.environ['MAIL_PASSWORD'] = ''
os.environ['S3_BUCKET'] = ''
os.environ['S3_ACCESS_KEY'] = ''
os.environ['S3_SECRET_ACCESS_KEY'] = ''


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
