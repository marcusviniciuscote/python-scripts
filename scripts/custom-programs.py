#!/usr/bin/python3

import subprocess
from time import sleep

def terminal_comand(comand):
    '''
    Enter a comand in linux to execute in a terminal
    comand = comand to execute
    '''
    subprocess.call([comand], shell=True)
    sleep(1)

update_and_upgrade = "sudo apt update && sudo apt upgrade -y && sudo apt autoremove"
shutdown = "shutdown -h now"
install_some_programs = "sudo apt install -y neofetch vim neovim virtualbox virtualbox-guest-additions-iso virtualbox-guest-utils eza bat zsh zsh-autosuggestions zsh-syntax-highlighting htop ca-certificates curl wget"

install_nerd_font = "wget -P ~/.local/share/fonts https://github.com/ryanoasis/nerd-fonts/releases/download/v3.0.2/JetBrainsMono.zip && cd ~/.local/share/fonts && unzip JetBrainsMono.zip && rm JetBrainsMono.zip && fc-cache -fv"

docker_down = 'sudo install -m 0755 -d /etc/apt/keyrings && sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc && sudo chmod a+r /etc/apt/keyrings/docker.asc'

docker_dependencies = 'echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null && sudo apt-get update'

install_docker = "sudo apt-get install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin"

docker_post_install = "sudo groupadd docker && sudo usermod -aG docker $USER && newgrp docker"

docker_start_on_boot = "sudo systemctl enable docker.service && sudo systemctl enable containerd.service"

test_docker = "docker run hello-world"

install_zsh = 'sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"'

default_zsh = "chsh -s /usr/bin/zsh"

terminal_comand(update_and_upgrade)
terminal_comand(install_some_programs)
terminal_comand(install_nerd_font)
terminal_comand(docker_down)
terminal_comand(docker_dependencies)
terminal_comand(install_docker)
terminal_comand(docker_post_install)
terminal_comand(docker_start_on_boot)
terminal_comand(test_docker)
terminal_comand(install_zsh)
terminal_comand(default_zsh)
