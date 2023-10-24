import subprocess
import os
from dotenv import load_dotenv

load_dotenv()

name = os.environ.get("name")
email = os.environ.get("email")

subprocess.run(['git', 'config', '--local', 'user.name', name])
subprocess.run(['git', 'config', '--local', 'user.email', email])

subprocess.run(['git', 'checkout', '-B', 'new-branch'])
subprocess.run(['git', 'pull', 'origin', 'new-branch'])
subprocess.run(['git', 'add', '.'])
subprocess.run(['git', 'commit', '--allow-empty', '-m' "New commit message"])
subprocess.run(['git', 'push', '-u', 'origin', 'new-branch'])
subprocess.run(['gh', 'pr', 'create', '-f'])
subprocess.run(['gh', 'pr', 'merge', '--merge', '--delete-branch'])
# sleep 40
