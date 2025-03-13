from tkinter import *
import random, string
import pyperclip
import sys

root = Tk()
root.geometry("300x400")
root.resizable(0,0)
root.title("PYTHON PROJECT  - PASSWORD GENERATOR")

root.config(borderwidth=2, relief="ridge")
frame = Frame(root, highlightbackground="black", highlightthickness=1)
frame.pack(fill=BOTH, expand=True, padx=10, pady=10)

#Label(root, text='PASSWORD GENERATOR', font='arial 15 bold').pack()
Label(frame, text='PASSWORD GENERATOR', font=('arial', 15, 'bold underline')).pack()
Label(frame, text='', font='arial 5 bold').pack()
Label(root, text='@Meruva', font='arial 15 bold').pack(side=BOTTOM)

pass_label = Label(frame, text='PASSWORD LENGTH', font='arial 10 bold').pack()
pass_len = IntVar()
length = Spinbox(frame, from_=8, to_=32, textvariable=pass_len, width=15).pack()
pass_str = StringVar()

def Generator():
    password = []
    
    # Ensuring at least one character from each type (Uppercase, Lowercase, Digits, Punctuation)
    if pass_len.get() >= 4:
        password.append(random.choice(string.ascii_uppercase))
        password.append(random.choice(string.ascii_lowercase))
        password.append(random.choice(string.digits))
        password.append(random.choice(string.punctuation))

        # Fill the rest with random choices until the specified length
        for _ in range(pass_len.get() - 4):
            password.append(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation))
        
        # Shuffle to ensure randomness
        random.shuffle(password)
    else:
        # If length is less than 4, just fill the required length with random choices
        for _ in range(pass_len.get()):
            password.append(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation))
    
    # Convert list to string and set it to the variable
    pass_str.set(''.join(password))



def Copy_password():
    pyperclip.copy(pass_str.get())

def Clear_password():
    pass_str.set('')

def close_app():
    """
    Closes the application.
    """
    root.destroy()

Button(frame, text='GENERATE PASSWORD', command=Generator).pack(pady=5)
Entry(frame, textvariable=pass_str).pack()

button_frame = Frame(frame)
button_frame.pack(pady=10)

Button(button_frame, text='COPY TO CLIPBOARD', command=Copy_password).pack(side=LEFT, padx=5)
Button(button_frame, text='CLEAR', command=Clear_password).pack(side=LEFT, padx=5)

Button(frame, text='Exit', command=close_app).pack(side=BOTTOM,pady=5)
root.mainloop()