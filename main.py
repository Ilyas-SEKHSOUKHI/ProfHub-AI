import tkinter as tk
from tkinter import scrolledtext
from groq import Groq

# Création du client
client = Groq(api_key="")

# Prompts
ENGLISH_PROF = (
    "You are an English professor. "
    "You ONLY answer questions related to English language: grammar, vocabulary, writing, speaking, comprehension. "
    "If the question is not related to English, respond: 'I only answer English-related questions.' "
    "Be clear, educational, and give examples when needed."
)

CS_PROF = (
    "You are a Computer Science professor. "
    "You ONLY answer questions about programming, algorithms, data structures, databases, AI, and software engineering. "
    "If the question is not related to computer science, respond: 'I only answer computer science questions.' "
    "Explain clearly with simple examples."
)

MANAGEMENT_PROF = (
    "You are a Management professor. "
    "You ONLY answer questions about management, business, leadership, organization, marketing, and economics basics. "
    "If the question is not related to management, respond: 'I only answer management-related questions.' "
    "Be practical and give real-world examples."
)

# Fonction API
def chat_with_groq(messages):
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=messages
    )
    return response.choices[0].message.content


# ================= UI =================

class ProfHubApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ProfHub Chatbot")
        self.root.geometry("500x600")

        self.system_prompt = ENGLISH_PROF

        # Choix du prof
        self.label = tk.Label(root, text="Choisir un professeur :", font=("Arial", 12))
        self.label.pack(pady=5)

        self.prof_choice = tk.StringVar(value="English")

        tk.Radiobutton(root, text="English", variable=self.prof_choice, value="English", command=self.set_prof).pack()
        tk.Radiobutton(root, text="Computer Science", variable=self.prof_choice, value="CS", command=self.set_prof).pack()
        tk.Radiobutton(root, text="Management", variable=self.prof_choice, value="Management", command=self.set_prof).pack()

        # Zone de chat
        self.chat_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=20)
        self.chat_area.pack(pady=10)
        self.chat_area.config(state='disabled')

        # Input
        self.user_input = tk.Entry(root, width=40)
        self.user_input.pack(side=tk.LEFT, padx=10, pady=10)

        # Bouton envoyer
        self.send_button = tk.Button(root, text="Envoyer", command=self.send_message)
        self.send_button.pack(side=tk.LEFT)

    def set_prof(self):
        choice = self.prof_choice.get()
        if choice == "English":
            self.system_prompt = ENGLISH_PROF
        elif choice == "CS":
            self.system_prompt = CS_PROF
        elif choice == "Management":
            self.system_prompt = MANAGEMENT_PROF

    def send_message(self):
        user_text = self.user_input.get()
        if user_text == "":
            return

        self.chat_area.config(state='normal')
        self.chat_area.insert(tk.END, "You: " + user_text + "\n")

        messages = [
            {"role": "system", "content": self.system_prompt},
            {"role": "user", "content": user_text}
        ]

        reply = chat_with_groq(messages)

        self.chat_area.insert(tk.END, "Bot: " + reply + "\n\n")
        self.chat_area.config(state='disabled')

        self.user_input.delete(0, tk.END)


# Lancer app
if __name__ == "__main__":
    root = tk.Tk()
    app = ProfHubApp(root)
    root.mainloop()