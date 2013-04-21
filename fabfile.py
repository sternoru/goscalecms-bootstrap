import os
from fabric.api import *


# === Utility functions ===
def _get_project_dir():
    project_dir = '{{ project_name }}'
    if '{' in project_dir:
        for file in os.listdir(os.curdir):
            if '.' not in file:
                return file
    return project_dir


def _get_settings(module='settings'):
    settings_module = '%s.%s' % (_get_project_dir(), module)
    print 'Using settings:', settings_module
    return settings_module


# === Environments ===
def dev():
    env.env = 'dev'
    env.settings = _get_settings('dev_settings')


# def staging():
#     env.env = 'staging'
#     env.settings = '{{ project_name }}.settings.staging'
#     env.remote = ''
#     env.heroku_app = ''
#
#
# def production():
#     env.env = 'production'
#     env.settings = '{{ project_name }}.settings.production'
#     env.remote = ''
#     env.heroku_app = ''


# Default Environment
dev()


# === Utils ===
def manage(command='help'):
    man = 'python manage.py %s --settings={settings}' % command
    local(man.format(**env))


# === Static assets stuff ===
def collectstatic():
    # brunchbuild()
    local('python manage.py collectstatic --noinput --settings={settings}'.format(**env))


# === DB ===
def resetdb(create_admin=False):
    if env.env == 'dev':
        with settings(warn_only=True):
            local('rm -f dev.db')
        local('python manage.py syncdb --settings={settings} --noinput --all'.format(**env))
        local('python manage.py migrate --settings={settings} --fake'.format(**env))
    else:
        # Your production code here
        pass
    loaddata()
    if create_admin:
        local('python manage.py createsuperuser --settings={settings}'.format(**env))
    manage('goscale update_posts')


def schemamigration(app_names='core'):
    local('python manage.py schemamigration {app_names} --auto --settings={settings}'.format(app_names, **env))


def migrate():
    if env.env == 'dev':
        local('python manage.py migrate --settings={settings}'.format(**env))
    else:
        # Your production code here
        pass


def updatedb(app_names=None):
    if app_names:
        schemamigration(app_names)
    else:
        schemamigration()
    migrate()


def dumpdata():
    manage('goscale dump')


def loaddata():
    manage('goscale load')


# === Bootstrap the environment ===
def bootstrap(create_admin=False, virtualenv=None):
    if virtualenv:
        local('mkvirtualenv %s' % 'goscale' if type(virtualenv) is bool else virtualenv)
    local('pip install -r requirements.txt')
    resetdb(create_admin)
    collectstatic()
    print 'Project is ready, execute "fab run" to run the server.'


# === Routine tasks ===
def run():
    local('python manage.py runserver --settings=%s' % env.settings)