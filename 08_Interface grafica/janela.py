import tkinter as tk
janela  = tk.Tk()
def ajustar_fonte(event):
    if event.widget == janela:
        largura = event.width


        if largura < 550 and largura > 350:
            titulo.config(font=("Arial", 20, "bold"))
        elif largura <  350 and largura > 250:
            titulo.config(font=("Arial", 15, "bold"))
        elif largura < 250:
            titulo.config(font=("Arial", 10, "bold"))



janela.title("Sistema de cadastro de usuarios")
janela.geometry("900x600")
janela.configure(background="#E87400")
janela.maxsize(1350, 900)
janela.minsize(300, 200)

titulo = tk.Label(
    text = "Bem vindo ao meu app",
    font=("Arial", 30, "bold"),
        background="#E87400"
)
titulo.pack()

subtitulo = tk.Label(text="Digite seu nome: ",
                     font=("italic", 15, "bold"),
                     background="#E87400")
subtitulo.pack(pady=(50,50))

janela.bind("<Configure>", ajustar_fonte)

janela.mainloop()


