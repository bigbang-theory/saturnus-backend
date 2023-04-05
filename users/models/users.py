from ..main import db
from datetime import datetime
import sqlalchemy
import uuid

class User(db.Model):
    __tablename__ = 'users'

    user_id = sqlalchemy.Column(sqlalchemy.String(36), primary_key=True, default=str(uuid.uuid4()))
    first_name = sqlalchemy.Column(sqlalchemy.String(80), nullable=False)
    last_name = sqlalchemy.Column(sqlalchemy.String(80), nullable=False)
    email = sqlalchemy.Column(sqlalchemy.String(120), unique=True, nullable=False)

    address_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('addresses.address_id'), nullable=False)
    role_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('roles.role_id'), nullable=False)

    created_at = sqlalchemy.Column(sqlalchemy.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = sqlalchemy.Column(sqlalchemy.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return '<User %s>' % self.first_name