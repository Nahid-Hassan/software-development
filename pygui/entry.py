from tkinter import *

# start
root = Tk()

# business logic
entry = Entry(root, width=50, borderwidth=3)
entry.pack()
entry.insert(0, "Enter your name ")

def click_me():
    # entry.get()
    hello = 'Hello ' + entry.get()
    label = Label(root, text=hello)
    label.pack()

button = Button(root, text='Submit', command=click_me)
button.pack()

# end
root.mainloop()