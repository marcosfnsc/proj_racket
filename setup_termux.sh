#!/bin/env bash

set -o errexit

pkg install -y \
  git \
  python \
  python-pip \
  termux-api

git clone https://github.com/marcosfnsc/proj_racket.git

# create venv for python
cd proj_racket
python -m venv proj_racket_venv
source proj_racket_venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
deactvate

echo "configuração concluida!"
