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
        
        # Search label and entry box
        search_entry = tk.Label(self, text="Search by Name:", bg="#E3DAFF")
        search_entry.place(x=30, y=233)

        self.search_entry = tk.Entry(self, width=45)
        self.search_entry.place(x=130, y=233)
        
        # Search button
        search_button = tk.Button(self, text="Search", command=self.search)
        search_button.place(x=415, y=230)

        # Back button
        back_to_main_button = tk.Button(self, text="Back", command=self.back_to_main)
        back_to_main_button.place(x=195, y=680)
        