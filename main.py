#!/usr/bin/env python3
import asyncio
import os.path
import platform
import shlex
import sys

from nicegui import ui

async def run_command(input) -> None:
    process = await asyncio.create_subprocess_exec(
        *shlex.split(sys.executable+input, posix="win" not in sys.platform.lower()),
        stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.STDOUT,
        cwd=os.path.dirname(os.path.abspath(__file__))
    )

ui.button('FIND', on_click=lambda: run_command(' slow.py')).props('no-caps')

# NOTE: On Windows reload must be disabled to make asyncio.create_subprocess_exec work (see https://github.com/zauberzeug/nicegui/issues/486)
ui.run(reload=platform.system() != 'Windows')
