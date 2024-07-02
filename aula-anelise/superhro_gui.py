import json
import o
import sys
import tkinter as tk
from ktinter import tkinter import ttk
import logging

logging.basicConfig(filename='superhero_gui.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s:%(message)s')

def resource_path(relative_path):
    """ Get absolute path to resouce, works for dev and for PyIstaller"""
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
        