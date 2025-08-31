import tkinter as tk
def mostrardatos():
    nombre = txtnombre.get()
    apellido = txtapellido.get()  
    email = txtemail.get()
    telefono = txttelefono.get()
    
      
    info.config(text=f"Nombre: {nombre}\nApellido: {apellido}\nEmail: {email}\nTeléfono: {telefono}")



    tk.Label(info, text=f"nombre: {nombre}").place(x=500, y=200)
    tk.Label(info, text=f"apellido: {apellido}").place(x=500, y=230)
    tk.Label(info, text=f"email: {email}").place(x=500, y=260)
    tk.Label(info, text=f"telefono: {telefono}").place(x=500, y=290)


    txtnombre.delete(0, tk.END)
    txtapellido.delete(0, tk.END)
    txtemail.delete(0, tk.END)
    txttelefono.delete(0, tk.END)

ventana = tk.Tk()
ancho = ventana.winfo_screenwidth()

alto = ventana.winfo_screenheight()

ventana.geometry(f"{ancho}x{alto}")

ventana.title("app con place: ")
ventana.resizable(False, False)

inicio = tk.Label(ventana, text="formulario de registro", bg="blue", font=("Arial", 24))
lblnombre = tk.Label(ventana, text="Nombre")
lblapellido = tk.Label(ventana, text="Apellido")
lblemail = tk.Label(ventana, text="Email")
lbltelefono = tk.Label(ventana, text="Teléfono")

inicio.place(x=100, y=20)
lblnombre.place(x=100, y=80)
lblapellido.place(x=100, y=120)
lblemail.place(x=100, y=160)
lbltelefono.place(x=100, y=200)

txtnombre = tk.Entry(ventana, width=30)
txtapellido = tk.Entry(ventana, width=30)
txtemail = tk.Entry(ventana, width=30)
txttelefono = tk.Entry(ventana, width=30)

txtnombre.place(x=200, y=80)
txtapellido.place(x=200, y=120)
txtemail.place(x=200, y=160)
txttelefono.place(x=200, y=200)

btnGuardar = tk.Button(ventana, text="Guardar", command=mostrardatos).place(x=299, y=240)

info = tk.Label(ventana, text="", fg="green")
info.place(x=300, y=300)
ventana.mainloop()