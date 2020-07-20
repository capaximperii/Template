from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from datetime import datetime

db = SQLAlchemy(session_options={'autoflush': False, 'autocommit': False, 'expire_on_commit': False })
ma = Marshmallow()

class BaseModel(db.Model):
    __abstract__ = True
    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)    # Creation time
    updated = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)    # Updation time

    def insert(self):
        db.session.add(self)
        db.session.commit()
    
    def update(self):
        self.Updated = datetime.utcnow()
        db.session.add(self)
        db.session.commit()
