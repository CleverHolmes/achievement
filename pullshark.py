import subprocess
from time import sleep

name = input("Input your github user name: ")
email = input("Input your github user email: ")
repo = input("Input your github repository name: ")
num = input("Input the numbers of pull request: ")


subprocess.run(['git', 'config', '--local', 'user.name', name])
subprocess.run(['git', 'config', '--local', 'user.email', email])
subprocess.run(['git', 'remote', 'set-url', 'origin', f'https://github.com/CleverHolmes/{repo}.git'])

try:
    subprocess.check_output(['gh', 'repo', 'view', f'{name}/{repo}'])
except subprocess.CalledProcessError:
    subprocess.run(['gh', 'repo', 'create', repo, '--public'])
    subprocess.run(['git', 'checkout', '-B', 'master'])
    subprocess.run(['git', 'add', '.'])
    subprocess.run(['git', 'commit', '-m', "init"])
    subprocess.run(['git', 'push', '-u', 'origin', 'master'])

for i in range(int(num)):
    subprocess.run(['git', 'checkout', '-B', 'new-branch'])
    subprocess.run(['git', 'add', '.'])
    subprocess.run(['git', 'commit', '--allow-empty', '-m', "New commit message"])
    subprocess.run(['git', 'push', '-u', 'origin', 'new-branch'])
    subprocess.run(['gh', 'pr', 'create', '-f'])
    subprocess.run(['gh', 'pr', 'merge', '--merge', '--delete-branch'])
    sleep(50)