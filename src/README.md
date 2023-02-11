# Setup guide

Install python

Create virtual enviroment to separate libraries:
`python -m venv env`

Activate venv:
- Windows
`source env/bin/activate.ps1`
- Linux
`source env/bin/activate`

To exit venv if you stop working on project:
`deactivate`

Load libraries:
`pip install -r requirements.txt`

Add library to requirements.txt after installation:
`pip freeze > requirements.txt`
