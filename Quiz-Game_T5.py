'''quiz_data = [
    {
        "question": "Which city is known as the “summer capital” of Jammu and Kashmir?",
        "options": ["Jammu", "Srinagar", "Shimla", "Anantnag"],
        "correct_answer": "Srinagar",
    },
    {
        "question": "If you divivde any Natural Number by Zero the Result will be ?",
        "options": ["Zero", "Infinity", "Arthmetical Error", "One"],
        "correct_answer": "Infinity",
    },
    {
        "question": "Which planet is the largest planet in the Solar System'?",
        "options": ["Venus", "Jupiter", "Mars", "Neptune"],
        "correct_answer": "Jupiter",
    },
    {
        "question": "Which Supreme Country Invented the number Zero?",
        "options": ["India", "US", "France", "China"],
        "correct_answer": "India",
    },
]'''
import tkinter as tk
from tkinter import messagebox

# Quiz questions and answers 
quiz_data = [
    {
        "question": "Which city is known as the “summer capital” of Jammu and Kashmir?",
        "options": ["Jammu", "Srinagar", "Shimla", "Anantnag"],
        "correct_answer": "Srinagar",
    },
    {
        "question": "If you divivde any Natural Number by Zero the Result will be ?",
        "options": ["Zero", "Infinity", "Arthmetical Error", "One"],
        "correct_answer": "Infinity",
    },
    {
        "question": "Which planet is the largest planet in the Solar System'?",
        "options": ["Venus", "Jupiter", "Mars", "Neptune"],
        "correct_answer": "Jupiter",
    },
    {
        "question": "Which Supreme Country Invented the number Zero?",
        "options": ["India", "US", "France", "China"],
        "correct_answer": "India",
    },
]

class QuizApplication(tk.Tk):
    def __init__(self):
        super().__init__()

        self.score = 0
        self.current_question = 0

        self.title("Quiz Game By Chetan Dawani")
        self.geometry("600x500")

        self.label_question = tk.Label(self, text="", wraplength=300, font=('Arial Black', 20, 'bold'))
        self.label_question.pack(pady=10)

        self.radio_var = tk.StringVar()
        self.radio_var.set(-1) 

        self.radio_buttons = []
        for i in range(4):
            radio = tk.Radiobutton(self, text="", variable=self.radio_var, value=i)
            self.radio_buttons.append(radio)
            radio.pack()

        self.button_next = tk.Button(self, text="Next", command=self.next_question, font=('Arial Black', 14, 'bold'))
        self.button_next.pack(pady=10)
        self.loading_question(0)
        

    def loading_question(self, question_index):
        if question_index < len(quiz_data):
            self.label_question.config(text=quiz_data[question_index]["question"])
            for i in range(4):
                self.radio_buttons[i].config(text=quiz_data[question_index]["options"][i], font=('Algerian', 14 ))
        else:
            self.show_result()

    def next_question(self):
        selected_option = int(self.radio_var.get())

        if selected_option == -1:
            messagebox.showwarning("Warning", "Please select an option.", font=('Arial Narrow', 10, 'bold'))
        else:
            correct_answer = quiz_data[self.current_question]["correct_answer"]
            if quiz_data[self.current_question]["options"][selected_option] == correct_answer:
                self.score += 1

            self.current_question += 1
            self.radio_var.set(-1)  

            if self.current_question < len(quiz_data):
                self.loading_question(self.current_question)
            else:
                self.show_result()

    def show_result(self):
        messagebox.showinfo("Your Result:", f"You've scored: {self.score}/{len(quiz_data)}")
        self.quit()

if __name__ == "__main__":
    app = QuizApplication()
    app.mainloop()