import os
import sys
import git
import psutil
from subprocess import Popen
from flask import Blueprint, request
from flask_restful import Resource
from Controllers.ApiRef import RootApi


class HealthController(Resource):
    def __init__(self):
        repo = git.Repo('..')
        for remote in repo.remotes:
            remote.fetch()
        self.version = next((tag.name for tag in repo.tags if tag.commit == repo.head.commit), 'Development')

    def get(self):
        current_process = psutil.Process(os.getpid())
        mempc = current_process.memory_percent()
        for child in current_process.children(recursive=True):
            mempc += child.memory_percent()
        cpu = psutil.cpu_percent()
        net = len(psutil.net_connections())
        vm = psutil.virtual_memory()
        memtotal = int(100 - vm.percent)
        return dict(cpu=cpu, mempc=mempc, net=net, memtotal=memtotal, version=self.version)

    def put(self):
        """ Updates the remote refs  """
        repo = git.Repo('..')
        for remote in repo.remotes:
            remote.fetch()
        version = next((tag.name for tag in repo.tags if tag.commit == repo.head.commit), 'Development')
        tags = sorted(repo.tags, key=lambda t: t.name)
        tags = list(map(lambda x: x.name, tags))
        result = {
            'version': version,
            'releases': tags
        }
        return result

    def post(self):
        body = request.get_json()
        version = body.get('version', None)
        print(version)
        if version:
            repo = git.Git('..')
            changed = len(repo.diff()) > 0
            if changed: repo.stash() # Local configs stash
            repo.checkout('master') # Go to head
            repo.pull()
            repo.checkout(version)
            if changed: repo.stash('pop') # Local configs stash pop
            # Rebuild ui, restart server for changes to take effect
            Popen(['pip', 'install', '-r', 'requirements.txt'], shell=True)
            spawn = Popen(['npm', 'run', 'build'], cwd='../frontend', shell=True)
            spawn.wait()
            os._exit(0) # shut down immediately, ui gets no response.
        return { 'message': 'Upgrade Failed' }, 400


HealthApi = Blueprint('Health', __name__, url_prefix='/api/health')
__api = RootApi(HealthApi)
__api.add_resource(HealthController, '')
