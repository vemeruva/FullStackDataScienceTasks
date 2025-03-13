import tkinter as tk 

# function to called when button is clicked
def on_button_click():
    label.config(text = 'Button clicked')

#create the main application window 
root = tk.Tk()
root.geometry("300x150")
root.resizable(0,0)
root.title('Simple tkinter app')

#create label widget
label = tk.Label(root, text ='hello Tkinter')
label.pack(pady=20)

# button creation 
button = tk.Button(root, text = 'Click me ', command = on_button_click)
button.pack(pady=20)

root.mainloop()