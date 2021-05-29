from tkinter import *

# root widget
root = Tk()

# create a label widgets
my_label1 = Label(root, text='Hello World!')
my_label2 = Label(root, text='My name is Md. Nahid Hassan.')
my_label3 = Label(root, text='              ')

# griding
# griding system are relative, that means row=0, column=5 don't make 
# a gap between row=0, column=0, this is just relative.

# my_label1.grid(row=0, column=0)
# my_label2.grid(row=1, column=5)
# my_label3.grid(row=0, column=2)


# Hence python is object oriented....we can do this things like this.
my_label1 = Label(root, text='Hello World!').grid(row=0, column=0)
my_label2 = Label(root, text='My name is Md. Nahid Hassan.').grid(row=0, column=1)


root.mainloop()