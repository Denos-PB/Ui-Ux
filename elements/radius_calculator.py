import tkinter as tk
import math


class RadiusCalculator:
    def __init__(self, root=None):
        # allow creating without passing a root: create one when None
        if root is None:
            self.root = tk.Tk()
            self._owns_root = True
        else:
            self.root = root
            self._owns_root = False
        self.root.title("Radius Calculator")
        self.root.geometry("600x400")
        self.root.resizable(False, False)
        self.bg_color = "#c0c0c0"
        self.root.configure(bg=self.bg_color)

        main_frame = tk.Frame(self.root, bg=self.bg_color)
        main_frame.pack(fill="both", expand=True)

        left_frame = tk.Frame(main_frame, bg=self.bg_color, width=200)
        left_frame.pack(side="left", fill="y", padx=10, pady=10)

        tk.Label(left_frame, text="Choose option:", font=("MS Sans Serif", 12, "bold"),
                 bg=self.bg_color).pack(pady=10)

        tk.Button(left_frame, text="Radius from Circumference",
                  font=("MS Sans Serif", 11), width=25, height=2,
                  bg="#835ca3", fg="white",
                  command=self.show_radius_from_circumference).pack(pady=5)

        tk.Button(left_frame, text="Radius from Area",
                  font=("MS Sans Serif", 11), width=25, height=2,
                  bg="#835ca3", fg="white",
                  command=self.show_radius_from_area).pack(pady=5)

        tk.Button(left_frame, text="Radius of Sphere",
                  font=("MS Sans Serif", 11), width=25, height=2,
                  bg="#835ca3", fg="white",
                  command=self.show_radius_of_sphere).pack(pady=5)

        tk.Button(left_frame, text="Radius of Cylinder",
                  font=("MS Sans Serif", 11), width=25, height=2,
                  bg="#835ca3", fg="white",
                  command=self.show_radius_of_cylinder).pack(pady=5)

        self.right_frame = tk.Frame(main_frame, bg="#e0e0e0")
        self.right_frame.pack(side="right", fill="both", expand=True, padx=10, pady=10)

        self.result_label = tk.Label(self.right_frame, text="Select option on the left",
                                     font=("MS Sans Serif", 13, "bold"),
                                     bg="#e0e0e0", fg="black")
        self.result_label.pack(pady=20)

    def clear_right_frame(self):
        for widget in self.right_frame.winfo_children():
            widget.destroy()

    def show_radius_from_circumference(self):
        self.clear_right_frame()
        tk.Label(self.right_frame, text="Enter circumference C:",
                 font=("MS Sans Serif", 12), bg="#e0e0e0").pack(pady=10)
        entry = tk.Entry(self.right_frame, font=("MS Sans Serif", 12))
        entry.pack(pady=5)

        def calculate():
            try:
                C = float(entry.get())
                if C <= 0:
                    raise ValueError("Circumference must be positive")
                r = C / (2 * math.pi)
                self.show_result(r)
            except (ValueError, TypeError):
                self.show_error()

        tk.Button(self.right_frame, text="Calculate", font=("MS Sans Serif", 12),
                  bg="#835ca3", fg="white", command=calculate).pack(pady=10)

    def show_radius_from_area(self):
        self.clear_right_frame()
        tk.Label(self.right_frame, text="Enter area S:",
                 font=("MS Sans Serif", 12), bg="#e0e0e0").pack(pady=10)
        entry = tk.Entry(self.right_frame, font=("MS Sans Serif", 12))
        entry.pack(pady=5)

        def calculate():
            try:
                S = float(entry.get())
                if S <= 0:
                    raise ValueError("Area must be positive")
                r = math.sqrt(S / math.pi)
                self.show_result(r)
            except (ValueError, TypeError):
                self.show_error()

        tk.Button(self.right_frame, text="Calculate", font=("MS Sans Serif", 12),
                  bg="#835ca3", fg="white", command=calculate).pack(pady=10)

    def show_radius_of_sphere(self):
        self.clear_right_frame()
        tk.Label(self.right_frame, text="Enter volume V:",
                 font=("MS Sans Serif", 12), bg="#e0e0e0").pack(pady=10)
        entry = tk.Entry(self.right_frame, font=("MS Sans Serif", 12))
        entry.pack(pady=5)

        def calculate():
            try:
                V = float(entry.get())
                if V <= 0:
                    raise ValueError("Volume must be positive")
                r = ((3 * V) / (4 * math.pi)) ** (1 / 3)
                self.show_result(r)
            except (ValueError, TypeError):
                self.show_error()

        tk.Button(self.right_frame, text="Calculate", font=("MS Sans Serif", 12),
                  bg="#835ca3", fg="white", command=calculate).pack(pady=10)

    def show_radius_of_cylinder(self):
        self.clear_right_frame()
        tk.Label(self.right_frame, text="Enter volume V:",
                 font=("MS Sans Serif", 12), bg="#e0e0e0").pack(pady=10)
        entry_v = tk.Entry(self.right_frame, font=("MS Sans Serif", 12))
        entry_v.pack(pady=5)

        tk.Label(self.right_frame, text="Enter height h:",
                 font=("MS Sans Serif", 12), bg="#e0e0e0").pack(pady=10)
        entry_h = tk.Entry(self.right_frame, font=("MS Sans Serif", 12))
        entry_h.pack(pady=5)

        def calculate():
            try:
                V = float(entry_v.get())
                h = float(entry_h.get())
                if V <= 0 or h <= 0:
                    raise ValueError("Volume and height must be positive")
                r = math.sqrt(V / (math.pi * h))
                self.show_result(r)
            except (ValueError, TypeError, ZeroDivisionError):
                self.show_error()

        tk.Button(self.right_frame, text="Calculate", font=("MS Sans Serif", 12),
                  bg="#835ca3", fg="white", command=calculate).pack(pady=10)

    def show_result(self, r):
        self.clear_right_frame()
        tk.Label(self.right_frame, text=f"Result: r = {r:.4f}",
                 font=("MS Sans Serif", 14, "bold"),
                 bg="#e0e0e0", fg="black").pack(pady=15)

    def show_error(self):
        self.clear_right_frame()
        tk.Label(self.right_frame, text="Invalid input!",
                 font=("MS Sans Serif", 12, "bold"),
                 bg="#e0e0e0", fg="red").pack(pady=15)