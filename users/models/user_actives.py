from ..main import db
import sqlalchemy

class UserActive(db.Model):
    __tablename__ = 'user_actives'

    user_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('auth_users.user_id'), nullable=False)
    access_token = sqlalchemy.Column(sqlalchemy.String(32))

    def __repr__(self):
        return '<UserActive %s>' % self.user_id