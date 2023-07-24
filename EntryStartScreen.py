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
        
        # Symptoms no.2 Loss of taste
        symptoms_2_label = ttk.Label(self, text="Loss of taste?", font=("Source Sans Pro", 11, "bold"), background="#E3DAFF")
        symptoms_2_label.place(x=80, y=315)

        yes_button_2 = ttk.Radiobutton(self, variable=self.qs2, value=1, text="Yes", style="Custom.TRadiobutton")
        yes_button_2.place(x=280, y=315)

        no_button_2= ttk.Radiobutton(self, variable=self.qs2, value=0, text="No", style="Custom.TRadiobutton")
        no_button_2.place(x=370, y=315)
        
        # Symptoms no.3 Loss of smell
        symptoms_3_label = tk.Label(self, text="Loss of smell?", font=("Source Sans Pro", 11, "bold"), background="#E3DAFF")
        symptoms_3_label.place(x=80, y=345)

        yes_button_3 = ttk.Radiobutton(self, variable=self.qs3, value=1, text="Yes", style="Custom.TRadiobutton")
        yes_button_3.place(x=280, y=345)

        no_button_3 = ttk.Radiobutton(self, variable=self.qs3, value=0, text="No", style="Custom.TRadiobutton")
        no_button_3.place(x=370, y=345)
        
        # Symptoms no. 4 Cough or sore throat
        symptoms_4_label = tk.Label(self, text="Cough or sore throat?", font=("Source Sans Pro", 11, "bold"), background="#E3DAFF")
        symptoms_4_label.place(x=80, y=375)

        yes_button_4 = ttk.Radiobutton(self, variable=self.qs4, value=1, text="Yes", style="Custom.TRadiobutton")
        yes_button_4.place(x=280, y=375)

        no_button_4 = ttk.Radiobutton(self, variable=self.qs4, value=0, text="No", style="Custom.TRadiobutton")
        no_button_4.place(x=370, y=375)
        
        # Symptoms no. 5 Shortness of Breath
        symptoms_5_label = tk.Label(self, text="Shortness of breath?", font=("Source Sans Pro", 11, "bold"), background="#E3DAFF")
        symptoms_5_label.place(x=80, y=405)

        yes_button_5 = ttk.Radiobutton(self, variable=self.qs5, value=1, text="Yes", style="Custom.TRadiobutton")
        yes_button_5.place(x=280, y=405)

        no_button_5 = ttk.Radiobutton(self, variable=self.qs5, value=0, text="No", style="Custom.TRadiobutton")
        no_button_5.place(x=370, y=405)
        
        # Symptoms no.6 Difficulty of breathing
        symptoms_6_label = tk.Label(self, text="Difficulty of breathing", font=("Source Sans Pro", 11, "bold"), background="#E3DAFF")
        symptoms_6_label.place(x=80, y=435)

        yes_button_6 = ttk.Radiobutton(self, variable=self.qs6, value=1, text="Yes", style="Custom.TRadiobutton")
        yes_button_6.place(x=280, y=435)

        no_button_6 = ttk.Radiobutton(self, variable=self.qs6, value=0, text="No", style="Custom.TRadiobutton")
        no_button_6.place(x=370, y=435)
        
        # Symptoms no.7 Nausea or vomiting
        symptoms_7_label = tk.Label(self, text="Nausea or vomiting?", font=("Source Sans Pro", 11, "bold"), background="#E3DAFF")
        symptoms_7_label.place(x=80, y=465)

        yes_button_7 = ttk.Radiobutton(self, variable=self.qs7, value=1, text="Yes", style="Custom.TRadiobutton")
        yes_button_7.place(x=280, y=465)

        no_button_7 = ttk.Radiobutton(self, variable=self.qs7, value=0, text="No", style="Custom.TRadiobutton")
        no_button_7.place(x=370, y=465)