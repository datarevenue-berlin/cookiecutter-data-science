from subprocess import check_output, CalledProcessError


def run_cmd(cmd, raise_=False):
    try:
        cmd = cmd.split(' ') if isinstance(cmd, str) else cmd
        check_output(cmd)
    except CalledProcessError as e:
        if raise_:
            raise


run_cmd('git init', True)
print('Git repository initialized.')

run_cmd('versioneer install')
print('Setting up versioneer.')

run_cmd('git add *')
run_cmd(['git', 'commit', '-m', 'Initial commit from project template.'])
run_cmd('git tag v0.0.0')
print('Created initial commit and tagged as v0.0.0')

run_cmd('git remote add origin remote '
        'git@github.com:/datarevenue-berlin/{{cookiecutter.repo_name}}')
print('Added remote origin: '
      'git@github.com:/datarevenue-berlin/{{cookiecutter.repo_name}}')
print('Use:\n'
      'git push -u origin master\n'
      'to create github repository')
