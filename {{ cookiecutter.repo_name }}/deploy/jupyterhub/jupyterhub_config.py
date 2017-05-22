c.Application.log_level = 'DEBUG'

c.DockerSpawner.volumes = {
    '/srv/{{cookiecutter.repo_name}}/data':'/srv/{{cookiecutter.repo_name}}/data',
    '/home/{username}': '/home/{username}',
    '/home/{username}/drtools': '/home/ubuntu/drtools',
    '/srv/{{cookiecutter.repo_name}}/tmp':'/tmp'
}

c.JupyterHub.admin_access = True

c.JupyterHub.admin_users = set(['kayibal'])

from jupyter_client.localinterfaces import public_ips
c.JupyterHub.hub_ip = public_ips()[0]

c.JupyterHub.spawner_class = 'dockerspawner_usermap.DockerUsermapSpawner'
c.DockerUsermapSpawner.container_image = 'drtools/{{cookiecutter.repo_name}}-worker:jupyter'
c.DockerUsermapSpawner.group_name = 'developer'
c.DockerUsermapSpawner.settings_module = \
    '{{cookiecutter.repo_name}}.settings.dev'