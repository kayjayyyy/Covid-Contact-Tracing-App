# Templanza, Kristine Joy F.
# BSCPE 1-4
# Final Project - Covid Contact Tracing App

import tkinter as tk
from tkinter import messagebox, ttk
import csv

class StartScreen(tk.Tk):

    def __init__(self):
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
        
        # Symptoms no.8 Muscle or body pains
        symptoms_8_label = tk.Label(self, text="Muscle or body pains?", font=("Source Sans Pro", 11, "bold"), background="#E3DAFF")
        symptoms_8_label.place(x=80, y=495)

        yes_button_8 = ttk.Radiobutton(self, variable=self.qs8, value=1, text="Yes", style="Custom.TRadiobutton")
        yes_button_8.place(x=280, y=495)

        no_button_8 = ttk.Radiobutton(self, variable=self.qs8, value=0, text="No", style="Custom.TRadiobutton")
        no_button_8.place(x=370, y=495)
        
        # Symptoms no. 9 Headache
        symptoms_9_label = tk.Label(self, text="Headache?", font=("Source Sans Pro", 11, "bold"), background="#E3DAFF")
        symptoms_9_label.place(x=80, y=525)
        
        yes_button_9 = ttk.Radiobutton(self, variable=self.qs9, value=1, text="Yes", style="Custom.TRadiobutton")
        yes_button_9.place(x=280, y=525)
        
        no_button_9 = ttk.Radiobutton(self, variable=self.qs9, value=0, text="No", style="Custom.TRadiobutton")
        no_button_9.place(x=370, y=525)
        
        # Question no.10 Exposure
        question_10_label = tk.Label(self, text="Have you had exposure to a", font=("Source Sans Pro", 10, "bold"), background="#E3DAFF")
        question_10_label.place(x=55, y=555)
        
        question_10_label = tk.Label(self, text="probable or confirmed case in", font=("Source Sans Pro", 10, "bold"), background="#E3DAFF")
        question_10_label.place(x=48, y=575)
        
        question_10_label = tk.Label(self, text="the last 14 days?", font=("Source Sans Pro", 10, "bold"), background="#E3DAFF")
        question_10_label.place(x=85, y=595)
        
        yes_button_10 = ttk.Radiobutton(self, variable=self.qs10, value=1, text="Yes", style="Custom.TRadiobutton")
        yes_button_10.place(x=280, y=575)
        
        no_button_10 = ttk.Radiobutton(self, variable=self.qs10, value=0, text="No", style="Custom.TRadiobutton")
        no_button_10.place(x=370, y=575)
        
        # Terms and Condition
        terms = tk.Label(self, text="In line with the Data Privacy Act of 2012", font=("Source Sans Pro", 11, "bold"), background="#E3DAFF")
        terms.place(x=110, y=655)
        
        terms_next = tk.Label(self, text="Please be informed that data gathered in this form", font=("Source Sans Pro", 10), background="#E3DAFF")
        terms_next.place(x=100, y=675)
        
        terms_next_2 = tk.Label(self, text="will be treated with the utmost confidentiality.", font=("Source Sans Pro", 10), background="#E3DAFF")
        terms_next_2.place(x=113, y=695)
        
        # Submit button
        submit_button = tk.Button(self, text="Submit", command=self.submit_response)
        submit_button.place(x=188, y=750)
        
        # Back button
        go_back_to_start = tk.Button(self, text="Back", command=self.to_start_screen)
        go_back_to_start.place(x=260, y=750)
    
    # Define back to start screen
    def to_start_screen(self):
        self.destroy()

    # Define success window message
    def success_window_message(self):
        messagebox.showinfo("Thank you!", "Your response has been successfully saved")
        self.destroy()
    
    # Define submit responses
    def submit_response(self):
        full_name = self.full_name_entry.get()
        age = self.age_entry.get()
        phone_number = self.phone_number_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()
        covid_symptoms = ["No" if value == 0 else "Yes" for value in [self.qs1.get(), self.qs2.get(), self.qs3.get(), self.qs4.get(),
                self.qs5.get(), self.qs6.get(), self.qs7.get(), self.qs8.get(), self.qs9.get(), self.qs10.get()]]
        
        # Write/save to csv file 
        data = [full_name, age, phone_number, email, address] + covid_symptoms
        file = open("Responses.csv", mode="a", newline="")
        response = csv.writer(file)
        response.writerow(data)
        file.close()
        
        # Clear info in entry box
        self.full_name_entry.delete(0, 'end')
        self.age_entry.delete(0, 'end')
        self.phone_number_entry.delete(0, 'end')
        self.email_entry.delete(0, 'end')
        self.address_entry.delete(0, 'end')
        
        # Clear radiobuttons
        self.qs1.set(0)
        self.qs2.set(0)
        self.qs3.set(0)
        self.qs4.set(0)
        self.qs5.set(0)
        self.qs6.set(0)
        self.qs7.set(0)
        self.qs8.set(0)
        self.qs9.set(0)
        self.qs10.set(0)
        
        self.success_window_message()
        
if __name__ == "__main__":
    entry = StartScreen()
    entry.mainloop()