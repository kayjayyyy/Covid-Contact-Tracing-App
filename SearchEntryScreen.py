import tkinter as tk
import csv

class SearchEntry(tk.Tk):
    
    def __init__(self):
        super().__init__()
        
        self.title("Contact Tracing App")
        self.geometry("500x730")
        self.configure(bg="#E3DAFF")