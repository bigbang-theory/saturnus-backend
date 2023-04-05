from ..main import db
import sqlalchemy

class Role(db.Model):
    __tablename__ = 'roles'

    role_id = sqlalchemy.Column(sqlalchemy.String(8), primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String(20), unique=True, nullable=False)

    def __repr__(self):
        return '<Role %s>' % self.name