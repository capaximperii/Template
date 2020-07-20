import os
import sys
import subprocess
import atexit
from Workers.WorkerRef import executor
sys.path.append(os.getcwd())

def initialize(appl):
    os.makedirs('./Data/broker/out', exist_ok=True)
    os.makedirs('./Data/broker/processed', exist_ok=True)
    os.makedirs('./Data/broker/results', exist_ok=True)
    executor.init_app(appl)
    # if 'celery worker' not in ' '.join(sys.argv):
    proc = subprocess.Popen(['celery', 'worker', '--app=Workers:executor', '--concurrency=1', '--loglevel=INFO'])
    atexit.register(proc.kill)

__all__ = ['initialize', 'executor']