from celery import Celery
from celery.loaders.app import AppLoader
from Models import JobsSchema

class QueuedExecutor(Celery):
    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.loader_cls = 'celery.loaders.app:AppLoader'
        self.conf.update({
            'broker_url': 'filesystem://',
            'broker_transport_options': {
                'data_folder_in': './Data/broker/out',
                'data_folder_out': './Data/broker/out',
                'data_folder_processed': './Data/broker/processed'
            },
            'imports': ('Workers.StmWorker',),
            'result_persistent': False,
            'task_serializer': 'json',
            'result_serializer': 'json',
            'accept_content': ['json', 'application/json']
        })

    def init_app(self, appl):
        self.conf.update(appl.config)

    def submit(self, job, token):
        schema = JobsSchema(many=False)
        job_json = schema.dump(job)
        self.send_task('do_stm_processing', (job_json, token))

executor = QueuedExecutor('stmworker')
