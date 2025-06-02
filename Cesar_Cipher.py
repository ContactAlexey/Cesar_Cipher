import tkinter as tk
from tkinter import ttk

def caesar_cipher(text, k):
    result = ""
    for char in text:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            result += chr((ord(char) - ascii_offset + k) % 26 + ascii_offset)
        else:
            result += char
    return result

def encrypt_text():
    text = entry_text.get()
    try:
        k = int(entry_key.get())
        ciphered = caesar_cipher(text, k)
        result_label.config(text=f"Ciphered text: {ciphered}")
    except ValueError:
        result_label.config(text="Please enter a valid integer for the key.")

# Create the main window
window = tk.Tk()
window.title("Cesar Cipher Encryptor")

# Input text
ttk.Label(window, text="Enter text:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
entry_text = ttk.Entry(window, width=40)
entry_text.grid(row=0, column=1, padx=10, pady=5)

# Input key
ttk.Label(window, text="Enter shift (key):").grid(row=1, column=0, padx=10, pady=5, sticky="w")
entry_key = ttk.Entry(window, width=10)
entry_key.grid(row=1, column=1, padx=10, pady=5, sticky="w")

# Encrypt button
encrypt_button = ttk.Button(window, text="Encrypt", command=encrypt_text)
encrypt_button.grid(row=2, column=0, columnspan=2, pady=10)

# Result label
result_label = ttk.Label(window, text="Ciphered text: ", foreground="blue")
result_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Run the app
window.mainloop()
