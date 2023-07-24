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
        
        # Age label and entry box
        age_label = tk.Label(self, text="Age", bg="#E3DAFF")
        age_label.place(x=108, y=110)

        self.age_entry = tk.Entry(self, width=45)
        self.age_entry.place(x=150, y=110)
        
        # Phone number label and entry box
        phone_number_label = tk.Label(self, text="Phone Number", bg="#E3DAFF")
        phone_number_label.place(x=50, y=140)

        self.phone_number_entry = tk.Entry(self, width=45)
        self.phone_number_entry.place(x=150, y=140)
        
        # Email label and entry box
        email_label = tk.Label(self, text="Email", bg="#E3DAFF")
        email_label.place(x=100, y=170)

        self.email_entry = tk.Entry(self, width=45)  
        self.email_entry.place(x=150, y=170)

        # Adress label and entry box
        address_label = tk.Label(self, text="Address", bg="#E3DAFF")
        address_label.place(x=88, y=200)

        self.address_entry = tk.Entry(self, width=45) 
        self.address_entry.place(x=150, y=200)
        
        # Main question for symptoms
        questions = tk.Label(self, text="Do you experience any of the following in the last 14 days?", font=("Source Sans Pro", 12, "bold"), bg="#E3DAFF")
        questions.place(x=26, y=250)
        
        # Yes and No Radiobutton
        self.qs1 = tk.IntVar(value="")
        self.qs2 = tk.IntVar(value="")
        self.qs3 = tk.IntVar(value="")
        self.qs4 = tk.IntVar(value="")
        self.qs5 = tk.IntVar(value="")
        self.qs6 = tk.IntVar(value="")
        self.qs7 = tk.IntVar(value="")
        self.qs8 = tk.IntVar(value="")
        self.qs9 = tk.IntVar(value="")
        self.qs10 = tk.IntVar(value="")

        style = ttk.Style()
        style.configure("Custom.TRadiobutton", background="#E3DAFF", fg="black", font=("Source Sans Pro", 9))
        
        # Symptoms no.1 Fever
        symptoms_1_label = tk.Label(self, text="Fever or chills?", font=("Source Sans Pro", 11, "bold"), background="#E3DAFF")
        symptoms_1_label.place(x=80, y=285)

        yes_button_1 = ttk.Radiobutton(self, variable=self.qs1, value=1, text="Yes", style="Custom.TRadiobutton")
        yes_button_1.place(x=280, y=285)

        no_button_1 = ttk.Radiobutton(self, variable=self.qs1, value=0, text="No", style="Custom.TRadiobutton")
        no_button_1.place(x=370, y=285)