import tkinter as tk
import speech_recognition as sr
import pyttsx3

# ---------------- Text To Speech ----------------
engine = pyttsx3.init()

def speak(text):
    engine.say(str(text))
    engine.runAndWait()

# ---------------- Calculator Functions ----------------
expression = ""

def press(value):
    global expression
    expression += str(value)
    display_var.set(expression)

def clear():
    global expression
    expression = ""
    display_var.set("")

def delete():
    global expression
    expression = expression[:-1]
    display_var.set(expression)

def calculate():
    global expression

    try:
        result = str(eval(expression))
        display_var.set(result)
        speak("The answer is " + result)
        expression = result

    except:
        display_var.set("Error")
        expression = ""

# ---------------- Voice Input ----------------
def voice_input():
    global expression

    recognizer = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            display_var.set("Listening...")
            root.update()

            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)

        text = recognizer.recognize_google(audio)
        text = text.lower()

        replacements = {
            "zero":"0",
            "one":"1",
            "two":"2",
            "three":"3",
            "four":"4",
            "five":"5",
            "six":"6",
            "seven":"7",
            "eight":"8",
            "nine":"9",
            "plus":"+",
            "minus":"-",
            "times":"*",
            "multiply":"*",
            "multiplied by":"*",
            "divide":"/",
            "divided by":"/"
        }

        for word, symbol in replacements.items():
            text = text.replace(word, symbol)

        text = text.replace(" ", "")

        expression = text

        result = str(eval(expression))

        display_var.set(result)

        speak("The answer is " + result)

        expression = result

    except Exception:
        display_var.set("Voice Error")

# ---------------- GUI ----------------
root = tk.Tk()
root.title("AI Smart Calculator")
root.geometry("380x550")
root.configure(bg="#1e1e1e")
root.resizable(False, False)

display_var = tk.StringVar()

display = tk.Entry(
    root,
    textvariable=display_var,
    font=("Arial", 24),
    justify="right",
    bd=10,
    bg="white"
)

display.pack(fill="x", padx=10, pady=10, ipady=15)

# Button Frame
frame = tk.Frame(root, bg="#1e1e1e")
frame.pack()

buttons = [
    ['7','8','9','/'],
    ['4','5','6','*'],
    ['1','2','3','-'],
    ['0','.','=','+']
]

for row in buttons:
    row_frame = tk.Frame(frame, bg="#1e1e1e")
    row_frame.pack()

    for btn in row:
        if btn == "=":
            command = calculate
            color = "#4CAF50"
        else:
            command = lambda x=btn: press(x)
            color = "#333333"

        tk.Button(
            row_frame,
            text=btn,
            width=6,
            height=2,
            font=("Arial",18),
            bg=color,
            fg="white",
            command=command
        ).pack(side="left", padx=5, pady=5)

# Bottom Buttons
# Bottom Buttons
bottom = tk.Frame(root, bg="#1e1e1e")
bottom.pack(pady=10)

tk.Button(
    bottom,
    text="Clear",
    bg="red",
    fg="white",
    width=8,
    height=2,
    font=("Arial", 12, "bold"),
    command=clear
).pack(side="left", padx=5)

tk.Button(
    bottom,
    text="Delete",
    bg="orange",
    fg="white",
    width=8,
    height=2,
    font=("Arial", 12, "bold"),
    command=delete
).pack(side="left", padx=5)

tk.Button(
    bottom,
    text="🎤 Mic",
    bg="#2196F3",
    fg="white",
    width=8,
    height=2,
    font=("Arial", 12, "bold"),
    command=voice_input
).pack(side="left", padx=5)

root.mainloop()