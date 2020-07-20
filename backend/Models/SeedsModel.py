import json
import datetime
import hashlib
from Models.DbRef import db

class SeedsModel(db.Model):
    __tablename__ = 'Seeds'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)                                # File name
    digest = db.Column(db.String(255), default=None)                                # Digest of file
    created = db.Column(db.DateTime, default=datetime.datetime.utcnow)              # Creation time
    updated = db.Column(db.DateTime, default=datetime.datetime.utcnow)              # Updation time

    def insert(self):
        self.updated = datetime.datetime.utcnow()
        db.session.add(self)
        db.session.commit()


def ResetOrSeedDb(filename, schema, models, no_update=False):
    last = SeedsModel.query.filter_by(name=filename).first()
    if last and no_update:
        return
    elif not last:
        last = SeedsModel(name=filename)
    hasher = hashlib.md5()
    with open(filename, 'rb') as afile:
        buf = afile.read()
        hasher.update(buf)
    needs_update = last.digest != hasher.hexdigest()
    if needs_update:
        print(f'Update is required: {filename}')
        last.digest = hasher.hexdigest()
        last.insert()
        for model in models: model.query.delete()
        db.session.commit()
        with open(filename) as f:
            objs = schema.load(json.load(f))
            for each in objs:
                db.session.add(each)
            db.session.commit()
