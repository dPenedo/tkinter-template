from tkinter import *
from tkinter import filedialog, messagebox

operator = ''

# Functions
#def function_print1():
#    return input_text1

# Colors
dark= '#252525'
light= '#FCFCFC'
accent = '#A5C9FF'
# Font
font = 'Inter'


# init tkinter
win = Tk()


# Window size

win.geometry('800x400')

# Don't maximize

win.resizable(0, 0)

# Window title
win.title('My browser application')

# Color if the window
win.config(bg=dark)


# Top frame
top_frame = Frame(win, relief=FLAT)
top_frame.pack(side= TOP)

# Title
title_label = Label(top_frame, text = 'Title of the application', fg= light, font=(font, 38, 'bold'), bg=dark)
title_label.grid(row=0, column=0)

# Description frame

description_frame = Frame(win, relief=FLAT)
description_frame.pack()
description_frame.config(width='400', height='200')
# Center frame
center_frame = Frame(win, bd=1, relief=FLAT)
center_frame.pack(side=TOP, pady=20)

# Bottoms frame
buttoms_frame = Frame(win, bd=1, relief=FLAT)
buttoms_frame.pack(side=TOP)
buttoms_frame.config(width='400', height='200')

# Results frame
results_frame = Frame(win,bg=light, bd=1, relief=FLAT)
results_frame.pack(side=BOTTOM, pady=10)
results_frame.config(width='400', height='200')
# App Description
description_label = Label(description_frame,
                                text='Description of the aplication',
                                font=(font, 12, 'bold'),
                                bg= dark,
                                fg=light,
                                pady = 10)

description_label.grid(row=0, column=0)

# Insert a text
input_label1 = Label(center_frame, text='Insert a text or an item:',
                                font=(font, 13, 'bold'),
                                bg= light,
                                fg=dark,
                                pady=10)
input_label1.grid(row=1, column=0)
input_text1 = Entry(center_frame,
                   font=(font, 13, 'bold'),
                   bg=light,
                    width=40,
                    show='Here')
input_text1.grid(row=1,column=1, padx=41)

# Insert another text
input_label2 = Label(center_frame, text='Insert another text:',
                                font=(font, 13, 'bold'),
                                bg= light,
                                fg=dark,
                                pady=10)
input_label2.grid(row=2, column=0)
input_text2 = Entry(center_frame,
                   font=(font, 13, 'bold'),
                   bg=light,
                    width=40)
input_text2.grid(row=2,column=1, padx=41)

# Buttons

button_a = Button(buttoms_frame,
            text= 'Button number one',
            font = (font, 12, 'bold'),
            fg= light,
            bg= dark,
            width=15,
            
            )

button_a.grid(row=3, column=2)

button_b = Button(buttoms_frame,
            text= 'Button number two',
            font = (font, 12, 'bold'),
            fg= light,
            bg= dark,
            width=15)

button_b.grid(row=4, column=2)
#button_b.config(command=function_print)

# Result text
results_text = Text(results_frame,
                font=(font,12, 'bold'),
                bd=1,
                width=42,
                height=10)



win.mainloop()

