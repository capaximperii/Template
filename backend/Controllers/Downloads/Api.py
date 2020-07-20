import os
import shutil
from urllib.parse import unquote_plus
from flask import Blueprint, request
from flask_restful import Resource, Api
from flask import Response
from werkzeug.wsgi import wrap_file

def cure_path(p):
    p = p.replace('\\', '/')
    p = p.replace('..', '.')
    p = p.replace(' ', '')
    p = p[1:] if p.startswith('/') else p # make paths starting with / relative
    base = os.path.join(os.getcwd(), 'Workspace', p)
    return base

class DownloadsListController(Resource):
    def get(self, name=None):
        path =  cure_path(request.args.get('path', '.'))
        files =  os.listdir(path)
        base =  os.getcwd() + '/Workspace'
        results = [
            {'name': '..', 'path': base, 'type': 'dir' }
        ]
        for f in files:
            current = { }
            current['name'] = f
            abspath = os.path.join(path, f)
            current['path'] = os.path.dirname(abspath.replace(base, ''))
            if os.path.isdir( abspath ):
                current['type'] = 'dir'
            else:
                ext = f.split('.')
                ext = ext[-1] if len(ext) > 1 else 'file'
                current['type'] = ext
            results.append(current)
        return results

class DownloadsController(Resource):
    def get(self, fname):
        path = os.path.join(cure_path(request.args.get('path', '.')), fname)
        file_name = os.path.basename(path)
        file_size = os.path.getsize(path)
        fh = wrap_file(request.environ, open(path, 'rb'))
        return Response(fh,
            mimetype='application/octet-stream',
            headers=[
                ('Content-Length', str(file_size)),
                ('Content-Disposition', "attachment; filename=\"%s\"" % file_name),
            ],
            direct_passthrough=True)

    def delete(self, fname):
        fname = unquote_plus(unquote_plus(fname))
        path = cure_path(fname)
        print(path)
        file_name = os.path.abspath(path)
        print(file_name)
        os.remove(file_name)
        return {'path': path, 'file_name': file_name}

DownloadsApi = Blueprint('Downloads', __name__, url_prefix='/api/downloads')
__api = Api(DownloadsApi)
__api.add_resource(DownloadsListController, '')
__api.add_resource(DownloadsController, '/<fname>')
