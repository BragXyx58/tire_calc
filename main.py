import tkinter as tk
from tkinter import messagebox

class TireCalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Шинный калькулятор")
        self.root.geometry("400x350")

        self.create_widgets()

    def create_widgets(self):
        labels = ["Ширина (мм)", "Профиль (%)", "Диаметр (дюймы)"]
        self.old_entries = []
        self.new_entries = []

        tk.Label(self.root, text="Старые шины").grid(row=0, column=1)
        tk.Label(self.root, text="Новые шины").grid(row=0, column=2)

        for i, label in enumerate(labels):
            tk.Label(self.root, text=label).grid(row=i+1, column=0)
            old_entry = tk.Entry(self.root)
            new_entry = tk.Entry(self.root)
            old_entry.grid(row=i+1, column=1)
            new_entry.grid(row=i+1, column=2)
            self.old_entries.append(old_entry)
            self.new_entries.append(new_entry)

        calc_button = tk.Button(self.root, text="Рассчитать", command=self.calculate)
        reset_button = tk.Button(self.root, text="Сбросить", command=self.reset_fields)
        calc_button.grid(row=5, column=0, columnspan=2, pady=10)
        reset_button.grid(row=5, column=2, pady=10)

        self.result_labels = {
            "Диаметр": tk.Label(self.root, text="Результаты будут тут"),
            "Клиренс": tk.Label(self.root, text="Результаты будут тут"),
            "Скорость": tk.Label(self.root, text="Результаты будут тут")
        }

        for i, label in enumerate(self.result_labels.values(), start=6):
            label.grid(row=i, column=0, columnspan=3)

    def calculate(self):
        self.result_labels["Диаметр"].config(text="Разница в диаметре: 10 мм")
        self.result_labels["Клиренс"].config(text="Изменение клиренса: 5 мм")
        self.result_labels["Скорость"].config(text="Отклонение скорости: 3 км/ч")

    def reset_fields(self):
        for entry in self.old_entries + self.new_entries:
            entry.delete(0, tk.END)
        for label in self.result_labels.values():
            label.config(text="Результаты будут тут")


root = tk.Tk()
app = TireCalculatorApp(root)
root.mainloop()
