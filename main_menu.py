import tkinter as tk
from elements.calculator95 import RetroCalculator
from elements.quadratic_solver import QuadraticSolverApp
from elements.speed_converter import SpeedConverterApp

class MainMenu:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Айтішники")
        self.root.geometry("400x420")
        self.root.resizable(False, False)
        self.bg_color = "#c0c0c0"
        self.root.configure(bg=self.bg_color)

        title = tk.Label(self.root, text="Айтішники",
                         font=("MS Sans Serif", 16, "bold"),
                         bg=self.bg_color, fg="navy")
        title.pack(pady=(24, 16))

        btn_frame = tk.Frame(self.root, bg=self.bg_color)
        btn_frame.pack(pady=16)

        tk.Button(btn_frame, text="Calculator 95", font=("MS Sans Serif", 13, "bold"),
                  width=22, height=2, bg="#0066cc", fg="white",
                  command=self.open_calculator).pack(pady=8)
        tk.Button(btn_frame, text="Quadratic Solver", font=("MS Sans Serif", 13, "bold"),
                  width=22, height=2, bg="#008000", fg="white",
                  command=self.open_quadratic_solver).pack(pady=8)
        tk.Button(btn_frame, text="Speed Converter", font=("MS Sans Serif", 13, "bold"),
                  width=22, height=2, bg="#ff8000", fg="white",
                  command=self.open_speed_converter).pack(pady=8)

        tk.Button(self.root, text="Exit", font=("MS Sans Serif", 12),
                  width=10, bg="#ff6060", fg="white",
                  command=self.root.destroy).pack(pady=(16, 0))

    def open_calculator(self):
        win = tk.Toplevel(self.root)
        RetroCalculator(root=win)

    def open_quadratic_solver(self):
        win = tk.Toplevel(self.root)
        QuadraticSolverApp(root=win)

    def open_speed_converter(self):
        win = tk.Toplevel(self.root)
        SpeedConverterApp(root=win)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    MainMenu().run()
