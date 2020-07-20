
from Models.DbRef import db, ma
from marshmallow import EXCLUDE

class ProductsModel(db.Model):
    __tablename__ = 'Products'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)                    # Id
    name = db.Column(db.String(64), unique=True, nullable=False)                        # Product name
    schema = db.Column(db.String(64), nullable=False)                                   # Schema
    table = db.Column(db.String(64), nullable=False)                                    # Table

class ProductsSchema(ma.ModelSchema):
    class Meta:
        unknown = EXCLUDE
        model = ProductsModel
        sqla_session = db.session
        include_fk = True
        strict = True

