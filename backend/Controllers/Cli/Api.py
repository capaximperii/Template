import csv
import click
from zipfile import ZipFile
from flask import Blueprint
import pandas as pd
from io import StringIO
from Library.Client import Jobs
# https://stackoverflow.com/a/58276955

CommandsCli = Blueprint('cli', __name__)

@CommandsCli.cli.command('Backup')
@click.argument('file')
def backup(file):
    """ flask cli Backup backup.zip"""
    with ZipFile(file, 'w') as backup:
        jobs = Jobs.get_all()
        df = pd.DataFrame(jobs)
        buf = StringIO()
        df.to_csv(buf, encoding='utf-8', index=False)
        buf.seek(0)
        with backup.open('jobs.csv', 'w') as bk:
            bk.write(buf.read().encode('utf-8'))
        print(f'Backed up Jobs to archive: {file}')

@CommandsCli.cli.command('Restore')
@click.argument('file')
def restore(file):
    """ flask cli Restore backup.zip"""
    with ZipFile(file) as backup:
        with backup.open('jobs.csv') as jobbk:
            df = pd.read_csv(jobbk)
            objects = df.to_dict('records')
            for payload in objects:
                Jobs.create(payload, token=None)  # Wont update because token is none
        print(f'Restored Jobs from archive: {file}')


