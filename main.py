# ProfHub

# Import
from groq import Groq
#Creation du client groq
client = Groq(api_key="YOUR_API_KEY")
#le system prompt

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
#la fonction qui appelle IA
def chat_with_groq(messages):
    response = client.chat.completions.create(
        model = "llama-3.1-8b-instant",
        messages=messages
    )
    return response.choices[0].message.content

if __name__=="__main__":
    print("Choose professor:")
    print("1 - English")
    print("2 - Computer Science")
    print("3 - Management")

    choice = input("Select: ")

    if choice == "1":
        SYSTEM_PROMPT = ENGLISH_PROF
    elif choice == "2":
        SYSTEM_PROMPT = CS_PROF
    elif choice == "3":
        SYSTEM_PROMPT = MANAGEMENT_PROF
    else:
        SYSTEM_PROMPT = "You are a helpful assistant."
    
    while True:
        user_input = input("You : ")
        if user_input.lower() in ["quit","exit","break"]:
            break
        A = [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_input}
        ]
        reply = chat_with_groq(A)
        print("Chatbot : ", reply)