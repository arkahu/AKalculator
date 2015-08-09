# -*- coding: cp1252 -*-

"""
--AKalculator--
version 1.1 
"Advanded Kalculator"?

This program is a simple function calculator.
Created by: Arttu Huttunen, Oulu, Finland <arttuhut@gmail.com>
Created: August 2011

Copyright (C) 2011 by Arttu Huttunen 
Published under MIT-license. Anyone is free to do anything they want with
the software or the source code and it comes with absolutely no warranty
of any kind.

This is a PyQt graphical frontend for Python's math functions.
Created with Python version 2.6.5 and PyQt4 4.5.4 in Python(x,y)-package.

You need Python and PyQt on your machine to run this. 
"""

#import division to have fractional division by default
from __future__ import division

#required modules, math is imported so that the user can use
#the math commands directly
import sys
from functools import partial
import cmath
from math import *
from PyQt4.QtCore import *
from PyQt4.QtGui import *

#Main window
class CalculatorGUI(QMainWindow):
    
    def __init__(self, parent=None):
        super (CalculatorGUI,self).__init__(parent)
        
        self.setWindowTitle("AKalculator")
        
        #Add statusbar for tooltips
        self.statusBar()
        
        #Create Menus  ----------------------------------------------------
        #Menu items first
        self.quitAction = QAction( 'Quit', self)
        self.helpAction = QAction( 'Help', self)
        self.infoAction = QAction( 'Info', self)
        self.clearAction = QAction( 'Clear All', self)
        self.dotAction = QAction ('Commas to dots', self)
        
        self.dotAction.setCheckable(True)
        
        #Mathematical funtions to "functions"-menu
        self.piAction = QAction ('pi', self)
        self.eAction = QAction ('e', self)
        
        self.sinAction = QAction( 'sin', self)
        self.cosAction = QAction( 'cos', self)
        self.tanAction = QAction( 'tan', self)
        self.asinAction = QAction( 'asin', self)
        self.acosAction = QAction( 'acos', self)
        self.atanAction = QAction( 'atan', self)
        self.degAction = QAction( 'degree', self)
        self.radAction = QAction( 'radian', self)
        
        self.expAction = QAction ('e exponential', self)
        self.logAction = QAction ('logarithm', self)
        self.logeAction = QAction ('logarithm e', self)
        self.log10Action = QAction ('logarithm 10', self)
        self.powAction = QAction ('exponential', self)
        self.sqrtAction = QAction ('SquareRoot', self)
        
        self.absAction = QAction ('abs', self)
        self.factorialAction = QAction ('factorial', self)


        #Create the menu-object
        menubar = self.menuBar()
        #'menu'-menu
        menuMenu = menubar.addMenu('Menu')
        menuMenu.addAction(self.dotAction)
        menuMenu.addAction(self.clearAction)
        menuMenu.addAction(self.helpAction)
        menuMenu.addAction(self.infoAction)
        menuMenu.addAction(self.quitAction)

        #'function'-menu
        functionMenu = menubar.addMenu('Functions')
        
        constants = functionMenu.addMenu('Constants')
        constants.addAction(self.piAction)
        constants.addAction(self.eAction)
        
        trigonometric = functionMenu.addMenu('Trigonometric')
        trigonometric.addAction(self.sinAction)
        trigonometric.addAction(self.cosAction)
        trigonometric.addAction(self.tanAction)
        trigonometric.addAction(self.asinAction)
        trigonometric.addAction(self.acosAction)
        trigonometric.addAction(self.atanAction)
        trigonometric.addAction(self.degAction)
        trigonometric.addAction(self.radAction)
        
        exponential = functionMenu.addMenu('Exponential')
        exponential.addAction(self.expAction)
        exponential.addAction(self.logAction)
        exponential.addAction(self.logeAction)
        exponential.addAction(self.log10Action)
        exponential.addAction(self.powAction)
        exponential.addAction(self.sqrtAction)
        
        numerical = functionMenu.addMenu('Numerical')
        numerical.addAction(self.absAction)
        numerical.addAction(self.factorialAction)
        
        #Calculator widgets (input, output, buttons...)----------------------
        
        #Create the output and input widgets
        self.outputBox = QTextBrowser()
        self.inputBox = QLineEdit("Type expression and press enter")
        
        self.inputBox.selectAll()
        
        #Calculate, backspace and clear buttons
        self.buttonCalculate = QPushButton("CALCULATE")
        self.buttonBackspace = QPushButton("Backspace")
        self.buttonClear = QPushButton("CLEAR")
        
        #Number buttons
        self.button1 = QPushButton("1")
        self.button2 = QPushButton("2")
        self.button3 = QPushButton("3")
        self.button4 = QPushButton("4")
        self.button5 = QPushButton("5")
        self.button6 = QPushButton("6")
        self.button7 = QPushButton("7")
        self.button8 = QPushButton("8")
        self.button9 = QPushButton("9")
        self.button0 = QPushButton("0")
        self.buttonDot = QPushButton(".")
        
        #special math buttons
        self.buttonParenthesisOpen = QPushButton ("(")
        self.buttonParenthesisClosed = QPushButton (")")
        self.buttonModulo = QPushButton ("Modulo")

        #Functionbuttons
        self.buttonPlus = QPushButton("+")
        self.buttonMinus = QPushButton("-")
        self.buttonMultip = QPushButton("X")
        self.buttonDivision = QPushButton("/")
        
        self.buttonPower = QPushButton ("x^y")
        self.buttonSqrt = QPushButton ("SQRT")

        
        #Button Statustips, collected here because they make ugly lines
        self.quitAction.setStatusTip('Exit application')
        self.helpAction.setStatusTip("Print help")
        self.infoAction.setStatusTip("Print Application info")
        self.clearAction.setStatusTip("Clear input and output")
        self.dotAction.setStatusTip("If checked, convert commas to dots "
        "during calculation")
        
        self.outputBox.setStatusTip("Result of the calculations are "
        "displayed here")
        self.inputBox.setStatusTip('Enter mathematical expressions here')
        self.buttonCalculate.setStatusTip("Click this to calculate "
        "the given input (or press enter)" )
        self.buttonBackspace.setStatusTip('Remove one character from input')
        self.buttonClear.setStatusTip('Remove all characters from input')
        self.buttonDivision.setStatusTip("Fractional division, use // for "
        "truncating division")
        self.buttonPower.setStatusTip("x raised to power y, other option is "
        "pow(x,y)")
        self.buttonSqrt.setStatusTip("Square root")
        self.buttonModulo.setStatusTip("Modulo operation, remainder of a "
        "division (%)")

        #Function menu status tips
        self.piAction.setStatusTip("Pi = 3.141592... to available precision")
        self.eAction.setStatusTip("e = 2.718281... to available precision")
        
        self.sinAction.setStatusTip("Sine")
        self.cosAction.setStatusTip("Cosine")
        self.tanAction.setStatusTip("Tangent")
        self.asinAction.setStatusTip("Arc sine")
        self.acosAction.setStatusTip("Arc cosine")
        self.atanAction.setStatusTip("Arc tangent")
        self.degAction.setStatusTip("Convert radians to degrees")
        self.radAction.setStatusTip("Convert degrees to radians")
        
        self.expAction.setStatusTip("e to power x")
        self.logAction.setStatusTip("General logartithm by log(x,base)")
        self.logeAction.setStatusTip("e based logartithm by log(x)")
        self.log10Action.setStatusTip("10 based logarithm")
        self.powAction.setStatusTip("pow(x,y), x raised to power y, other "
        "option is **")
        self.sqrtAction.setStatusTip("Square root")
        
        self.absAction.setStatusTip("Absolute value")
        self.factorialAction.setStatusTip("Factorial, n!")
        
        
        #-------Set layout----------------------------------------------------
        #First create groups of buttons then add them to layout

        #Group buttons into one row
        rowThree = QHBoxLayout()
        rowThree.addWidget(self.buttonBackspace)
        rowThree.addWidget(self.buttonClear)
        
        rowFour = QHBoxLayout()
        rowFour.addWidget(self.button7)
        rowFour.addWidget(self.button8)
        rowFour.addWidget(self.button9)

        rowFour.addWidget(self.buttonParenthesisOpen)
        rowFour.addWidget(self.buttonParenthesisClosed)
        
        rowFive = QHBoxLayout()
        rowFive.addWidget(self.button4)
        rowFive.addWidget(self.button5)
        rowFive.addWidget(self.button6)
        rowFive.addWidget(self.buttonPlus)
        rowFive.addWidget(self.buttonMultip)
        
        rowSix = QHBoxLayout()
        rowSix.addWidget(self.button1)
        rowSix.addWidget(self.button2)
        rowSix.addWidget(self.button3)
        rowSix.addWidget(self.buttonMinus)
        rowSix.addWidget(self.buttonDivision)
        
        rowSeven = QHBoxLayout()
        rowSeven.addWidget(self.button0)
        rowSeven.addWidget(self.buttonDot)
        rowSeven.addWidget(self.buttonModulo)
        rowSeven.addWidget(self.buttonPower)
        rowSeven.addWidget(self.buttonSqrt)


        #Create the layout        
        #Input and output widgets and calculate&clear buttons
        self.grid = QGridLayout()
        self.grid.addWidget(self.outputBox, 0, 0)
        self.grid.addWidget(self.inputBox, 1, 0)
        self.grid.addWidget(self.buttonCalculate, 2, 0)
        
        #Rows are inserted here
        self.grid.addLayout(rowThree, 3, 0)
        self.grid.addLayout(rowFour, 4, 0)
        self.grid.addLayout(rowFive, 5, 0)
        self.grid.addLayout(rowSix, 6, 0)
        self.grid.addLayout(rowSeven, 7, 0)
        
        
        #Create widget from layout and set it as CentralWidget
        self.gridWidget = QWidget()
        self.gridWidget.setLayout(self.grid)
        self.setCentralWidget(self.gridWidget)
        
        self.inputBox.setFocus()
        
        
        
        """ -----------------------------------------------------------------
        #Button functionality is implemented here by connecting the signals
        #Most signals are wrapped with "partial" so that the name of the
        #button can be sent to the receiving function
        """
        
        #Menu item signals:
        #Menu-menu
        self.connect(self.quitAction, SIGNAL('triggered()'), SLOT('close()'))
        self.connect(self.helpAction, SIGNAL('triggered()'), self.PrintHelp)
        self.connect(self.infoAction, SIGNAL('triggered()'), self.PrintInfo)
        self.connect(self.clearAction, SIGNAL('triggered()'), self.ClearAllBoxes)
        
        #Functions-menu  ----------------------------------------
        self.piActionWrap = partial(self.FunctionInsert, "pi")
        self.connect(self.piAction, SIGNAL('triggered()'), 
                     self.piActionWrap)
        
        self.eActionWrap = partial(self.FunctionInsert, "e")
        self.connect(self.eAction, SIGNAL('triggered()'), 
                     self.eActionWrap)
        
        self.sinActionWrap = partial(self.FunctionInsert, "sin (")
        self.connect(self.sinAction, SIGNAL('triggered()'), 
                     self.sinActionWrap)
        
        self.cosActionWrap = partial(self.FunctionInsert, "cos (")
        self.connect(self.cosAction, SIGNAL('triggered()'), 
                     self.cosActionWrap)
        
        self.tanActionWrap = partial(self.FunctionInsert, "tan (")
        self.connect(self.tanAction, SIGNAL('triggered()'), 
                     self.tanActionWrap)
        
        self.asinActionWrap = partial(self.FunctionInsert, "asin (")
        self.connect(self.asinAction, SIGNAL('triggered()'), 
                     self.asinActionWrap)
        
        self.acosActionWrap = partial(self.FunctionInsert, "acos (")
        self.connect(self.acosAction, SIGNAL('triggered()'), 
                     self.acosActionWrap)
        
        self.atanActionWrap = partial(self.FunctionInsert, "atan (")
        self.connect(self.atanAction, SIGNAL('triggered()'), 
                     self.atanActionWrap)
                     
        self.degActionWrap = partial(self.FunctionInsert, "degrees (")
        self.connect(self.degAction, SIGNAL('triggered()'), 
                     self.degActionWrap)
        
        self.radActionWrap = partial(self.FunctionInsert, "radians (")
        self.connect(self.radAction, SIGNAL('triggered()'), 
                     self.radActionWrap)
        
        self.expActionWrap = partial(self.FunctionInsert, "exp (")
        self.connect(self.expAction, SIGNAL('triggered()'), 
                     self.expActionWrap)
        
        self.logActionWrap = partial(self.FunctionInsert, "log (x,y)")
        self.connect(self.logAction, SIGNAL('triggered()'), 
                     self.logActionWrap)
        
        self.logeActionWrap = partial(self.FunctionInsert, "log (")
        self.connect(self.logeAction, SIGNAL('triggered()'), 
                     self.logeActionWrap)
        
        self.log10ActionWrap = partial(self.FunctionInsert, "log10 (")
        self.connect(self.log10Action, SIGNAL('triggered()'), 
                     self.log10ActionWrap)
        
        self.powActionWrap = partial(self.FunctionInsert, "pow (x,y)")
        self.connect(self.powAction, SIGNAL('triggered()'), 
                     self.powActionWrap)
        
        self.sqrtActionWrap = partial(self.FunctionInsert, "sqrt (")
        self.connect(self.sqrtAction, SIGNAL('triggered()'), 
                     self.sqrtActionWrap)
        
        
        self.absActionWrap = partial(self.FunctionInsert, "fabs (")
        self.connect(self.absAction, SIGNAL('triggered()'), 
                     self.absActionWrap)
        
        self.factorialActionWrap = partial(self.FunctionInsert, "factorial (")
        self.connect(self.factorialAction, SIGNAL('triggered()'), 
                     self.factorialActionWrap)
        
        #-----------------------------------------------------------------
        #Pressing return is same as clicking "calculate"
        self.connect(self.inputBox, SIGNAL("returnPressed()"),
                     self.Calculate)
        
        #Button signals:
        self.connect(self.buttonCalculate, SIGNAL("clicked()"),
                     self.Calculate)            
        
        self.buttonClearWrap = partial(self.ButtonFunctions, "clear")
        self.connect(self.buttonClear, SIGNAL("clicked()"), 
                     self.buttonClearWrap)

        self.buttonBackspaceWrap = partial(self.ButtonFunctions, "backspace")
        self.connect(self.buttonBackspace, SIGNAL("clicked()"), 
                     self.buttonBackspaceWrap)
                     
        self.buttonPlusWrap = partial(self.FunctionInsert, "+")
        self.connect(self.buttonPlus, SIGNAL("clicked()"), 
                     self.buttonPlusWrap)
        
        self.buttonMinusWrap = partial(self.FunctionInsert, "-")
        self.connect(self.buttonMinus, SIGNAL("clicked()"), 
                     self.buttonMinusWrap)
        
        self.buttonMultipWrap = partial(self.FunctionInsert, "*")
        self.connect(self.buttonMultip, SIGNAL("clicked()"), 
                     self.buttonMultipWrap)
        
        self.buttonDivisionWrap = partial(self.FunctionInsert, "/")
        self.connect(self.buttonDivision, SIGNAL("clicked()"), 
                     self.buttonDivisionWrap)

        self.button1Wrap = partial(self.FunctionInsert, "1")
        self.connect(self.button1, SIGNAL("clicked()"), 
                     self.button1Wrap)

        self.button2Wrap = partial(self.FunctionInsert, "2")
        self.connect(self.button2, SIGNAL("clicked()"), 
                     self.button2Wrap)

        self.button3Wrap = partial(self.FunctionInsert, "3")
        self.connect(self.button3, SIGNAL("clicked()"), 
                     self.button3Wrap)

        self.button4Wrap = partial(self.FunctionInsert, "4")
        self.connect(self.button4, SIGNAL("clicked()"), 
                     self.button4Wrap)

        self.button5Wrap = partial(self.FunctionInsert, "5")
        self.connect(self.button5, SIGNAL("clicked()"), 
                     self.button5Wrap)

        self.button6Wrap = partial(self.FunctionInsert, "6")
        self.connect(self.button6, SIGNAL("clicked()"), 
                     self.button6Wrap)

        self.button7Wrap = partial(self.FunctionInsert, "7")
        self.connect(self.button7, SIGNAL("clicked()"), 
                     self.button7Wrap)

        self.button8Wrap = partial(self.FunctionInsert, "8")
        self.connect(self.button8, SIGNAL("clicked()"), 
                     self.button8Wrap)

        self.button9Wrap = partial(self.FunctionInsert, "9")
        self.connect(self.button9, SIGNAL("clicked()"), 
                     self.button9Wrap)

        self.button0Wrap = partial(self.FunctionInsert, "0")
        self.connect(self.button0, SIGNAL("clicked()"), 
                     self.button0Wrap)

        self.buttonDotWrap = partial(self.FunctionInsert, ".")
        self.connect(self.buttonDot, SIGNAL("clicked()"), 
                     self.buttonDotWrap)

        self.buttonModuloWrap = partial(self.FunctionInsert, "%")
        self.connect(self.buttonModulo, SIGNAL("clicked()"), 
                     self.buttonModuloWrap)

        self.buttonPOWrap = partial(self.FunctionInsert, "(")
        self.connect(self.buttonParenthesisOpen, SIGNAL("clicked()"), 
                     self.buttonPOWrap)

        self.buttonPCWrap = partial(self.FunctionInsert, ")")
        self.connect(self.buttonParenthesisClosed, SIGNAL("clicked()"), 
                     self.buttonPCWrap)

        self.buttonPowerWrap = partial(self.FunctionInsert, "**")
        self.connect(self.buttonPower, SIGNAL("clicked()"), 
                     self.buttonPowerWrap)

        self.buttonSqrtWrap = partial(self.FunctionInsert, "sqrt (")
        self.connect(self.buttonSqrt, SIGNAL("clicked()"), 
                     self.buttonSqrtWrap)



    #For text inserting buttons, simply insert buttonName to inputline
    def FunctionInsert (self, buttonName):
        self.inputBox.insert(buttonName)
        self.inputBox.setFocus()

    #For clear and backspace buttons, select the desired action
    def ButtonFunctions(self, buttonName):
        if buttonName == "clear": 
            self.inputBox.setText("")
        elif buttonName == "backspace":
            self.inputBox.backspace()
        self.inputBox.setFocus()
    
    #Read input, calculate write output
    def Calculate(self):
        try:
            inputText = unicode(self.inputBox.text())
            if self.dotAction.isChecked():
                inputText = inputText.replace(',','.')
            
            self.outputBox.append("%s = %s" % (inputText,eval(inputText)))
        except:
            self.outputBox.append("ERROR")
 
    #Clear all boxes menu command function
    def ClearAllBoxes(self):
        self.inputBox.setText("")
        self.outputBox.setText("")
    
    #Prints help to ouput
    def PrintHelp(self):
        self.outputBox.append("""\nAKalculator Usage instructions: \n
Example: sqrt(9) [click calculate]
This application uses Python's built in mathematical functions for 
calculations (math-module). You can type in an expression into the
'input'-line and it will be evaluated with the 'eval()' method.
Therefore it is possible to use math functions not listed in the 
functions-menu (boolean, hexadecimals...).
NOTE: Radians always assumed, convert rads-degs when necessary.
NOTE: For complex math, use cmath.function [e.g. cmath.polar(1+1j)]
NOTE: Use dots for decimal point, comma creates a list.\n""")
        
    def PrintInfo(self):
        self.outputBox.append('''
AKalculator \nVersion: 1.1 \nCreated by: 
Arttu Huttunen, (Oulu, Finland, 2011)
Copyright (C) 2011 by Arttu Huttunen
This software is distributed under MIT-license. Therefore it is free and
open source software.\n''')


#And start the application -------------------------------------------------
app =QApplication(sys.argv)
form = CalculatorGUI()
form.show()
app.exec_()