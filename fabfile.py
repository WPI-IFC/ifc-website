import os

from fabric import Connection
from invoke import task

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DEV_PKEY_PATH = os.path.join(BASE_DIR, '.vagrant/machines/default/virtualbox/private_key')

@task
def deploy(cntx, prod=False):
    if prod:
        con = None
        print("Running production deploy")
    else:
        con = Connection('localhost', 'vagrant', 2222, connect_kwargs={"key_filename": DEV_PKEY_PATH})
        with con.cd('/vagrant'):
            con.run('ls -l')