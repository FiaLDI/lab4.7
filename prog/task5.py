#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk

def main():
    def update_label():
        """Обновляет текст метки в зависимости от выбранной радиокнопки."""
        name = selected_option.get()
        if name == 'Вася':
            label.config(text=f"+ 7 (985) 423-23-54")
        elif name == 'Петя':
            label.config(text=f"+ 7 (953) 411-45-54")
        elif name == 'Маша':
            label.config(text=f"+ 7 (963) 493-23-57")

    # Создание главного окна
    root = tk.Tk()
    root.title("Radiobuttons with indicatoron=0")

    # Переменная для отслеживания выбранной кнопки
    selected_option = tk.StringVar(value="Ничего не выбрано")

    # Метка для отображения информации
    label = tk.Label(root, text="Ничего не выбрано", font=("Arial", 12))
    label.pack(side=tk.RIGHT)

    # Радиокнопки
    options = ["Вася", "Петя", "Маша"]
    for option in options:
        rb = tk.Radiobutton(
            root,
            text=option,
            value=option,
            variable=selected_option,
            command=update_label,
            indicatoron=0,  # Отключение индикатора
            width=15,
            padx=5,
            pady=5,
            font=15
        )
        rb.pack()

    # Запуск главного цикла приложения
    root.mainloop()

if __name__ == '__main__':
    main()