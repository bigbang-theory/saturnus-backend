from ..main import db
from datetime import datetime
import sqlalchemy
import uuid

class AuthUser(db.Model):
    __tablename__ = 'auth_users'

    user_id = sqlalchemy.Column(sqlalchemy.String(36), primary_key=True, default=str(uuid.uuid4()))
    username = sqlalchemy.Column(sqlalchemy.String(80), nullable=False)
    password = sqlalchemy.Column(sqlalchemy.String(80), nullable=False)

    created_at = sqlalchemy.Column(sqlalchemy.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = sqlalchemy.Column(sqlalchemy.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return '<AuthUser %s>' % self.username