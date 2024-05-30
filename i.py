import tkinter as tk
from tkinter import ttk

# Giả định hàm prediction có định nghĩa như sau:
def prediction(text, tokenizer, model):
    return ["Predicted: " + text]

my_tokenizer = None  # Thay thế bằng tokenizer thực tế của bạn
my_model = None  # Thay thế bằng model thực tế của bạn

def on_button_click():
    input_text = text_entry.get()
    if input_text.lower() == 'end':
        root.quit()
    else:
        result = prediction(input_text, my_tokenizer, my_model)[0]
        result_label.config(text=result)

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Text Prediction App")

# Tạo frame chính
main_frame = ttk.Frame(root, padding="10")
main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Tạo và đặt Entry
text_entry = ttk.Entry(main_frame, width=50)
text_entry.grid(row=0, column=0, padx=5, pady=5)

# Tạo và đặt Button
predict_button = ttk.Button(main_frame, text="Predict", command=on_button_click)
predict_button.grid(row=0, column=1, padx=5, pady=5)

# Tạo và đặt Label cho kết quả
result_label = ttk.Label(main_frame, text="Prediction result will be shown here.")
result_label.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

# Chạy vòng lặp chính của Tkinter
root.mainloop()
