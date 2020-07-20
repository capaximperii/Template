import requests
from Library.Client.Web.WebRef import Modelify

def create(payload, token, host='localhost', port=8888):
    headers = {'Authorization': token}
    job = requests.post(f'http://{host}:{port}/api/jobs', json=payload, verify=False, headers=headers)
    return Modelify(job.json())

def update(id, payload, token, host='localhost', port=8888):
    headers = {'Authorization': token}
    job = requests.put(f'http://{host}:{port}/api/jobs/{id}', json=payload, verify=False, headers=headers)
    return Modelify(job.json())

def get_all(host='localhost', port=8888):
    job = Modelify(requests.get(f'http://{host}:{port}/api/jobs?itemsPerPage=1000000', verify=False).json())
    return job['items'] # Because jobs is paginated item.
