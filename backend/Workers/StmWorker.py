import random
import time
from Workers.WorkerRef import executor
from Library.Client.Web import Jobs

@executor.task(bind=True, name='do_stm_processing')
def do_stm_processing(taskref, job_spec, token):
    time.sleep(30)
    result = random.randint(0, 10) % 2 == 0
    job_spec['status'] = 'PASSED' if result is True else 'FAILED'
    Jobs.update(job_spec['id'], job_spec, token)
    return job_spec['status']
