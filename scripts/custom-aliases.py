#!/usr/bin/python3

import subprocess

def terminal_comand(comand):
    '''
    Enter a comand in linux to execute in a terminal
    comand = comand to execute
    '''
    subprocess.call([comand], shell=True)

def aliases_comand(alias, comand):
    '''
    Add a alias in aliases.zsh
    alias = name of the alias
    comand = comand to execute
    '''
    ac = f'alias {alias}="{comand}"'
    path = '~/.oh-my-zsh/custom/aliases.zsh'
    aliases = 'echo '+'\'alias '+alias+'="'+comand+'"'+'\' >> '+path
    terminal_comand(aliases)

update_and_upgrade = "sudo apt update && sudo apt upgrade -y && sudo apt autoremove"
shutdown = "shutdown -h now"

aliases_comand('ls', 'eza --icons')
aliases_comand('ll', 'eza --icons -la')
aliases_comand('cat', 'batcat')
aliases_comand('atualiza', update_and_upgrade)
aliases_comand('desliga', shutdown)
