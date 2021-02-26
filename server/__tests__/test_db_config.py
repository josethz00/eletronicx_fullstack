from flask import Flask
from datetime import datetime
import hashlib

from src.shared.database.db import db
from src.shared.database.sql_connector import SQLConnector
from app import create_app
from config import variables


def test_db_url_is_loaded(app: Flask):
    assert bool(app.config['SQLALCHEMY_DATABASE_URI']) is True


def test_db_url_is_correct(app: Flask):
    db_conn = SQLConnector()
    assert app.config['SQLALCHEMY_DATABASE_URI'] == db_conn.connection_url


def test_db_is_responsive(app: Flask):
    with app.app_context():
        if variables.FLASK_ENV == 'testing':
            db.drop_all()
            db.create_all()

            hashed_password = hashlib.blake2b(bytes(
                'br123456789',
                'utf-8')).hexdigest()

            table_name = "users"
            ls_cols = [
                "username",
                "email",
                "password",
                "role",
                "created_at",
                "updated_at"
            ]
            ls_vals = [
                f'''('José Thomaz',
                'jtsoares17@hotmail.com',
                '1234567890', 'admin',
                '{datetime.utcnow()}',
                '{datetime.utcnow()}'
                )''',
                f'''('José',
                'josethomaz2003@gmail.com',
                '1234567890', 'admin',
                '{datetime.utcnow()}',
                '{datetime.utcnow()}'
                )''',
                f'''('Thomaz',
                'josefhasmussen@gmail.com',
                '1234567890', 'admin',
                '{datetime.utcnow()}',
                '{datetime.utcnow()}'
                )''',
                f'''('Rei delas',
                'reidelasns@gmail.com',
                '{hashed_password}', 'admin',
                '{datetime.utcnow()}',
                '{datetime.utcnow()}'
                )'''
            ]
            s_cols = ', '.join(ls_cols)
            s_vals = ', '.join(ls_vals)
            db.engine.execute(
                f"INSERT INTO {table_name} ({s_cols}) VALUES {s_vals}"
            )

        else:
            print('You should change your flask_env variable to testing')
