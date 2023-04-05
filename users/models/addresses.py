from ..main import db
from datetime import datetime
import sqlalchemy

class Address(db.Model):
    __tablename__ = 'addresses'

    address_id = sqlalchemy.Column(sqlalchemy.Integer, unique=True, nullable=False)
    name = sqlalchemy.Column(sqlalchemy.String(240), nullable=False)
    phone = sqlalchemy.Column(sqlalchemy.String(12), nullable=False)
    address = sqlalchemy.Column(sqlalchemy.String(120), nullable=False)
    city = sqlalchemy.Column(sqlalchemy.String(80), nullable=False)
    state = sqlalchemy.Column(sqlalchemy.String(80), nullable=False)
    country = sqlalchemy.Column(sqlalchemy.String(40), nullable=False)
    post_code = sqlalchemy.Column(sqlalchemy.String(8), nullable=False)
    created_at = sqlalchemy.Column(sqlalchemy.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = sqlalchemy.Column(sqlalchemy.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return '<Address %s>' % self.name