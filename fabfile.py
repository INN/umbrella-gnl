from tools.fablib import *

from fabric.api import task

"""
Getting set up for the first time and using vim?
Run:
    :%s/gnl/project_name/g       # name for the project, used as the database name. This should match the umbrella repository name and the domain.wpengine.com name
    :%s/GNL/YOUR_SITE_ENV_VAR/g      # environment variable slug from INN's secrets repository
"""

"""
Base configuration
"""
env.project_name = 'gnl'
env.hosts = ['localhost', ]
env.sftp_deploy = True # needed for wpengine
env.domain = 'gnl.dev'

"""
Add HipChat info to send a message to a room when new code has been deployed.
"""
env.hipchat_token = ''
env.hipchat_room_id = ''


# Environments
@task
def production():
    """
    Work on production environment
    """
    env.settings    = 'production'
    env.hosts       = [ os.environ[ 'GNL_PRODUCTION_SFTP_HOST' ], ]   # ssh host for production.
    env.user        = os.environ[ 'GNL_PRODUCTION_SFTP_USER' ]        # ssh user for production.
    env.password    = os.environ[ 'GNL_PRODUCTION_SFTP_PASSWORD' ]    # ssh password for production.
    env.domain      = 'gnl.wpengine.com'
    env.port        = '2222'


@task
def staging():
    """TKTKNAME
    Work on staging environment
    """
    env.settings    = 'staging'
    env.hosts       = [ os.environ[ 'GNL_STAGING_SFTP_HOST' ], ]   # ssh host for production.
    env.user        = os.environ[ 'GNL_STAGING_SFTP_USER' ],       # ssh user for production.
    env.password    = os.environ[ 'GNL_STAGING_SFTP_PASSWORD' ]    # ssh password for production.
    env.domain      = 'gnl.staging.wpengine.com'
    env.port        = '2222'

try:
    from local_fabfile import  *
except ImportError:
    pass
