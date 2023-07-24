# Templanza, Kristine Joy F.
# BSCPE 1-4
# Final Project - Covid Contact Tracing App

import tkinter as tk
from EntryStartScreen import StartScreen

class MainScreen(tk.Tk):
    
    def __init__(self):
        super().__init__()

        self.title("Contact Tracing App")
        self.geometry("500x780")
        self.configure(bg="#E3DAFF")
        self.pack_propagate(0)