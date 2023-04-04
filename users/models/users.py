from ..main import db
from datetime import datetime
import sqlalchemy as sa
import uuid

class User(db.Model):
    __tablename__ = 'user'

    user_id = sa.Column(sa.String(36), primary_key=True, default=str(uuid.uuid4()))
    first_name = sa.Column(sa.String(80), nullable=False)
    last_name = sa.Column(sa.String(80), nullable=False)
    email = sa.Column(sa.String(120), unique=True, nullable=False)

    address_id = sa.Column(sa.Integer, sa.ForeignKey('addresses.address_id'), nullable=False)
    role_id = sa.Column(sa.Integer, sa.ForeignKey('roles.role_id'), nullable=False)

    created_at = sa.Column(sa.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = sa.Column(sa.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return '<User %s>' % self.first_name
    
class Role(db.Model):
    __tablename__ = 'role'

    role_id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(80), unique=True, nullable=False)

    def __repr__(self):
        return '<Role %s>' % self.name

class Address(db.Model):
    __tablename__ = 'address'

    address_id = sa.Column(sa.Integer, unique=True, nullable=False)
    name = sa.Column(sa.String(240), nullable=False)
    phone = sa.Column(sa.String(12), nullable=False)
    address = sa.Column(sa.String(120), nullable=False)
    city = sa.Column(sa.String(80), nullable=False)
    state = sa.Column(sa.String(80), nullable=False)
    country = sa.Column(sa.String(40), nullable=False)
    post_code = sa.Column(sa.String(8), nullable=False)
    created_at = sa.Column(sa.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = sa.Column(sa.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return '<Address %s>' % self.name