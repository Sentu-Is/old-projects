import customtkinter
import math
customtkinter.set_appearance_mode("dark")



window = customtkinter.CTk()

pixeles = 337

window.geometry(f"{pixeles}x{pixeles}")
window.resizable(False, False)
window.title("Calculadora")

nums = ""

def sumar(*args):
    global nums
    texts = str(*args)
    nums += texts
    text.configure(text=nums)
def res():
    global nums
    nums = str(nums)
    nums = eval(nums)
    text.configure(text=nums)
    nums = str(nums)

def borrar():
    global nums
    nums = ""
    text.configure(text=nums)

def operador(*args):
    global nums
    nums = str(nums)
    texts = str(*args)
    try:
        nums = eval(nums)
    except (SyntaxError or TypeError):
        pass

    i = str(nums)
    if i[-1].isdigit() is False:
        if i[-1] != str(*args):
            nums = i[:-1]
            nums += texts
            text.configure(text=nums)
            nums = str(nums)
    if i[-1].isdigit():
        nums = i
        nums += texts
        text.configure(text=nums)
        nums = str(nums)


def raiz(*args):
    global nums
    texts = str(*args)
    nums = ""
    nums += texts
    text.configure(text=nums)
    nums = eval(nums)

def par():
    global nums
    i = int(nums)
    if (i%2) == 0:
        nums = "Par"
        text.configure(text=nums)
        nums = ""
    else:
        nums = "impar"
        text.configure(text=nums)
        nums = ""
def teclado(event):
    global nums
    tecla = event.keysym
    if tecla == "plus":
        nums += "+"
    elif tecla == "1":
        nums += "1"
    elif tecla == "2":
        nums += "2"
    elif tecla == "3":
        nums += "3"
    elif tecla == "4":
        nums += "4"
    elif tecla == "5":
        nums += "5"
    elif tecla == "6":
        nums += "6"
    elif tecla == "7":
        nums += "7"
    elif tecla == "8":
        nums += "8"
    elif tecla == "9":
        nums += "9"
    elif tecla == "0":
        nums += "0"
    elif tecla == "slash":
        nums += "/"
    elif tecla == "asterisk":
        nums += "*"
    elif tecla == "minus":
        nums += "-"
    elif tecla == "Return":
        res()
    elif tecla == "c":
        borrar()

    print(event)

    text.configure(text=nums)

#Muestra resultado
box = customtkinter.CTkFrame(window, bg_color="grey")
box.grid(row=0, column=0,sticky="nsew")
box.columnconfigure(0, minsize=150)
text = customtkinter.CTkLabel(box, text=nums)
text.grid(row=0, column=0, sticky="nsew", pady=20,padx=55)

#Interfaz
box_interface = customtkinter.CTkFrame(window)
box_interface.grid(row=1, column=0, sticky="nsew")

button_row1 = customtkinter.CTkButton(box_interface, text="%", command=lambda: par(), height=50, width=80, fg_color="grey")
button_row1.grid(row=1, column=0, pady=2, padx=2)
button_row2 = customtkinter.CTkButton(box_interface, text="π", command=lambda: sumar("3.14"), height=50, width=80, fg_color="grey")
button_row2.grid(row=1, column=1, pady=2, padx=2)
button_row3 = customtkinter.CTkButton(box_interface, text="√", command=lambda: raiz("math.sqrt("+nums+")"), height=50, width=80, fg_color="grey")
button_row3.grid(row=1, column=2, pady=2, padx=2)
button_row4 = customtkinter.CTkButton(box_interface, text="C", command=lambda: borrar(), height=50, width=80, fg_color="grey")
button_row4.grid(row=1, column=4, pady=2, padx=2)
button = customtkinter.CTkButton(box_interface, text="1", command=lambda: sumar("1"), height=50, width=80, fg_color="grey")
button.grid(row=2, column=0, pady=2, padx=2)
button2 = customtkinter.CTkButton(box_interface, text="2", command=lambda: sumar("2"), height=50, width=80, fg_color="grey")
button2.grid(row=2, column=1, pady=2, padx=2)
button3 = customtkinter.CTkButton(box_interface, text="3", command=lambda: sumar("3"), height=50, width=80, fg_color="grey")
button3.grid(row=2, column=2, pady=2, padx=2)
button15 = customtkinter.CTkButton(box_interface, text="^", command=lambda: operador("**"), height=50, width=80, fg_color="grey")
button15.grid(row=2, column=4, pady=2, padx=2, sticky="nsew")
button4 = customtkinter.CTkButton(box_interface, text="4", command=lambda: sumar("4"), height=50, width=80, fg_color="grey")
button4.grid(row=3, column=0, pady=2, padx=2)
button5 = customtkinter.CTkButton(box_interface, text="5", command=lambda: sumar("5"), height=50, width=80, fg_color="grey")
button5.grid(row=3, column=1, pady=2, padx=2)
button6 = customtkinter.CTkButton(box_interface, text="6", command=lambda: sumar("6"), height=50, width=80, fg_color="grey")
button6.grid(row=3, column=2, pady=2, padx=2)
button14 = customtkinter.CTkButton(box_interface, text="*", command=lambda: operador("*"), height=50, width=80, fg_color="grey")
button14.grid(row=3, column=4, pady=2, padx=2, sticky="nsew")
button7 = customtkinter.CTkButton(box_interface, text="7", command=lambda: sumar("7"), height=50, width=80, fg_color="grey")
button7.grid(row=4, column=0, pady=2, padx=2, sticky="nsew")
button8 = customtkinter.CTkButton(box_interface, text="8", command=lambda: sumar("8"), height=50, width=80, fg_color="grey")
button8.grid(row=4, column=1, pady=2, padx=2, sticky="nsew")
button9 = customtkinter.CTkButton(box_interface, text="9", command=lambda: sumar("9"), height=50, width=80, fg_color="grey")
button9.grid(row=4, column=2, pady=2, padx=2, sticky="nsew")
button13 = customtkinter.CTkButton(box_interface, text="/", command=lambda: operador("/"), height=50, width=80, fg_color="grey")
button13.grid(row=4, column=4, pady=2, padx=2, sticky="nsew")
button10 = customtkinter.CTkButton(box_interface, text="0", command=lambda: sumar("0"), height=50, width=80, fg_color="grey")
button10.grid(row=5, column=1, pady=2, padx=2, sticky="nsew")
button11 = customtkinter.CTkButton(box_interface, text="-", command=lambda: operador("-"), height=50, width=80, fg_color="grey")
button11.grid(row=5, column=0, pady=2, padx=2, sticky="nsew")
button12 = customtkinter.CTkButton(box_interface, text="+", command=lambda: operador("+"), height=50, width=80, fg_color="grey")
button12.grid(row=5, column=2, pady=2, padx=2, sticky="nsew")
button16 = customtkinter.CTkButton(box_interface, text="=", command=lambda: res(), height=50, width=80, fg_color="grey")
button16.grid(row=5, column=4, pady=2, padx=2, sticky="nsew")


window.bind("<Key>", teclado)
window.mainloop()