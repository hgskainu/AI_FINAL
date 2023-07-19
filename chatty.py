from tkinter import BOTH, YES, ttk
from tkmacosx import Button
import openai
import speech_recognition as sr
from tkinter.constants import DISABLED, NORMAL, END
import tkinter as tk
from PIL import Image, ImageTk
# Set up OpenAI API credentials
openai.api_key = ''
def ask_openai(question):
    model_engine = "text-davinci-003"
    prompt = f"Q: {question}\nA:"
    completions = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )
    message = completions.choices[0].text.strip()
    return message
# Function to recognize speech using microphone
def recognize_speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        return "Sorry, I could not understand you."
    except sr.RequestError:
        return "Sorry, my speech recognition service is currently down."
class ChatbotGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("F.R.I.D.A.Y")
        # Set the background image
        def resize_image(event):
            new_width = event.width
            new_height = event.height
            image = copy_of_image.resize((new_width, new_height))
            photo = ImageTk.PhotoImage(image)
            label.config(image = photo)
            label.image = photo #avoid garbage collection
        image = Image.open('photo.jpeg')
        copy_of_image = image.copy()
        photo = ImageTk.PhotoImage(image)
        label = ttk.Label(self.window, image = photo)
        label.bind('<Configure>', resize_image)
        label.pack(fill=BOTH, expand = YES)
        self.chat_history = tk.Text(
            label,
            wrap="word",
            state="disabled",
            bg="#15202B",  # Adjusted black background
            fg="#00BFFF",  # Blue text
            font=("Comic Sans MS", 14),
        )
        self.chat_history.place(relx=0.05, rely=0.1, relwidth=0.9, relheight=0.6)
        self.question_entry = tk.Entry(
            label,
            font=("Comic Sans MS", 14),
            bg="#263238",  # Darker blue background
            fg="#FFFFFF",  # White text
        )
        placeholder_text = 'Type here...'
        self.question_entry.insert(0, placeholder_text)
        self.question_entry.bind("<Button-1>", lambda event: clear_entry(event,self.question_entry))
        self.question_entry.configure(fg="white")
        def clear_entry(event, entry):
            entry.delete(0, 'end')
            entry.unbind('<Button-1>', event)
        self.question_entry.place(relx=0.05, rely=0.75, relwidth=0.6, relheight=0.1)
        self.ask_button = Button(
            label,
            text="Ask",
            command=self.ask_question,
            font=("Comic Sans MS", 14),
            bg="#00BFFF",  # Blue background
            fg="#15202B",  # Adjusted black text
            activebackground="#5CACEE",  # Lighter blue when clicked
            activeforeground="#15202B",  # Adjusted black text when clicked
        )
        self.ask_button.place(relx=0.67, rely=0.75, relwidth=0.28, relheight=0.1)
        # Bind Enter key to ask question
        self.window.bind("<Return>", self.on_enter_key)
        self.window.mainloop()
    def ask_question(self, event=None):  # Add event=None to handle button click
        question = self.question_entry.get().strip()
        if question != "":
            response = ask_openai(question)
            self.update_chat_history(question, response)
        self.question_entry.delete(0, "end")
    def update_chat_history(self, question, response):
        self.chat_history.configure(state="normal")
        if self.chat_history.index('end') != None:
            self.chat_history.insert('end', "You: " + question + "\n", 'bold')
            self.chat_history.insert('end', "Friday: " + response + "\n\n")
            self.chat_history.tag_configure('bold', font=("Comic Sans MS", 14, 'bold'))
            self.chat_history.configure(state="disabled")
            self.chat_history.see('end')  # Scroll to end
    def on_enter_key(self, event):
        self.ask_question()
if __name__ == "__main__":from tkinter import BOTH, YES, ttk
import openai
import speech_recognition as sr
from tkinter.constants import DISABLED, NORMAL, END
import tkinter as tk
from PIL import Image, ImageTk
# Set up OpenAI API credentials
openai.api_key = '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'
def ask_openai(question):
    model_engine = "text-davinci-003"
    prompt = f"Q: {question}\nA:"
    completions = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )
    message = completions.choices[0].text.strip()
    return message
# Function to recognize speech using microphone
def recognize_speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        return "Sorry, I could not understand you."
    except sr.RequestError:
        return "Sorry, my speech recognition service is currently down."
class ChatbotGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("F.R.I.D.A.Y")
        self.window.geometry("300x520")
        # Set the background image
        def resize_image(event):
            new_width = event.width
            new_height = event.height
            image = copy_of_image.resize((new_width, new_height))
            photo = ImageTk.PhotoImage(image)
            label.config(image = photo)
            label.image = photo #avoid garbage collection
        image = Image.open('photo.jpeg')
        copy_of_image = image.copy()
        photo = ImageTk.PhotoImage(image)
        label = ttk.Label(self.window, image = photo)
        label.bind('<Configure>', resize_image)
        label.pack(fill=BOTH, expand = YES)
        
        message = "[Enter] to ask, [Enter] + [Shift] to clear the chat history"

        self.chat_history = tk.Text(
            label,
            wrap="word",
            bg="#15202B",  # Adjusted black background
            fg="#00BFFF",  # Blue text
            font=("Comic Sans MS", 14),
        )
        self.chat_history.place(relx=0.05, rely=0.1, relwidth=0.9, relheight=0.6)
        self.chat_history.insert('end', message)
        self.chat_history.config(state="disabled")
        self.question_entry = tk.Entry(
            label,
            font=("Comic Sans MS", 14),
            bg="#263238",  # Darker blue background
            fg="#FFFFFF",  # White text
        )
        placeholder_text = 'Type here...'
        self.question_entry.insert(0, placeholder_text)
        self.question_entry.bind("<Button-1>", lambda event: clear_entry(event,self.question_entry))
        self.question_entry.configure(fg="white")
        self.question_entry.bind("<Shift-Return>", self.clear_chat_history)  # Bind Shift+Enter to clear chat history
        def clear_entry(event, entry):
            entry.delete(0, 'end')
            entry.unbind('<Button-1>', event)
        self.question_entry.place(relx=0.05, rely=0.75, relwidth=0.6, relheight=0.1)
        self.ask_button = Button(
            label,
            text="Ask",
            command=self.ask_question,
            font=("Comic Sans MS", 16),
            bg="#00BFFF",  # Blue background
            fg="#15202B",  # Adjusted black text
            activebackground="#EEDC82",  # Lighter blue when clicked
            activeforeground="#15202B",  # Adjusted black text when clicked
        )
        self.ask_button.place(relx=0.67, rely=0.75, relwidth=0.28, relheight=0.1)
        # Bind Enter key to ask question
        self.window.bind("<Return>", self.on_enter_key)
        self.window.mainloop()
    def ask_question(self, event=None):  # Add event=None to handle button click
        question = self.question_entry.get().strip()
        if question != "":
            response = ask_openai(question)
            self.update_chat_history(question, response)
        self.question_entry.delete(0, "end")
    def update_chat_history(self, question, response):
        self.chat_history.configure(state="normal")
        if self.chat_history.index('end') != None:
            self.chat_history.insert('end', "\n\n" "You: " + question + "\n", 'bold')
            self.chat_history.insert('end', "Friday: " + response + "\n\n")
            self.chat_history.tag_configure('bold', font=("Comic Sans MS", 14, 'bold'))
            self.chat_history.configure(state="disabled")
            self.chat_history.see('end')  # Scroll to end
    def on_enter_key(self, event):
        self.ask_question()

    def clear_chat_history(self, event):
        self.chat_history.configure(state="normal")
        self.chat_history.delete(1.0, END)
        self.chat_history.configure(state="disabled")
if __name__ == "__main__":
    gui = ChatbotGUI()