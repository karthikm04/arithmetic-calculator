# Import the necessary libraries
import tkinter as tk
from tkinter import messagebox

# Create the main window
class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.entry = tk.Entry(self.root, width=36, borderwidth=5)
        self.entry.grid(row=0, column=0, columnspan=4)
        self.create_buttons()

    # Create the buttons
    def create_buttons(self):
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+','%'
        ]

        row_val = 1
        col_val = 0
        # new text
        
        for button in buttons:
            tk.Button(self.root, text=button, width=5, command=lambda button=button: self.click_button(button)).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

        # Create the clear button
        tk.Button(self.root, text="Clear", width=21, command=self.clear_entry).grid(row=row_val, column=0, columnspan=4)

    # Handle button clicks
    def click_button(self, button):
        if button == '=':
            try:
                result = str(eval(self.entry.get()))
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, result)
            except Exception as e:
                messagebox.showerror("Error", str(e))
        else:
            self.entry.insert(tk.END, button)

    # Clear the entry field
    def clear_entry(self):
        self.entry.delete(0, tk.END)

# Run the calculator
if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()