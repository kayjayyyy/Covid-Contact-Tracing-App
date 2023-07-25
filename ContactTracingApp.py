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
        
        title = tk.Label(self, text="Covid-19 Contact Tracing App", font=("Source Sans Pro", 20, "bold"), bg="#E3DAFF")
        title.place(x=48, y=150)
        
        # Instruction
        instruction = tk.Label(self, text="If you are either diagnosed with Coronavirus or experiencing", font=("Source Sans Pro", 11), background="#E3DAFF")
        instruction.place(x=53, y=250)
        
        instruction = tk.Label(self, text="Coronavirus symptoms, please provide us with your contact information.", font=("Source Sans Pro", 11), background="#E3DAFF")
        instruction.place(x=18, y=270)
        
        instruction_2 = tk.Label(self, text="And you can also check here any interactions a person may have", font=("Source Sans Pro", 11), background="#E3DAFF")
        instruction_2.place(x=40, y=290)
        
        instruction_2 = tk.Label(self, text="had with somebody who might be a COVID-19 virus carrier.", font=("Source Sans Pro", 11), background="#E3DAFF")
        instruction_2.place(x=53, y=310)
        