from tkinter import *
from tkinter import ttk
from translate import Translator

# Initialize the main window
root = Tk()
root.title("Translator")
root.geometry("500x700")
root.config(bg='Red')

# Function to handle translation
def translate_text():
    source_text = src_txt.get("1.0", END).strip()
    src_language = comb_sor.get()
    dest_language = dest_sor.get()

    if source_text:
        try:
            translator = Translator(from_lang=src_language, to_lang=dest_language)
            translation = translator.translate(source_text)
            dest_txt.delete("1.0", END)
            dest_txt.insert(END, translation)
        except Exception as e:
            dest_txt.delete("1.0", END)
            dest_txt.insert(END, f"Error: {str(e)}")

# Title Label
lbl_txt = Label(root, text="Translator", font=("Times New Roman", 40, "bold"), bg="Red", fg="white")
lbl_txt.place(x=100, y=20, height=60, width=300)

# Source Text Label
lbl_source = Label(root, text="Source Text", font=("Times New Roman", 20, "bold"), fg='black', bg='Red')
lbl_source.place(x=100, y=100, height=30, width=300)

# Source Text Box
src_txt = Text(root, font=("Times New Roman", 16), wrap=WORD, bg="lightgray", fg="black")
src_txt.place(x=10, y=150, height=150, width=480)

# Extended Language List
languages = [
    "english", "spanish", "french", "german", "hindi", "italian", "chinese",
    "japanese", "korean", "russian", "arabic", "portuguese", "turkish",
    "dutch", "swedish", "greek", "polish", "indonesian", "thai", "vietnamese",
    "malay", "persian", "urdu", "hebrew", "romanian", "bulgarian", "czech",
    "slovak", "hungarian", "norwegian", "danish", "finnish"
]

# Combobox for Source Language Selection
comb_sor = ttk.Combobox(root, value=languages, font=("Times New Roman", 14), height=10)
comb_sor.place(x=10, y=320, height=40, width=150)
comb_sor.set("english")  # Default source language

# Combobox for Destination Language Selection
dest_sor = ttk.Combobox(root, value=languages, font=("Times New Roman", 14), height=10)
dest_sor.place(x=330, y=320, height=40, width=150)
dest_sor.set("english")  # Default target language

# Translate Button
button_change = Button(root, text="Translate", relief=RAISED, font=("Times New Roman", 14), command=translate_text)
button_change.place(x=190, y=320, height=40, width=120)

# Destination Text Label
lbl_dest = Label(root, text="Destination Text", font=("Times New Roman", 20, "bold"), fg='black', bg='Red')
lbl_dest.place(x=100, y=380, height=30, width=300)

# Destination Text Box
dest_txt = Text(root, font=("Times New Roman", 16), wrap=WORD, bg="lightgray", fg="black")
dest_txt.place(x=10, y=430, height=150, width=480)

# Start the main loop
root.mainloop()