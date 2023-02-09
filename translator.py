from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES
page = Tk()
page.geometry("1920x1080")
def translatebutton():
    entrytext = entrybar.get(1.0, END)
    translator = Translator()
    translated = translator.translate(text=entrytext, src=inputlanguage.get(), dest=outputlanguage.get())
    print(translated)
    outputbar.delete(1.0, END)
    outputbar.insert(END, translated.text)


language = list(LANGUAGES.values())
inputlanguage = ttk.Combobox(page, values=language, width="50",)
inputlanguage.place(relx='0.05', rely="0.1")
inputlanguage.set("Please select your input language")
outputlanguage = ttk.Combobox(page, values= language, width="50")
outputlanguage.place(relx="0.65", rely="0.1")
outputlanguage.set("Please select your output language")
firstlanguage = Label(page, text="First Language")
firstlanguage.place(relx="0.05", rely="0.2")
entrybar = Text(page, width="80")
entrybar.place(relx="0.1", rely="0.2")
secondlanguage = Label(page, text="Translated language",)
secondlanguage.place(relx="0.55", rely="0.2")
outputbar = Text(page, width="80")
outputbar.place(relx="0.65", rely="0.2")
translatorbutton = Button(page, command=translatebutton, text="Translate")
translatorbutton.place(relx="0.5", rely="0.3")
page.mainloop()