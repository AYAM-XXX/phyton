import tkinter as tk
from PIL import Image, ImageTk
import customtkinter as ctk
from tkinter import mainloop
from tkinter.ttk import Treeview, Scrollbar, Style
COR_FUNDO = "#FFF5F3"
COR_FRAME = "#FFE8E5"
COR_TEXTO = "#4A2C2A"
COR_CAMPO = "#FFFFFF"
COR_BORDA = "#E8A9A2"
COR_BOTAO = "#E98F86"
COR_BOTAO_HOVER = "#D96F65"
COR_BRANCO = "#FFFFFF"


class Function():

    def calcular_imc(self):
        try:
            weight = float(self.weight_entry.get())
            height = float(self.height_entry.get())

            imc = weight / (height * height)

            if imc == "":
                self.saida_label.configure(text="Insira os dados")
            if imc < 18.5:
                texto_saida = f"Seu IMC é {imc:.2f}, você esta abaixo do peso"
                self.saida_label.configure(text=texto_saida)

            elif imc < 25:
                texto_saida = f"Seu IMC é {imc:.2f}, você esta com peso normal"
                self.saida_label.configure(text=texto_saida)
            elif imc < 30:
                texto_saida = f"Seu IMC é {imc:.2f}, você esta acima do peso"
                self.saida_label.configure(text=texto_saida)
            elif imc < 40:
                texto_saida = f"Seu IMC é {imc:.2f}, você esta com obesidade"
                self.saida_label.configure(text=texto_saida)

            else:
                texto_saida = f"Seu IMC é {imc:.2f}, você esta com obesidade morbida"
                self.saida_label.configure(text=texto_saida)

        except ValueError:

            self.saida_label.configure(text="Insira os dados certos")






class Aplication(Function):
    def __init__(self, window):
        self.window = window
        self.tela()
        self.label_img()
        self.label()
        self.botao()
        self.saida()
        self.window.mainloop()


    def tela(self):
        self.window.title("Calculo imc")
        self.window.geometry("750x650")
        self.window.configure(background=COR_FUNDO)
        self.window.maxsize(750, 650)
        self.window.minsize(750, 650)

    def label_img(self):
        imagem_pil = Image.open("images/graficoCanva.png")
        self.imgTk=ImageTk.PhotoImage(imagem_pil)
        self.img=tk.Label(self.window,image=self.imgTk)
        self.img.configure(background=COR_FUNDO, bd=1, highlightbackground=COR_BORDA, highlightthickness=3)
        self.img.place(relwidth=0.5, relheight=0.4, rely=0.01, relx=0.25)

    def label(self):
        self.weight_label=ctk.CTkLabel(self.window,
            text="Peso (KG)",
            font=("Comic Sans", 30, "bold"),
            text_color=COR_TEXTO,
            fg_color=COR_FUNDO,
            corner_radius=10
            )
        self.weight_label.place(relwidth=0.25, relheight=0.15, rely= 0.42, relx=0.25)
        self.weight_entry=ctk.CTkEntry(
            self.window,
            fg_color=COR_FRAME,
            border_width=3,
            corner_radius=8,
            border_color=COR_BORDA,
            font=("Comic Sans", 15, "bold")
        )
        self.weight_entry.place(relwidth=0.25, relheight=0.07, rely=0.47, relx=0.5)

        self.height_label=ctk.CTkLabel(
            self.window,
            text="Altura (M)",
            fg_color=COR_FUNDO,
            text_color=COR_TEXTO,
            font=("Comic Sans", 30, "bold"),
            corner_radius=8
        )
        self.height_label.place(relwidth=0.25, relheight=0.15, rely=0.55, relx=0.25)
        self.height_entry=ctk.CTkEntry(
            self.window,
            fg_color=COR_FRAME,
            text_color=COR_TEXTO,
            font=("Comic Sans", 15, "bold"),
            border_color=COR_BORDA,
            border_width=3,
            corner_radius=8
        )
        self.height_entry.place(relwidth=0.25, relheight=0.07, rely=0.60, relx=0.5)

    def botao(self):
        self.btn_imc = ctk.CTkButton(
            self.window,
            text="Calcular IMC",
            fg_color=COR_BOTAO,
            text_color=COR_TEXTO,
            border_width=3,
            border_color=COR_BORDA,
            corner_radius=8,
            font=("Comic Sans", 20, "bold"),
            command=self.calcular_imc
            )
        self.btn_imc.place(relwidth=0.55, relheight=0.09, rely=0.70,relx=0.23)

    def saida(self):
        self.saida_label=ctk.CTkLabel(
            self.window,
            text="Insira os dados",
            fg_color=COR_FUNDO,
            text_color=COR_TEXTO,
            font=("Comic Sans", 20, "bold")
        )
        self.saida_label.place(relwidth=0.9, relheight=0.08, rely=0.85,relx=0.05)







window = tk.Tk()

Aplication(window)