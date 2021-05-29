from tkinter import *

# create root widget
root = Tk()

def my_click():
    my_label = Label(root, text='I just clicked a button!')
    my_label.pack()

# create button
my_button = Button(root, text="Click Me!", command=my_click, fg='blue', bg='red')

# pack
my_button.pack()

# mainloop
root.mainloop()