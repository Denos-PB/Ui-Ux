# speed_converter.py
import tkinter as tk
from tkinter import messagebox

class SpeedConverterApp:
    def __init__(self, root=None):
        self.root = root if root is not None else tk.Tk()
        self.root.title("Конвертер швидкості")
        self.root.resizable(False, False)
        self.bg_color = "#c0c0c0"
        self.root.configure(bg=self.bg_color)
        self.root.geometry("680x360")
        self.units = {
            "m/s": 1.0,
            "km/h": 1000.0 / 3600.0,
            "mph": 1609.344 / 3600.0,
            "knot": 1852.0 / 3600.0,
            "ft/s": 0.3048,
        }
        self.build_ui()

    def build_ui(self):
        container = tk.Frame(self.root, bg=self.bg_color, bd=3, relief="sunken")
        container.pack(padx=16, pady=16, fill="both", expand=True)

        title = tk.Label(container, text="Конвертація між одиницями швидкості",
                         font=("MS Sans Serif", 16, "bold"),
                         bg=self.bg_color, fg="navy")
        title.grid(row=0, column=0, columnspan=4, pady=(0, 14))

        tk.Label(container, text="Значення:", font=("MS Sans Serif", 13),
                 bg=self.bg_color).grid(row=1, column=0, sticky="e", padx=8, pady=6)
        self.val_var = tk.StringVar(value="1")
        tk.Entry(container, textvariable=self.val_var, width=20,
                 font=("MS Sans Serif", 13)).grid(row=1, column=1, padx=8, pady=6, sticky="ew")

        self.from_var = tk.StringVar(value="m/s")
        self.to_var = tk.StringVar(value="km/h")

        tk.Label(container, text="З:", font=("MS Sans Serif", 13),
                 bg=self.bg_color).grid(row=2, column=0, sticky="e", padx=8, pady=6)
        tk.OptionMenu(container, self.from_var, "m/s", "km/h", "mph", "knot", "ft/s").grid(
            row=2, column=1, padx=8, pady=6, sticky="ew")

        tk.Label(container, text="У:", font=("MS Sans Serif", 13),
                 bg=self.bg_color).grid(row=3, column=0, sticky="e", padx=8, pady=6)
        tk.OptionMenu(container, self.to_var, "m/s", "km/h", "mph", "knot", "ft/s").grid(
            row=3, column=1, padx=8, pady=6, sticky="ew")

        self.res_label = tk.Label(
            container,
            text="Результат: -",
            bg=self.bg_color,
            fg="black",
            font=("MS Sans Serif", 13, "bold"),
            width=24  # Increase width to fit full result
        )
        self.res_label.grid(row=1, column=2, columnspan=2, padx=(16, 8), pady=6, sticky="w")

        btns_frame = tk.Frame(container, bg=self.bg_color)
        btns_frame.grid(row=4, column=0, columnspan=4, pady=(14, 0), sticky="ew")
        tk.Button(btns_frame, text="Конвертувати", bg="#0066cc", fg="white",
                  bd=3, relief="raised", font=("MS Sans Serif", 12, "bold"),
                  padx=14, pady=6, command=self.convert).pack(side="left", padx=6)
        tk.Button(btns_frame, text="Поміняти",
                  font=("MS Sans Serif", 12), padx=14, pady=6,
                  command=self.swap_units).pack(side="left", padx=6)
        tk.Button(btns_frame, text="Закрити",
                  font=("MS Sans Serif", 12), padx=14, pady=6,
                  command=self.root.destroy).pack(side="right", padx=6)

    def convert(self):
        try:
            val = float(self.val_var.get())
        except ValueError:
            messagebox.showerror("Помилка", "Введіть коректне число для значення швидкості.")
            return
        u_from = self.from_var.get()
        u_to = self.to_var.get()
        base = val * self.units[u_from]   # в м/с
        out = base / self.units[u_to]     # у цільову одиницю
        self.res_label.config(text=f"Результат: {out:.1f} {u_to}")

    def swap_units(self):
        f = self.from_var.get()
        t = self.to_var.get()
        self.from_var.set(t)
        self.to_var.set(f)
        self.convert()

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    SpeedConverterApp().run()