import tkinter as tk


def press_button():
    # set output text
    # read input text width method get()
    output['text'] = "Hej " + userInput.get()


# root is main window
root = tk.Tk()
root.title("demo 1")
root.minsize(100, 50)

# label added to root
label = tk.Label(root, text='Skriv in dit namn och tryck på knappen.')
# call pack() to arrange label and make it visible
label.pack()

# text input added to root
userInput = tk.Entry(root)
userInput.pack()

# button added to root
# The function press_button() will be called when button is pressed.
button = tk.Button(root, text='Tryck på knappen', command=press_button)
button.pack()

output = tk.Label(root, text='output')
output.pack()

# run application
root.mainloop()