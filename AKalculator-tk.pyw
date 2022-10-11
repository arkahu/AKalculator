# -*- coding: cp1252 -*-

"""
--AKalculator--
version 3.0 
"Advanced Kalculator"?

This program is a simple function calculator.
Created by: Arttu Huttunen, Oulu, Finland
Created: October 2022.

Copyright (C) 2022 by Arttu Huttunen 
Published under MIT-license. Anyone is free to do anything they want with
the software or the source code and it comes with absolutely no warranty
of any kind.

This is a graphical frontend for Python's math functions.
Originally created with Python version 2.6.5 and PyQt4 4.5.4 in 
Python(x,y)-package in 2011. Version 2.0 updated with Python 3.4.1 and PyQt 4.10.4.
in 2015. Version 3.0 with Python 3 and tkinter for better compatibility.

You need Python3 and tkinter on your machine to run this. 
"""

import tkinter as tk
from tkinter import ttk
import cmath
from math import *

class CalculatorFrame(ttk.Frame):
    """Define the GUI and functions."""
    def __init__(self, container):
        super().__init__(container)

        #Amount of padding in widgets.
        options = {'padx': 5, 'pady': 5}
        
        self.commasToDots_status = True

        self.outputBox= tk.scrolledtext.ScrolledText(self, width=50,  height=16)
        self.outputBox.grid(column=0, row=0, columnspan=5, **options)

        self.inputStr = tk.StringVar()
        self.inputBox = ttk.Entry(self, textvariable=self.inputStr)
        self.inputBox.grid(column=0, row=1, columnspan=5, sticky=tk.EW, **options)
        self.inputBox.focus()

        self.calculate_button = ttk.Button(self, text='Calculate')
        self.calculate_button['command'] = self.Calculate
        self.calculate_button.grid(column=0, row=2, columnspan=5, sticky=tk.EW, **options)


        self.backspace_button = ttk.Button(self, text='Backspace')
        self.backspace_button['command'] = self.backspaceFunc
        self.backspace_button.grid(column=0, row=3, columnspan=2, sticky=tk.EW, **options)

        self.clear_button = ttk.Button(self, text='Clear')
        self.clear_button['command'] = lambda: self.inputBox.delete(0, 'end')
        self.clear_button.grid(column=3, row=3, columnspan=2, sticky=tk.EW, **options)


        self.button7 = ttk.Button(self, text='7')
        self.button7['command'] = lambda: self.insertFunc('7')
        self.button7.grid(column=0, row=4, sticky=tk.E, **options)

        self.button8 = ttk.Button(self, text='8')
        self.button8['command'] = lambda: self.insertFunc('8')
        self.button8.grid(column=1, row=4, sticky=tk.E, **options)

        self.button9 = ttk.Button(self, text='9')
        self.button9['command'] = lambda: self.insertFunc('9')
        self.button9.grid(column=2, row=4, sticky=tk.E, **options)

        self.buttonPO = ttk.Button(self, text='(')
        self.buttonPO['command'] = lambda: self.insertFunc('(')
        self.buttonPO.grid(column=3, row=4, sticky=tk.E, **options)

        self.buttonPC = ttk.Button(self, text=')')
        self.buttonPC['command'] = lambda: self.insertFunc(')')
        self.buttonPC.grid(column=4, row=4, sticky=tk.E, **options)


        self.button4 = ttk.Button(self, text='4')
        self.button4['command'] = lambda: self.insertFunc('4')
        self.button4.grid(column=0, row=5, sticky=tk.E, **options)

        self.button5 = ttk.Button(self, text='5')
        self.button5['command'] = lambda: self.insertFunc('5')
        self.button5.grid(column=1, row=5, sticky=tk.E, **options)

        self.button6 = ttk.Button(self, text='6')
        self.button6['command'] = lambda: self.insertFunc('6')
        self.button6.grid(column=2, row=5, sticky=tk.E, **options)

        self.buttonPlus = ttk.Button(self, text='+')
        self.buttonPlus['command'] = lambda: self.insertFunc('+')
        self.buttonPlus.grid(column=3, row=5, sticky=tk.E, **options)

        self.buttonMinus = ttk.Button(self, text='-')
        self.buttonMinus['command'] = lambda: self.insertFunc('-')
        self.buttonMinus.grid(column=4, row=5, sticky=tk.E, **options)


        self.button1 = ttk.Button(self, text='1')
        self.button1['command'] = lambda: self.insertFunc('1')
        self.button1.grid(column=0, row=6, sticky=tk.E, **options)

        self.button2 = ttk.Button(self, text='2')
        self.button2['command'] = lambda: self.insertFunc('2')
        self.button2.grid(column=1, row=6, sticky=tk.E, **options)

        self.button3 = ttk.Button(self, text='3')
        self.button3['command'] = lambda: self.insertFunc('3')
        self.button3.grid(column=2, row=6, sticky=tk.E, **options)

        self.buttonMul = ttk.Button(self, text='*')
        self.buttonMul['command'] = lambda: self.insertFunc('*')
        self.buttonMul.grid(column=3, row=6, sticky=tk.E, **options)

        self.buttonDiv = ttk.Button(self, text='/')
        self.buttonDiv['command'] = lambda: self.insertFunc('/')
        self.buttonDiv.grid(column=4, row=6, sticky=tk.E, **options)


        self.button0 = ttk.Button(self, text='0')
        self.button0['command'] = lambda: self.insertFunc('0')
        self.button0.grid(column=0, row=7, sticky=tk.E, **options)

        self.buttonDot = ttk.Button(self, text='.')
        self.buttonDot['command'] = lambda: self.insertFunc('.')
        self.buttonDot.grid(column=1, row=7, sticky=tk.E, **options)

        self.buttonMod = ttk.Button(self, text='Modulo')
        self.buttonMod['command'] = lambda: self.insertFunc('%')
        self.buttonMod.grid(column=2, row=7, sticky=tk.E, **options)

        self.buttonPow = ttk.Button(self, text='x^y')
        self.buttonPow['command'] = lambda: self.insertFunc('**')
        self.buttonPow.grid(column=3, row=7, sticky=tk.E, **options)

        self.buttonSQRT = ttk.Button(self, text='SQRT')
        self.buttonSQRT['command'] = lambda: self.insertFunc('sqrt(')
        self.buttonSQRT.grid(column=4, row=7, sticky=tk.E, **options)

        self.grid(padx=10, pady=10, sticky=tk.NSEW)

        #If return pressed, calculate.
        self.bind_all('<Return>', self.Calculate)


    def Calculate(self, event=None):
        """Calls python eval() function on the input and writes the result 
        to output. Errors are simplified to ERROR-text. If commasToDots-option
        is active, commas(,) are converted to dots(.), useful on euro keyboards.
        """
        try:
            inputText = str(self.inputBox.get())
            if self.commasToDots_status:
                inputText = inputText.replace(',','.')
            self.outputBox.insert('end', "%s = %s\n" % (inputText,eval(inputText)))
        except:
            if inputText != '':
                self.outputBox.insert('end', "ERROR\n")
        self.inputBox.focus()
        self.outputBox.see('end')

    def backspaceFunc(self):
        """Delete character at the inputbox."""
        cursorLocation=self.inputBox.index(tk.INSERT)
        #don't remove chars if cursor is at start of the line
        if cursorLocation !=0:
            self.inputBox.delete(cursorLocation-1)
        self.inputBox.focus()

    def insertFunc(self, insfunc):
        """Insert text to inputline. Used by buttons and menu functions. """
        cursorLocation=self.inputBox.index(tk.INSERT)
        self.inputBox.insert(cursorLocation, insfunc)
        self.inputBox.focus()

    def SetCommasToDots(self, new_status):
        self.commasToDots_status = new_status

    def ClearAllBoxes(self):
        self.inputBox.delete(0, 'end')
        self.outputBox.delete(1.0, 'end')
        self.inputBox.focus()

    def PrintHelp(self):
        self.outputBox.insert('end', """
AKalculator Usage instructions:
Example: sqrt(9) [click calculate]

This application uses Python's built in
mathematical functions for calculations
(math-module). You can type in an expression into
the 'input'-line and it will be evaluated with the
'eval()' method. Therefore it is possible to use
math functions not listed in the functions-menu 
(boolean, hexadecimals...).
NOTE: Radians always assumed, convert rads-degs when necessary.
NOTE: For complex math, use cmath.function [e.g. cmath.polar(1+1j)]
NOTE: Use dot for decimal point.\n""")
        self.outputBox.see('end')
        
    def PrintInfo(self):
        self.outputBox.insert('end', """
\nAKalculator \nVersion: 3.0 \nCreated by: 
Arttu Huttunen, (Oulu, Finland, 2022)
Copyright (C) 2022 by Arttu Huttunen
This software is distributed under MIT-license. Therefore it is free and open source software.\n""")
        self.outputBox.see('end')


class App(tk.Tk):
    """Set the app and define menus."""
    def __init__(self):
        super().__init__()
        self.title('AKalculator')
        #self.attributes('-topmost', 1)
        #self.geometry('300x300')

        self.commasToDots = tk.BooleanVar()
        self.commasToDots.set(True)

        #Call the actual GUI so that the functions can be used in the menus.
        self.GUI_Frame = CalculatorFrame(self)

        self.menubar=tk.Menu(self)
        self.config(menu = self.menubar)
        
        self.action_menu = tk.Menu(self.menubar, tearoff=False)
        self.action_menu.add_checkbutton(label="Commas to dots", onvalue=True,
                                offvalue=False, variable = self.commasToDots,
                                command= lambda:
                    self.GUI_Frame.SetCommasToDots(self.commasToDots.get())
                                )
        self.action_menu.add_command(
            label='Clear all',
            command=self.GUI_Frame.ClearAllBoxes,
            )
        self.action_menu.add_command(
            label='Help',
            command=self.GUI_Frame.PrintHelp,
            )
        self.action_menu.add_command(
            label='Info',
            command=self.GUI_Frame.PrintInfo,
            )
        self.action_menu.add_command(
            label='Exit',
            command=self.destroy,
            )

        self.menubar.add_cascade(
            label="Action",
            menu=self.action_menu
            )
 
        
        self.functions_menu = tk.Menu(self.menubar, tearoff=False)

        self.constants_menu = tk.Menu(self.functions_menu, tearoff=False)
        self.constants_menu.add_command(
            label='pi',
            command=lambda: self.GUI_Frame.insertFunc('pi'),
            )
        self.constants_menu.add_command(
            label='e',
            command=lambda: self.GUI_Frame.insertFunc('e'),
            )
        self.functions_menu.add_cascade(
            label="Constants",
            menu=self.constants_menu
            )         

        self.trigonometric_menu = tk.Menu(self.functions_menu, tearoff=False)
        self.trigonometric_menu.add_command(
            label='sin',
            command=lambda: self.GUI_Frame.insertFunc('sin('),
            )
        self.trigonometric_menu.add_command(
            label='cos',
            command=lambda: self.GUI_Frame.insertFunc('cos('),
            )
        self.trigonometric_menu.add_command(
            label='tan',
            command=lambda: self.GUI_Frame.insertFunc('tan('),
            )
        self.trigonometric_menu.add_command(
            label='asin',
            command=lambda: self.GUI_Frame.insertFunc('asin('),
            )
        self.trigonometric_menu.add_command(
            label='acos',
            command=lambda: self.GUI_Frame.insertFunc('acos('),
            )
        self.trigonometric_menu.add_command(
            label='atan',
            command=lambda: self.GUI_Frame.insertFunc('atan('),
            )
        self.trigonometric_menu.add_command(
            label='degrees',
            command=lambda: self.GUI_Frame.insertFunc('degrees('),
            )
        self.trigonometric_menu.add_command(
            label='radians',
            command=lambda: self.GUI_Frame.insertFunc('radians('),
            )        
        self.functions_menu.add_cascade(
            label="Trigonometric",
            menu=self.trigonometric_menu
            )        
        
        self.exponential_menu = tk.Menu(self.functions_menu, tearoff=False)
        self.exponential_menu.add_command(
            label='e exponential',
            command=lambda: self.GUI_Frame.insertFunc('exp('),
            )
        self.exponential_menu.add_command(
            label='logarithm',
            command=lambda: self.GUI_Frame.insertFunc('log(x,y)'),
            )
        self.exponential_menu.add_command(
            label='logarithm e',
            command=lambda: self.GUI_Frame.insertFunc('log('),
            )
        self.exponential_menu.add_command(
            label='logarithm 10',
            command=lambda: self.GUI_Frame.insertFunc('log10('),
            )
        self.exponential_menu.add_command(
            label='exponential',
            command=lambda: self.GUI_Frame.insertFunc('pow(x,y)'),
            )      
        self.functions_menu.add_cascade(
            label="Exponential",
            menu=self.exponential_menu
            )           
        
        self.numerical_menu = tk.Menu(self.functions_menu, tearoff=False)
        self.numerical_menu.add_command(
            label='square root',
            command=lambda: self.GUI_Frame.insertFunc('sqrt('),
            )
        self.numerical_menu.add_command(
            label='abs',
            command=lambda: self.GUI_Frame.insertFunc('fabs('),
            )
        self.numerical_menu.add_command(
            label='factorial !',
            command=lambda: self.GUI_Frame.insertFunc('factorial ('),
            )
        self.numerical_menu.add_command(
            label='truncating division',
            command=lambda: self.GUI_Frame.insertFunc('//'),
            )     
        self.functions_menu.add_cascade(
            label="Numerical",
            menu=self.numerical_menu
            )           
                
        self.menubar.add_cascade(
            label="Functions",
            menu=self.functions_menu
            )  


if __name__ == "__main__":
    app = App()
    app.mainloop()
