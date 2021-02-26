from datetime import datetime
from dataclasses import dataclass

from src.shared.database.db import db


@dataclass
class Category(db.Model):

    id: int
    name: str

    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(60), nullable=False)
    item = db.relationship(
        'Item',
        backref='items',
        cascade='all, delete-orphan',
        uselist=True
    )

    def __repr__(self):
        return '<Category %r>' % self.id
