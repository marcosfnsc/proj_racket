#!/bin/env bash

set -o errexit

pkg up
pkg install git iprout2 nodejs python python-pip termux-api

git clone --depth 1 https://github.com/marcosfnsc/proj_racket.git

# create venv for python
cd proj_racket
python -m venv proj_racket_venv
source proj_racket_venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
deactvate

# install depedencies of npm
cd racket_ui && npm install

echo "configuração concluida!"
