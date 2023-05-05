#!/bin/env bash

import subprocess
import shlex
import time

SENSOR_NAME='gyroscope'

command_output = subprocess.Popen(shlex.split(f'termux-sensor -s {SENSOR_NAME}'), stdout=subprocess.PIPE)
for _ in range(3):
    print(command_output.stdout.readline().decode('utf-8'), end='')
    time.sleep(3)
