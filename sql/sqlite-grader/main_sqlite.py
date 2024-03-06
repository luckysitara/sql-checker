#!/usr/bin/python3
import tkinter
from tkinter import tkk
from SQLiteGraderApp import SQLiteGraderApp

# Create Tkinter root window
root = tk.Tk()

# Create SQLiteGraderApp instance
app = SQLiteGraderApp(root)

# Run the app
app.run()

