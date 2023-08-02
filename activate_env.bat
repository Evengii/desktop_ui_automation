@echo off

python -m pip install --upgrade pip
python -m pip install pipenv
pipenv sync
pipenv shell

cmd /k
