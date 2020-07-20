from flask import Blueprint, request
from flask_restful import Resource
from Models import UsersModel, JobsModel, JobsSchema, JobsPaginatedSchema
from flask_login import current_user, login_required
from sqlalchemy import or_
from sqlalchemy.sql import text
from Controllers.ApiRef import RootApi
from Workers import executor

class JobsListController(Resource):
    def get(self):
        params = dict(request.args)
        page = int(params.pop('page', 1))
        per_page = int(params.pop('itemsPerPage', 10))
        search = f'%{params.pop("query", "")}%'
        column = params.pop('column', 'id')
        if column in ['id', 'created', 'updated']: column = f'Jobs.{column}'
        order = params.pop('order', 'desc')
        jobs = JobsModel.join(UsersModel).query.filter(
                or_(
                    JobsModel.status.ilike(search),
                    JobsModel.job_title.ilike(search),
                    UsersModel.name.ilike(search),
                    UsersModel.email.ilike(search),
                    UsersModel.department.ilike(search)
                )
            ).order_by(text(f'{column} {order}')) \
            .paginate(page=page, per_page=per_page)
        schema = JobsPaginatedSchema(many=False)
        return schema.dump(jobs)

    @login_required
    def post(self):
        schema = JobsSchema(many=False)
        job = schema.load(request.json)
        job.user_id = current_user.id
        job.insert()
        token = request.headers.get('Authorization')
        executor.submit(job, token)
        return schema.dump(job), 202

class JobsController(Resource):
    @login_required
    def put(self, id):
        schema = JobsSchema(many=False)
        job = schema.load(request.json)
        job.update()
        return schema.dump(job), 200

JobsApi = Blueprint('Jobs', __name__, url_prefix='/api/jobs')
__api = RootApi(JobsApi)
__api.add_resource(JobsListController, '')
__api.add_resource(JobsController, '/<int:id>')
