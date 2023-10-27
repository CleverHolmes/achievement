import subprocess
import os
import random
from dotenv import load_dotenv
from time import sleep
import string

load_dotenv()

num = os.environ.get("repo_count")
period = os.environ.get("period")

for i in range(int(num)):
    repo_name = ''.join(random.choice(string.ascii_lowercase) for _ in range(12))

    subprocess.run(['gh', 'repo', 'create', repo_name, '--private'])
    print(repo_name)

    sleep(int(period))
