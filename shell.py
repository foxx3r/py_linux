#!/usr/bin/env python3
# coding: utf-8
import initially_config.py
import users.py
import commands.py
import directories.py
import colors.py
from time import sleep

status_code = 'running'
current_shell = 'bash'
while status_code != 'exit':
    if current_shell == 'bash' and users.current_user == 'root':
        cli_command = str(input(f'root@{initially_config.hostname}:{directories.current_directory}# '))
    elif current_shell == 'bash' and users.current_user != 'root':
        cli_command = str(input('$ '))
    elif current_shell == 'zsh' and users.current_user == 'root':
        cli_command = str(input(f'{colors.red_font}root{colors.final}:{directories.current_directory} # '))
    elif current_shell == 'zsh' and users.current_user != 'root':
        cli_command = str(input(f'{colors.white_font}{users.current_user}{colors.final}:{directories.current_directory} $ '))

    if cli_command in commands.list_of_commands:
        print(commands.execute_command(cli_command))
    elif cli_command not in commands.list_of_commands:
        print(f'{current_shell}: command not found: {cli_command}')
sleep(1)

