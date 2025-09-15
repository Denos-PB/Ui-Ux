import tkinter as tk
from tkinter import messagebox
import math

class RetroCalculator:
    def __init__(self, root=None):
        self.root = root if root is not None else tk.Tk()
        self.root.title("Calculator 95")
        self.root.geometry("320x480")
        self.root.resizable(False, False)
        self.bg_color = "#c0c0c0"
        self.display_bg = "#000080"
        self.display_fg = "#00ff00"
        self.button_bg = "#c0c0c0"
        self.button_active_bg = "#808080"
        self.operator_bg = "#ff8000"
        self.root.configure(bg=self.bg_color)

        self.current_input = "0"
        self.previous_input = ""
        self.operator = ""
        self.result = 0
        self.new_number = True

        self.setup_ui()


    def setup_ui(self):
        main_frame = tk.Frame(self.root, bg=self.bg_color, relief="raised", bd=3)
        main_frame.pack(fill="both", expand=True, padx=10, pady=10)

        title_frame = tk.Frame(main_frame, bg=self.bg_color, relief="sunken", bd=2)
        title_frame.pack(fill="x", pady=(0, 10))
        title_label = tk.Label(title_frame, text="Calculator 95",
                              font=("MS Sans Serif", 12, "bold"),
                              bg=self.bg_color, fg="navy")
        title_label.pack(pady=5)

        display_frame = tk.Frame(main_frame, bg="black", relief="sunken", bd=3)
        display_frame.pack(fill="x", pady=(0, 10))
        self.display = tk.Label(display_frame, text="0",
                               font=("Courier New", 18, "bold"),
                               bg=self.display_bg, fg=self.display_fg,
                               anchor="e", padx=10, pady=10)
        self.display.pack(fill="both", expand=True)

        # Кнопки
        button_frame = tk.Frame(main_frame, bg=self.bg_color)
        button_frame.pack(fill="both", expand=True)
        buttons = [
            ['C', 'CE', '√', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['±', '0', '.', '=']
        ]
        for i, row in enumerate(buttons):
            for j, text in enumerate(row):
                self.create_button(button_frame, text, i, j)

    def create_button(self, parent, text, row, col):
        if text in ['/', '*', '-', '+', '=']:
            bg_color = self.operator_bg
            fg_color = "white"
        elif text in ['C', 'CE', '√', '±']:
            bg_color = "#ff6060"
            fg_color = "white"
        else:
            bg_color = self.button_bg
            fg_color = "black"
        button = tk.Button(parent, text=text,
                          font=("MS Sans Serif", 12, "bold"),
                          width=5, height=2,
                          bg=bg_color, fg=fg_color,
                          activebackground=self.button_active_bg,
                          relief="raised", bd=3,
                          command=lambda t=text: self.button_click(t))
        button.grid(row=row, column=col, sticky="nsew", padx=2, pady=2)
        parent.grid_rowconfigure(row, weight=1)
        parent.grid_columnconfigure(col, weight=1)

    def button_click(self, value):
        try:
            if value.isdigit():
                self.number_click(value)
            elif value == '.':
                self.decimal_click()
            elif value in ['+', '-', '*', '/']:
                self.operator_click(value)
            elif value == '=':
                self.equals_click()
            elif value == 'C':
                self.clear_all()
            elif value == 'CE':
                self.clear_entry()
            elif value == '√':
                self.sqrt_click()
            elif value == '±':
                self.plus_minus_click()
        except Exception as e:
            messagebox.showerror("Ошибка", "Ошибка в вычислениях!")
            self.clear_all()

    def number_click(self, num):
        if self.new_number:
            self.current_input = num
            self.new_number = False
        else:
            if self.current_input == "0":
                self.current_input = num
            else:
                self.current_input += num
        self.update_display()

    def decimal_click(self):
        if '.' not in self.current_input:
            if self.new_number:
                self.current_input = "0."
                self.new_number = False
            else:
                self.current_input += "."
            self.update_display()

    def operator_click(self, op):
        if self.operator and not self.new_number:
            self.equals_click()
        self.previous_input = self.current_input
        self.operator = op
        self.new_number = True

    def equals_click(self):
        if self.operator and self.previous_input:
            try:
                prev = float(self.previous_input)
                curr = float(self.current_input)
                if self.operator == '+':
                    result = prev + curr
                elif self.operator == '-':
                    result = prev - curr
                elif self.operator == '*':
                    result = prev * curr
                elif self.operator == '/':
                    if curr == 0:
                        messagebox.showerror("Ошибка", "Деление на ноль!")
                        self.clear_all()
                        return
                    result = prev / curr
                if result == int(result):
                    self.current_input = str(int(result))
                else:
                    self.current_input = f"{result:.10g}"
                self.operator = ""
                self.previous_input = ""
                self.new_number = True
                self.update_display()
            except Exception:
                messagebox.showerror("Ошибка", "Ошибка в вычислениях!")
                self.clear_all()

    def clear_all(self):
        self.current_input = "0"
        self.previous_input = ""
        self.operator = ""
        self.new_number = True
        self.update_display()

    def clear_entry(self):
        self.current_input = "0"
        self.new_number = True
        self.update_display()

    def sqrt_click(self):
        try:
            num = float(self.current_input)
            if num < 0:
                messagebox.showerror("Ошибка", "Корень из отрицательного числа!")
                return
            result = math.sqrt(num)
            if result == int(result):
                self.current_input = str(int(result))
            else:
                self.current_input = f"{result:.10g}"
            self.new_number = True
            self.update_display()
        except Exception:
            messagebox.showerror("Ошибка", "Ошибка в вычислениях!")

    def plus_minus_click(self):
        if self.current_input != "0":
            if self.current_input.startswith("-"):
                self.current_input = self.current_input[1:]
            else:
                self.current_input = "-" + self.current_input
            self.update_display()

    def update_display(self):
        display_text = self.current_input
        if len(display_text) > 15:
            try:
                num = float(display_text)
                display_text = f"{num:.6e}"
            except:
                display_text = display_text[:15]
        self.display.config(text=display_text)

    def run(self):
        try:
            self.root.iconname("Calculator")
        except:
            pass
        self.root.bind('<Key>', self.key_press)
        self.root.focus_set()
        self.root.mainloop()

    def key_press(self, event):
        key = event.char
        if key.isdigit():
            self.button_click(key)
        elif key in ['+', '-', '*', '/']:
            self.button_click(key)
        elif key in ['.', ',']:
            self.button_click('.')
        elif key in ['\r', '\n', '=']:
            self.button_click('=')
        elif key == '\x08':  # Backspace
            self.button_click('CE')
        elif key == '\x1b':  # Escape
            self.button_click('C')

if __name__ == "__main__":
    calculator = RetroCalculator()
    calculator.run()