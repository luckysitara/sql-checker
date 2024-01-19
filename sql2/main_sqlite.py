#!/usr/bin/python3
from tkinter import Tk
from SQLiteGraderApp import SQLiteGraderApp

def main():
    root = Tk()
    app = SQLiteGraderApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

