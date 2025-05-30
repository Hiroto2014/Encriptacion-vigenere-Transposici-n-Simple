import tkinter as tk
from tkinter import ttk, messagebox

# ---------------- Cifrado Vigenère ---------------- #

# -------- Encriptado  -------- #
def vigenere_encrypt(text, key):
    text = text.upper().replace(" ", "")
    key = key.upper()
    encrypted = ""
    for i in range(len(text)):
        encrypted += chr((ord(text[i]) + ord(key[i % len(key)])) % 26 + 65)
    return encrypted

# -------- Desencriptado  -------- #
def vigenere_decrypt(cipher, key):
    cipher = cipher.upper().replace(" ", "")
    key = key.upper()
    decrypted = ""
    for i in range(len(cipher)):
        decrypted += chr((ord(cipher[i]) - ord(key[i % len(key)])) % 26 + 65)
    return decrypted

# ---------------- Transposición Simple ---------------- #

# -------- Encriptado  -------- #
def transposition_encrypt(text, key):
    key = int(key)
    ciphertext = [''] * key
    for column in range(key):
        pointer = column
        while pointer < len(text):
            ciphertext[column] += text[pointer]
            pointer += key
    return ''.join(ciphertext)

# -------- Desencriptado  -------- #
def transposition_decrypt(ciphertext, key):
    key = int(key)
    num_cols = len(ciphertext) // key + (len(ciphertext) % key != 0)
    num_rows = key
    num_shaded = (num_cols * num_rows) - len(ciphertext)

    plaintext = [''] * num_cols
    col = 0
    row = 0

    for symbol in ciphertext:
        plaintext[col] += symbol
        col += 1
        if (col == num_cols) or (col == num_cols - 1 and row >= num_rows - num_shaded):
            col = 0
            row += 1
    return ''.join(plaintext)

# ---------------- Interfaz ---------------- #

def procesar():
    texto = entrada_texto.get("1.0", tk.END).strip()
    clave = entrada_clave.get()
    metodo = metodo_cifrado.get()
    modo = modo_operacion.get()

    if not texto or not clave:
        messagebox.showerror("Error", "Por favor ingresa el texto y la clave.")
        return

    try:
        if metodo == "Vigenère":
            resultado = vigenere_encrypt(texto, clave) if modo == "Cifrar" else vigenere_decrypt(texto, clave)
        else:
            resultado = transposition_encrypt(texto, clave) if modo == "Cifrar" else transposition_decrypt(texto, clave)
        salida_texto.config(state="normal")
        salida_texto.delete("1.0", tk.END)
        salida_texto.insert(tk.END, resultado)
        salida_texto.config(state="disabled")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Ventana principal
ventana = tk.Tk()
ventana.title("Cifrados Vigenère y Transposición Simple")
ventana.geometry("600x500")

# Widgets
tk.Label(ventana, text="Texto:").pack()
entrada_texto = tk.Text(ventana, height=5)
entrada_texto.pack(padx=10, fill="x")

tk.Label(ventana, text="Clave:").pack()
entrada_clave = tk.Entry(ventana)
entrada_clave.pack(padx=10, fill="x")

tk.Label(ventana, text="Método de cifrado:").pack()
metodo_cifrado = ttk.Combobox(ventana, values=["Vigenère", "Transposición"], state="readonly")
metodo_cifrado.set("Vigenère")
metodo_cifrado.pack(padx=10)

tk.Label(ventana, text="Modo:").pack()
modo_operacion = ttk.Combobox(ventana, values=["Cifrar", "Descifrar"], state="readonly")
modo_operacion.set("Cifrar")
modo_operacion.pack(padx=10)

tk.Button(ventana, text="Procesar", command=procesar).pack(pady=10)

tk.Label(ventana, text="Resultado:").pack()
salida_texto = tk.Text(ventana, height=5, state="disabled")
salida_texto.pack(padx=10, fill="x")

ventana.mainloop()
