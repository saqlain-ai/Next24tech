import customtkinter as ctk
from tkinter import scrolledtext
import re
from datetime import datetime
import random

class ChatbotApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Chatbot")
        self.geometry("400x600")
        self.configure(bg_color='gray20')
        self.create_widgets()

    def create_widgets(self):
        self.chat_area = scrolledtext.ScrolledText(self, state='disabled', bg='black', fg='white', font=('Helvetica', 12), wrap='word')
        self.chat_area.pack(expand=True, fill='both', padx=10, pady=(10, 5))

        self.message_frame = ctk.CTkFrame(self, bg_color='gray20')
        self.message_frame.pack(fill='x', padx=10, pady=(0, 10))

        self.message_entry = ctk.CTkEntry(self.message_frame, placeholder_text="Type your message...", font=('Helvetica', 12))
        self.message_entry.pack(side='left', fill='x', padx=(0, 10), pady=5, expand=True)

        self.send_button = ctk.CTkButton(self.message_frame, text="Send", command=self.send_message, fg_color='blue', hover_color='darkblue')
        self.send_button.pack(side='right', padx=5, pady=5)

    def send_message(self):
        user_message = self.message_entry.get()
        if user_message:
            self.display_message(user_message, "User")
            response = self.generate_response(user_message)
            self.display_message(response, "Chatbot")
            self.message_entry.delete(0, 'end')

    def display_message(self, message, sender):
        self.chat_area.config(state='normal')
        self.chat_area.insert('end', f"{sender}: {message}\n")
        self.chat_area.config(state='disabled')
        self.chat_area.yview('end')

    def generate_response(self, user_message):
        patterns = {
            r'hello|hi|hey': "Hello! How can I assist you today?",
            r'how are you': "I'm doing well, thanks for asking! How about you?",
            r'what is your name': "I'm your friendly chatbot. What's your name?",
            r'bye|goodbye': "Goodbye! Have a great day!",
            r'time': self.get_time,
            r'date': self.get_date,
            r'how old are you': "I don't have an age, but I was created recently.",
            r'what can you do': "I can answer questions about the time, date, and engage in basic conversation.",
            r'joke|tell me a joke': self.tell_joke,
            r'trash talk': self.trash_talk,
            r'.*': self.default_response
        }
        for pattern, response in patterns.items():
            if re.search(pattern, user_message, re.IGNORECASE):
                if callable(response):
                    return response()
                return response
        return self.default_response()

    def get_time(self):
        return f"The current time is {datetime.now().strftime('%H:%M:%S')}."

    def get_date(self):
        return f"Today's date is {datetime.now().strftime('%Y-%m-%d')}."

    def tell_joke(self):
        jokes = [
            "Why did the scarecrow win an award? Because he was outstanding in his field!",
            "Why don't scientists trust atoms? Because they make up everything!",
            "What do you call fake spaghetti? An impasta!"
        ]
        return random.choice(jokes)

    def trash_talk(self):
        responses = [
            "I'm just a chatbot, but even I could outwit you!",
            "Is that the best you've got? Try again!",
            "You might want to save your energy; I'm unbeatable!"
        ]
        return random.choice(responses)

    def default_response(self):
        return "I'm not sure how to respond to that. Can you ask me something else?"

if __name__ == "__main__":
    app = ChatbotApp()
    app.mainloop()
