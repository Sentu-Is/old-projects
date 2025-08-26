import yagmail
import customtkinter as tk
from tkinter import messagebox
def datos():
    contrasena = password_entry.get()
    asunto = asunto_entry.get()
    mensaje = mensaje_entry.get("1.0", "end-1c")
    titulo = titulo_entry.get()    
    correo = email_entry.get()
    destino = destino_entry.get()


    if "@" not in correo:
        messagebox.showerror("Error", "El correo ingresado es invalido")
        return None
    return correo, contrasena, asunto, mensaje, titulo, destino


def enviar_correos():
    datos_obtenidos = datos()
    correo, contrasena, asunto, mensaje, titulo, destino = datos_obtenidos
    if destino == "":
            
        with open('mails.txt', 'r') as archivo:
            destinatarios = archivo.readlines()

        destinatarios = [destinatario_txt.strip() for destinatario_txt in destinatarios]
    else:
        destinatarios = [destino]
    yag = yagmail.SMTP(user=correo, password=contrasena)

    for destinatario_txt in destinatarios:
        yag.send(destinatario_txt, asunto, [titulo, mensaje])

window = tk.CTk()
email_text = tk.CTkLabel(window, text="Ingrese su Email:")
email_text.grid(row=1, column=0, padx=5)
email_entry = tk.CTkEntry(window)
email_entry.grid(row=1, column=1, pady=25, padx=5)

password_entry = tk.CTkEntry(window)
password_entry.grid(row=1, column=3)
password_text = tk.CTkLabel(window, text="Ingrese su contraseña:")
password_text.grid(row=1, column=2, padx=5)

asunto_entry = tk.CTkEntry(window)
asunto_entry.grid(row=2, column=3)
asunto_text = tk.CTkLabel(window, text="Ingrese el asunto:")
asunto_text.grid(row=2, column=2, padx=5)

destino_entry = tk.CTkEntry(window)
destino_entry.grid(row=3, column=2)
destino_text = tk.CTkLabel(window, text="Ingrese el destinatario:")
destino_text.grid(row=3, column=1, padx=5)

mensaje_entry = tk.CTkTextbox(window)
mensaje_entry.grid(row=4, column=1,columnspan=3, sticky="nsew", pady=10, padx=5)
mensaje_text = tk.CTkLabel(window, text="Ingrese el mensaje:")
mensaje_text.grid(row=4, column=0)

titulo_entry = tk.CTkEntry(window)
titulo_entry.grid(row=2, column=1)
titulo_text = tk.CTkLabel(window, text="Ingrese el titulo:")
titulo_text.grid(row=2, column=0, padx=5)

button_entry = tk.CTkButton(window, text="Llamar datos", command=lambda: datos())
button_entry.grid(row=5, column=0)
button = tk.CTkButton(window, text="Enviar mail", command=lambda: enviar_correos())
button.grid(row=5, column=1, padx=10)

window.title("Mandar Emails")
window.geometry("600x380")
window.mainloop()