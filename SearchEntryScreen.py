import tkinter as tk
import csv

class SearchEntry(tk.Tk):
    
    def __init__(self):
        super().__init__()
        
        self.title("Contact Tracing App")
        self.geometry("500x730")
        self.configure(bg="#E3DAFF")
        
        # Title
        title = tk.Label(self, text="COVID CONTACT TRACING", font=("Source Sans Pro", 15, "bold"), bg="#E4CCB4")
        title.place(x=118, y=50)
        
        # Instruction
        instruction_2 = tk.Label(self, text="And you can also check here any interactions a person may have", font=("Source Sans Pro", 11, "bold"), background="#E3DAFF")
        instruction_2.place(x=23, y=130)
        
        instruction_2 = tk.Label(self, text="had with somebody who might be a COVID-19 virus carrier.", font=("Source Sans Pro", 11, "bold"), background="#E3DAFF")
        instruction_2.place(x=40, y=150)