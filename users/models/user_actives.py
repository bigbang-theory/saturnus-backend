from ..main import db
import sqlalchemy

class UserActive(db.Model):
    __tablename__ = 'user_actives'

    user_id = sqlalchemy.Column(sqlalchemy.String(36), primary_key=True, nullable=False)
    access_token = sqlalchemy.Column(sqlalchemy.String(32))

    def __repr__(self):
        return '<UserActive %s>' % self.user_id