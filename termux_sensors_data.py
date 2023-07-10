#!/bin/env python

import os
import shlex
import subprocess

from flask import Flask
from flask_sock import Sock

# ============== codes for termux =================
# =================================================


class Shell():
    def __init__(self, command: str) -> None:
        self._subprocess_object = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)

    def readline(self) -> str:
        return self._subprocess_object.stdout.readline().decode('utf-8')

# ================= main code =================
# =============================================


if __name__ == '__main__':
    app = Flask(__name__)
    sock = Sock(app)

    SENSORS = 'accel,gyro'
    #shell = Shell(f'termux-sensor -s {SENSORS} -d 50')
    run_site = Shell('cd racket_ui && npm run dev')

    @sock.route('/')
    def echo(sock):
        while True:
            #data_output = shell.readline()
            data_output = 'casa'
            sock.send(data_output)

    app.run(port=8000)
    os.system('termux-sensor -c') # cleanup sensor
