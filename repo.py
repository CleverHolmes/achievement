import subprocess
import random
from time import sleep
import string

num = input("How many repositories do you want: ")
period = input("Choose the duration(as seconds): ")

for i in range(int(num)):
    repo_name = ''.join(random.choice(string.ascii_lowercase) for _ in range(12))

    subprocess.run(['gh', 'repo', 'create', repo_name, '--private'])

    sleep(int(period))
