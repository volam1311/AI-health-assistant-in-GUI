from tkinter import *
from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
# Set up the language model
model = OllamaLLM(model="llama3.2")
template = """
Imagine yourself as a psychiatrist. Give advice to a patient so that he can feel better.
Here is his concern: {questions}
"""
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model
window = Tk()
window.geometry("800x800")
window.title("AI Psychiatrist")

def get_advice():
    questions = user_entry.get()
    if questions.strip(): 
        response = chain.invoke(questions)
        answer.delete("1.0", END)
        answer.insert("1.0", response)


logo  = Label(text="Assistant for Health", font=("Helvetica", 30))
logo.pack(pady = 15)

user_input = Frame(window)
user_entry = Entry(user_input, width=50, font = ("Times New Roman",15))
user_entry.pack(side = 'left',padx=10,fill = 'both')
submit = Button(user_input, text="Get Advice", command=get_advice)
submit.pack(side = 'left',padx=5)
user_input.pack(pady = 10)

advice = Frame(window)
answer = Text(advice, wrap=WORD)
answer.pack(side = 'left')
scroll = Scrollbar(advice)
answer.config(yscrollcommand=scroll.set)
scroll.config(command = answer.yview)
scroll.pack(side = 'left',fill =  'y')
advice.pack()

window.mainloop()
