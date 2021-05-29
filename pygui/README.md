# Tkinter

Tkinter is build in Python.

[Youtube Link](https://youtu.be/yQSEXcf6s2I?list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV)

## Table of Contents

- [Tkinter](#tkinter)
  - [Table of Contents](#table-of-contents)
    - [1. First GUI Program](#1-first-gui-program)
    - [2) Grid System](#2-grid-system)
    - [3) Button](#3-button)
    - [Entry or Input Field](#entry-or-input-field)

### 1. First GUI Program

In `tkinter` everything is `widgets`. There is 

- Button widgets
- Text widgets
- Frame widgets

**Create root widget**:

- First thing we need to import `tkinter` module and create a `root` widgets, the `main window` widgets.

```py
from tkinter import tk

# 
root = Tk()
```

**Two step process**:

**1) Create widgets**

- Then simply create a `label` widgets.

```py
my_label = Label(root, text='Hello World!')
```

**2) Pack or fit widget on the window**:


```py
my_label.pack()
```

**Mainloop**:

```py
root.mainloop()
```

All code in one place:

```py
from tkinter import *

root = Tk()

# create a label widget
my_label = Label(root, text='Hello World!')
# showing it onto the screen
my_label.pack()

root.mainloop()
```

**Run program**:

```console
$ python3 hello.py
```

**Output**:

![images](https://i.imgur.com/GwXUBs6.png)

### 2) Grid System

```py
# create a label widgets
my_label1 = Label(root, text='Hello World!')
my_label2 = Label(root, text='My name is Md. Nahid Hassan.')
my_label3 = Label(root, text='              ')

# griding
# griding system are relative, that means row=0, column=5 don't make 
# a gap between row=0, column=0, this is just relative.

my_label1.grid(row=0, column=0)
my_label2.grid(row=1, column=5)
my_label3.grid(row=0, column=2)
```

![images](images/1.png)

**Hence Python is object oriented we can do this above things like this**:

```py
# Hence python is object oriented....we can do this things like this.
my_label1 = Label(root, text='Hello World!').grid(row=0, column=0)
my_label2 = Label(root, text='My name is Md. Nahid Hassan.').grid(row=0, column=1)
```

### 3) Button

- **Create simple Button**

```py
my_button = Button(root, text="Click Me!")
```

- **Button with `state` parameter**:

```py
my_button = Button(root, text="Click Me!", state=DISABLED)
```

- **Resizing button using `padx` and `pady`**

```py
my_button = Button(root, text="Click Me!", padx=50, pady=30)
```

- **Action Perform**:

```py
def my_click():
    my_label = Label(root, text='I just clicked a button!')
    my_label.pack()

# create button
my_button = Button(root, text="Click Me!", command=my_click)
```

- **`Foreground` and `Background` Color**:


```py
# also can taken hex code
my_button = Button(root, text="Click Me!", command=my_click, fg='blue', bg='red')
```

- **Final Code**:

```py
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
```

![images](images/2.png)

### Entry or Input Field

- **Basic Entry**:

```py
entry = Entry(root, width=50, fg='blue', bg='gray')
entry.pack()
```

- **entry.get() and insert(position, text)**:

```py
# .....

# business logic
entry = Entry(root, width=50, borderwidth=3)
entry.pack()

entry.insert(0, "Enter your name ")

def click_me():
    #  .....
    # get() method
    hello = 'Hello ' + entry.get()
    label = Label(root, text=hello)
    # ....

button = Button(root, text='Submit', command=click_me)
#  ....
```

- **Full Code**:

```py
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
```

