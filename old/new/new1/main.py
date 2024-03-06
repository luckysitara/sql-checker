import tkinter as tk
from gui import SQLGradingGUI

def main():
    root = tk.Tk()
    root.title("SQL Grading System")

    app = SQLGradingGUI(root)
    app.pack()

    root.mainloop()

if __name__ == "__main__":
    main()

