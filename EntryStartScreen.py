# Templanza, Kristine Joy F.
# BSCPE 1-4
# Final Project - Covid Contact Tracing App

import tkinter as tk
from tkinter import messagebox, ttk
import csv

class StartScreen(tk.Tk):

    def init(self):
        super().__init__()

        self.title("Covid Contact Tracing")
        self.geometry("500x800")
        self.configure(bg="#E3DAFF")

        title = tk.Label(self, text="COVID CONTACT TRACING FORM", font=("Source Sans Pro", 15, "bold"), bg="#E4CCB4")
        title.place(x=83, y=20)
        
        # Name label and entry box
        full_name_label = tk.Label(self, text="Full Name", bg="#E3DAFF")
        full_name_label.place(x=78, y=80)

        self.full_name_entry = tk.Entry(self, width=45)
        self.full_name_entry.place(x=150, y=80)
        
        # Age label and entry
        age_label = tk.Label(self, text="Age", bg="#E3DAFF")
        age_label.place(x=108, y=110)

        self.age_entry = tk.Entry(self, width=45)
        self.age_entry.place(x=150, y=110)