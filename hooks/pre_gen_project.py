import re
import sys


HINT = "\x1b[3;33m"
INFO = "\x1b[1;33m [INFO]: "
MODULE_REGEX = r'^[_a-zA-Z][_a-zA-Z0-9]+$'
TERMINATOR = "\x1b[0m"
SUCCESS = "\x1b[1;32m [SUCCESS]: "
WARNING = "\x1b[1;33m [WARNING]: "

project_slug = '{{ cookiecutter.project_slug }}'

if not re.match(MODULE_REGEX, project_slug):
	print('ERROR: %s is not a valid Python module name!' % project_slug)

	# exits with status 1 to indicate failure
	sys.exit(1)

assert "\\" not in "{{ cookiecutter.author }}", "Don't include backslashes in author name."

if "{{ cookiecutter.use_docker }}".lower() == "n":
	python_major_version = sys.version_info[0]
	if python_major_version == 2:
		print(
			WARNING + "You're running cookiecutter under Python 2, but the generated "
			"project requires Python 3.11+. Do you want to proceed (y/n)? " + TERMINATOR
			)
