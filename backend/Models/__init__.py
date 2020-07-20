import os
import sys
import json
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from Models.DbRef import db, ma
from Models.UsersModel import UsersModel, UsersSchema
from Models.JobsModel import JobsModel, JobsSchema, JobsPaginatedSchema
from Models.FactsModel import ProductsModel, ProductsSchema
from Models.SeedsModel import ResetOrSeedDb

def initialize(appl):
    os.makedirs('./Data', exist_ok=True)
    db.init_app(appl)
    ma.init_app(appl)
    Migrate(appl, db, directory=os.path.join(os.getcwd(), 'Models', 'Migrations'), version_table='Versions')
    manager = Manager(appl)
    manager.add_command('db', MigrateCommand)
    if 'flask db' in ' '.join(sys.argv): return
    with appl.app_context():
        db.create_all()
        ResetOrSeedDb('Models/Seed/Products.json', ProductsSchema(many=True), [ ProductsModel ])
        # Abort all running and Queued tasks.
        # https://stackoverflow.com/questions/49794899/why-is-my-flask-sqlalchemy-delete-query-failing
        JobsModel.query.filter(JobsModel.status.in_(['QUEUED','RUNNING'])) \
            .update(dict(status='ABORTED', detail='Server was rebooted'), synchronize_session=False)
        db.session.commit()

__all__ = ['initialize', 'JobsModel', 'JobsSchema', 'UsersModel', 'UsersSchema']

