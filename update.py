import subprocess
import random
from time import sleep
import string

result = subprocess.run(
        ["gh", "repo", "list", "--limit", "1000"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        check=True
    )

repo_lines = [line.split()[0] for line in result.stdout.splitlines()]

prefix = "https://github.com/"

with open("list", "w") as file:
    for repo in repo_lines:
        line = prefix + repo
        file.write(line + '\n')