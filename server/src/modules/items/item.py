from datetime import datetime
from dataclasses import dataclass

from src.shared.database.db import db


@dataclass
class Item(db.Model):

    id: int
    name: str
    price: float
    image_url: str
    quantity: str
    created_at: datetime
    updated_at: datetime
    category_id: int

    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    image_url = db.Column(
        db.String(120),
        nullable=True,
        default='https://makitweb.com/demo/broken_image/images/noimage.png'
    )
    quantity = db.Column(
        db.Integer,
        nullable=False,
        default=0
    )
    created_at = db.Column(
        db.DateTime(),
        default=datetime.utcnow(),
        nullable=False
    )
    updated_at = db.Column(
        db.DateTime(),
        default=datetime.utcnow(),
        onupdate=datetime.utcnow(),
        nullable=False
    )
    category_id = db.Column(
        db.Integer,
        db.ForeignKey('categories.id'),
        nullable=False
    )

    def __repr__(self):
        return '<Item %r>' % self.id
