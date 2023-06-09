#!/bin/env python

import json
import os
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

    print(Shell('bash scripts/update_ip_address.sh').readline())
    run_site = Shell('cd racket_ui && npm run dev -- --port 5173 --host')

    termux_shell = Shell(f'termux-sensor -s {SENSORS} -d 50')

    @sock.route('/')
    def echo(sock):
        data_output = ''
        while True:
            try:
                data_output += termux_shell.readline()
                dict_data = json.loads(data_output)
                sock.send(json.dumps(dict_data))
                data_output = ''
            except:
                continue

    app.run(host='0.0.0.0', port=8000)
    print(Shell('bash scripts/restore_ip_address.sh').readline())
    os.system('termux-sensor -c') # cleanup sensor
