#!/bin/env bash

import os
import json
import shlex
import subprocess

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

if __name__ == '__main__':
    command_output = Shell(f'termux-sensor -s {SENSOR_NAME}')
    output_length = get_length_line_output(command_output)

    while True:
        data_output = get_data_output(command_output, output_length)
        key = list(data_output.keys())[0]

        eixo_x = data_output[key]['values'][0]
        eixo_y = data_output[key]['values'][1]
        eixo_z = data_output[key]['values'][2]
        break

    # cleanup sensor
    os.system('termux-sensor -c')
