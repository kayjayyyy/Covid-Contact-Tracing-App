# Templanza, Kristine Joy F.
# BSCPE 1-4
# Final Project - Covid Contact Tracing App

import tkinter as tk
from AddEntryScreen import StartScreen
from SearchEntryScreen import SearchEntry

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
        
        # Description
        description = tk.Label(self, text="This Contact Tracing App will aid in finding those", font=("Source Sans Pro", 12, "bold"), background="#E3DAFF")
        description.place(x=65, y=380)
        
        description = tk.Label(self, text="who are at risk of viral exposure.", font=("Source Sans Pro", 12, "bold"), background="#E3DAFF")
        description.place(x=120, y=400)
        
        # Add entry button
        Start_button = tk.Button(self, text="Add entry", command=self.open_add_entry, height=2, width=14)
        Start_button.place(x=128, y=495)
        
        # Search entry button
        SearchEntryButton = tk.Button(self, text="Search Entry", command=self.open_search_entry, height=2, width=14)
        SearchEntryButton.place(x=270, y=495)
        
        # Close button
        close = tk.Button(self, text="Close", command=self.close_window)
        close.place(x=230, y=750)
        
    def open_add_response(self):
        self.destroy()
        entry = StartScreen()
        entry.mainloop()
        
    def open_search_entry(self):
        self.destroy()
        search = SearchEntry()
        search.mainloop()
        
    def close_window(self):
        self.destroy()
        
if __name__ == "__main__":
    app = MainScreen()
    app.mainloop()