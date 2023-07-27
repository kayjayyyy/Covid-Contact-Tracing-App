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
        
        # Close button
        close = tk.Button(self, text="Close", command=self.destroy)
        close.place(x=265, y=680)
    
        # Text widget to display results
        self.result = tk.Text(self, width=50, height=18, wrap=tk.WORD, bg="#E3DAFF")
        self.result.place(x=46, y=290)
        
    def search(self):
        search_term = self.search_entry.get()
        if search_term:
            search_results = []
            with open('Responses.csv', 'r', newline='') as csvfile:
                reader = csv.reader(csvfile)
                header = next(reader)
                for row in reader:
                    for value in row:
                        if search_term.lower() in value.lower():
                            search_results.append(row)
                            break 

            self.display_results(search_results)
            
    def display_results(self, results):
        self.result.delete(1.0, tk.END)
        
        for row in results:
            if len(row) > 0:
                self.result.insert(tk.END, f"Full Name: {', '.join(row[0:1])}\n")
                self.result.insert(tk.END, f"Age: {', '.join(row[1:2])}\n")
                self.result.insert(tk.END, f"Phone number: {', '.join(row[2:3])}\n")
                self.result.insert(tk.END, f"Email: {', '.join(row[3:4])}\n")
                self.result.insert(tk.END, f"Address: {', '.join(row[4:5])}\n")
                self.result.insert(tk.END, f"Fever? {', '.join(row[5:6])}\n")
                self.result.insert(tk.END, f"Loss of taste? {', '.join(row[6:7])}\n")
                self.result.insert(tk.END, f"Loss of smell? {', '.join(row[7:8])}\n")
                self.result.insert(tk.END, f"Cough or sore throat? {', '.join(row[8:9])}\n")
                self.result.insert(tk.END, f"Shortness of Breath? {', '.join(row[9:10])}\n")
                self.result.insert(tk.END, f"Difficulty of breathing? {', '.join(row[10:11])}\n")
                self.result.insert(tk.END, f"Nausea or vomiting? {', '.join(row[11:12])}\n")
                self.result.insert(tk.END, f"Musle or body pains? {', '.join(row[12:13])}\n")
                self.result.insert(tk.END, f"Headache? {', '.join(row[13:14])}\n")
                self.result.insert(tk.END, f"Have you had exposure to a probable or confirmed case in the last 14 days? {', '.join(row[14:15])}\n")
                
            self.result.insert(tk.END, "\n")
            
        if not results:
            self.result.insert(tk.END, "We're sorry. There are no matches.")
            
    def back_to_main(self):
        self.destroy()
        from ContactTracingApp import MainScreen
        entry = MainScreen()
        entry.mainloop()

if __name__ == "__main__":
    search = SearchEntry()
    search.mainloop()