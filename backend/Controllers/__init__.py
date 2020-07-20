import os
from Controllers.Downloads import DownloadsApi
from Controllers.Users import UsersApi
from Controllers.Jobs import JobsApi
from Controllers.Health import HealthApi
from Controllers.Cli import CommandsCli
from flask import send_file

# When routes dont match to anything, send index.html
def not_found_error(error):
    return send_file('./Ui/index.html')


def initialize(appl):
    # Register web api handlers
    os.makedirs('./Workspace', exist_ok=True)
    appl.register_blueprint(DownloadsApi)
    appl.register_blueprint(UsersApi)
    appl.register_blueprint(JobsApi)
    appl.register_blueprint(HealthApi)
    appl.register_blueprint(CommandsCli)
    appl.register_error_handler(404, not_found_error)
