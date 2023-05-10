#!/bin/env python

import json
import os
import shlex
import socket
import subprocess
import asyncio

import websockets
from websockets.server import serve

# ============== codes for termux =================
# =================================================

SENSOR_NAME='gyroscope'

class Shell():
    def __init__(self, command: str) -> None:
        self._subprocess_object = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE)

    def readline(self) -> str:
        return self._subprocess_object.stdout.readline().decode('utf-8')

def get_length_line_output(shell: Shell) -> int:
    '''descobrir quantas linhas precisa ler pra obter cada saida completa'''
    length_json_output = 1
    json_data = ''

    while True:
        json_data += shell.readline()
        try:
            json.loads(json_data)
        except:
            length_json_output += 1
        else:
            return length_json_output

def get_data_output(shell: Shell, output_length: int) -> dict:
    data_output = ''
    for _ in range(output_length):
        data_output += shell.readline()

    return json.loads(data_output)


# ================= main code =================
# =============================================

if __name__ == '__main__':
    command_output = Shell(f'termux-sensor -s {SENSOR_NAME} -d 50')
    output_length = get_length_line_output(command_output)

    async def handler(websocket, path):
        while True:
            data_output = get_data_output(command_output, output_length)
            key = list(data_output.keys())[0]

            eixo_x = data_output[key]['values'][0]
            eixo_y = data_output[key]['values'][1]
            eixo_z = data_output[key]['values'][2]
            message = f'{eixo_x}|{eixo_y}|{eixo_z}'
            await websocket.send(message)

    start_server = serve(handler,  port=8000)
    asyncio.get_event_loop().run_until_complete(start_server)
    try:
        asyncio.get_event_loop().run_forever()
    except:
        # cleanup sensor
        os.system('termux-sensor -c')
