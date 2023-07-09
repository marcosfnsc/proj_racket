#!/bin/env python

import os
import shlex
import subprocess
import asyncio
import websockets

# ============== codes for termux =================
# =================================================


class Shell():
    def __init__(self, command: str) -> None:
        self._subprocess_object = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE)

    def readline(self) -> str:
        return self._subprocess_object.stdout.readline().decode('utf-8')

# ================= main code =================
# =============================================


if __name__ == '__main__':
    SENSORS = 'accel,gyro'
    shell = Shell(f'termux-sensor -s {SENSORS} -d 50')

    async def handler(websocket):
        while True:
            data_output = shell.readline()
            await websocket.send(data_output)

    async def main():
        async with websockets.serve(handler, port=8000):
            await asyncio.Future()
    try:
        asyncio.run(main())
    except:
        # cleanup sensor
        os.system('termux-sensor -c')
