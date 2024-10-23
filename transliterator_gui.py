import tkinter as tk


def transliterate(text):
    translit_dict = {
        "а": "a", "б": "b", "в": "v", "г": "g", "д": "d", "е": "e", "ё": "yo",
        "ж": "zh", "з": "z", "и": "i", "й": "y", "к": "k", "л": "l", "м": "m",
        "н": "n", "о": "o", "п": "p", "р": "r", "с": "s", "т": "t", "у": "u",
        "ф": "f", "х": "kh", "ц": "ts", "ч": "ch", "ш": "sh", "щ": "sch",
        "ы": "y", "э": "e", "ю": "yu", "я": "ya", "ь": "", "ъ": "", " ": "."
    }

    result = ""
    for char in text.lower():
        result += translit_dict.get(char, char)

    return result


def on_transliterate_click():
    input_text = input_text_box.get("1.0", tk.END).strip()
    result_text = transliterate(input_text)
    output_text_box.config(state=tk.NORMAL)
    output_text_box.delete("1.0", tk.END)
    output_text_box.insert(tk.END, result_text)
    output_text_box.config(state=tk.DISABLED)


# Создаем главное окно
root = tk.Tk()
root.title("Transliterator")

# Поле ввода текста для транслитерации
input_text_label = tk.Label(root, text="Введите текст для транслитерации:")
input_text_label.pack()
input_text_box = tk.Text(root, height=5, width=50)
input_text_box.pack()

# Кнопка для запуска транслитерации
transliterate_button = tk.Button(root, text="Транслитерировать", command=on_transliterate_click)
transliterate_button.pack()

# Поле для результата транслитерации
output_text_label = tk.Label(root, text="Результат:")
output_text_label.pack()
output_text_box = tk.Text(root, height=5, width=50, state=tk.DISABLED)
output_text_box.pack()

# Запуск основного цикла приложения
root.mainloop()