import tkinter as tk
from tkinter import messagebox
import math
import cmath

class QuadraticSolverApp:
    def __init__(self, root=None):
        self.root = root if root is not None else tk.Tk()
        self.root.title("Розв'язувач квадратних рівнянь")
        self.root.resizable(False, False)
        self.bg_color = "#c0c0c0"
        self.root.configure(bg=self.bg_color)
        self.root.geometry("720x420")
        self.build_ui()


    def build_ui(self):
        container = tk.Frame(self.root, bg=self.bg_color, bd=3, relief="sunken")
        container.pack(padx=16, pady=16, fill="both", expand=True)

        title = tk.Label(container, text="ax² + bx + c = 0",
                         font=("MS Sans Serif", 16, "bold"),
                         bg=self.bg_color, fg="navy")
        title.grid(row=0, column=0, columnspan=4, pady=(0, 14))

        tk.Label(container, text="a:", font=("MS Sans Serif", 13),
                 bg=self.bg_color).grid(row=1, column=0, sticky="e", padx=8, pady=6)
        tk.Label(container, text="b:", font=("MS Sans Serif", 13),
                 bg=self.bg_color).grid(row=2, column=0, sticky="e", padx=8, pady=6)
        tk.Label(container, text="c:", font=("MS Sans Serif", 13),
                 bg=self.bg_color).grid(row=3, column=0, sticky="e", padx=8, pady=6)

        self.a_var = tk.StringVar(value="1")
        self.b_var = tk.StringVar(value="0")
        self.c_var = tk.StringVar(value="0")

        tk.Entry(container, textvariable=self.a_var, width=20,
                 font=("MS Sans Serif", 13)).grid(row=1, column=1, padx=8, pady=6, sticky="ew")
        tk.Entry(container, textvariable=self.b_var, width=20,
                 font=("MS Sans Serif", 13)).grid(row=2, column=1, padx=8, pady=6, sticky="ew")
        tk.Entry(container, textvariable=self.c_var, width=20,
                 font=("MS Sans Serif", 13)).grid(row=3, column=1, padx=8, pady=6, sticky="ew")

        self.res_box = tk.Text(container, height=10, width=60, bg="#f5f5f5",
                               font=("Courier New", 12))
        self.res_box.grid(row=1, column=2, rowspan=3, columnspan=2, padx=(16, 8), pady=6, sticky="nsew")
        self.res_box.config(state="disabled")

        container.grid_columnconfigure(2, weight=1)
        container.grid_rowconfigure(1, weight=1)

        btns_frame = tk.Frame(container, bg=self.bg_color)
        btns_frame.grid(row=4, column=0, columnspan=4, pady=(14, 0), sticky="ew")

        tk.Button(btns_frame, text="Розв'язати", bg="#008000", fg="white",
                  bd=3, relief="raised", font=("MS Sans Serif", 12, "bold"),
                  padx=14, pady=6, command=self.solve).pack(side="left", padx=6)
        tk.Button(btns_frame, text="Очистити", bg="#ff6060", fg="white",
                  bd=3, relief="raised", font=("MS Sans Serif", 12, "bold"),
                  padx=14, pady=6, command=self.clear).pack(side="left", padx=6)
        tk.Button(btns_frame, text="Закрити",
                  font=("MS Sans Serif", 12), padx=14, pady=6,
                  command=self.root.destroy).pack(side="right", padx=6)

    def show_result(self, text):
        self.res_box.config(state="normal")
        self.res_box.delete("1.0", "end")
        self.res_box.insert("end", text)
        self.res_box.config(state="disabled")

    def clear(self):
        self.a_var.set("1")
        self.b_var.set("0")
        self.c_var.set("0")
        self.show_result("")

    def solve(self):
        try:
            a = float(self.a_var.get())
            b = float(self.b_var.get())
            c = float(self.c_var.get())
        except ValueError:
            messagebox.showerror("Помилка", "Введіть коректні числа для a, b, c.")
            return

        if a == 0:
            if b == 0:
                self.show_result("Безліч розв'язків" if c == 0 else "Розв'язків немає")
            else:
                x = -c / b
                self.show_result(f"Лінійне рівняння: x = {x:.10g}")
            return

        D = b * b - 4 * a * c
        if D > 0:
            sqrtD = math.sqrt(D)
            x1 = (-b + sqrtD) / (2 * a)
            x2 = (-b - sqrtD) / (2 * a)
            self.show_result(f"D = {D:.10g} (> 0)\n"
                             f"x₁ = {x1:.10g}\n"
                             f"x₂ = {x2:.10g}")
        elif D == 0:
            x = -b / (2 * a)
            self.show_result(f"D = 0\nx = {x:.10g}")
        else:
            sqrtD = cmath.sqrt(D)
            x1 = (-b + sqrtD) / (2 * a)
            x2 = (-b - sqrtD) / (2 * a)
            self.show_result(f"D = {D:.10g} (< 0)\n"
                             f"x₁ = {x1.real:.10g} + {x1.imag:.10g}i\n"
                             f"x₂ = {x2.real:.10g} + {x2.imag:.10g}i")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    QuadraticSolverApp().run()