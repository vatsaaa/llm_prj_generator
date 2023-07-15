import os
import subprocess


TERMINATOR = "\x1b[0m"
WARNING = "\x1b[1;33m [WARNING]: "
INFO = "\x1b[1;33m [INFO]: "
HINT = "\x1b[3;33m"
SUCCESS = "\x1b[1;32m [SUCCESS]: "

REMOVE_PATHS = [
    '{% if cookiecutter.project_packaging != "pip" %} requirements.txt {% endif %}',
    '{% if cookiecutter.project_packaging != "poetry" %} poetry.lock {% endif %}',
]

for path in REMOVE_PATHS:
    path = path.strip()
    if path and os.path.exists(path):
        if os.path.isdir(path):
            os.rmdir(path)
        else:
            os.unlink(path)

cmd1="python3 -m venv .venv"
subprocess.run(cmd1, shell=True)

if "{{ cookiecutter.use_docker }}".lower() == "no":
    files = ["Dockerfile", ".dockerignore"]
    for file in files:
        os.remove(file)

if "{{ cookiecutter.open_source_license }}".lower() == "not open source":
    files = ["LICENSE.md"]
    for file in files:
        os.remove(file)

if "{{ cookiecutter.project_packaging }}" == "environment":
    os.remove(".env")

print(SUCCESS + "Project boilerplate initialized, let us get going!" + TERMINATOR)
