
from Models.DbRef import db, ma, BaseModel
from marshmallow import EXCLUDE
from flask_login import UserMixin

class UsersModel(UserMixin, BaseModel):
    __tablename__ = 'Users'
    email = db.Column(db.String(128), primary_key=True)                 # Email
    name = db.Column(db.String(128), nullable=False)                    # Name
    department = db.Column(db.String(32), default='OTHERS')             # Department

class UsersSchema(ma.ModelSchema):
    class Meta:
        unknown = EXCLUDE
        model = UsersModel
        sqla_session = db.session
        include_fk = True
        strict = True
