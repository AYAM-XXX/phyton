import tkinter as tk
from tkinter.ttk import Treeview
from xml.etree.ElementTree import TreeBuilder

COR_FUNDO = "#FFC8C2"
COR_FRAME = "#FFE8E5"
COR_BOTAO = "#8B5E5A"
COR_TEXTO = "#3D2927"
COR_CAMPO = "#FFFFFF"
COR_BORDA = "#C98F89"
TREE_FUNDO  = "#FFF5F3"
TREE_TEXTO  = "#3D2927"
TREE_HEADER = "#C98F89"
TREE_SELECT = "#D98F89"
class Aplication():

    def __init__(self, janela):
        self.janela=janela
        self.tela()
        self.frames_tela()
        self.botoes()
        self.entrar()
        self.lista_saida()
        self.imagem()
        self.janela.mainloop()

    def tela(self):
        self.janela.title("Tela de cadastro")
        self.janela.geometry("1000x600")
        self.janela.configure(background=COR_FUNDO)
        self.janela.maxsize(1350, 900)
        self.janela.minsize(720,460)
    def frames_tela(self):
        self.frames1 = tk.Frame(self.janela)
        self.frames1.configure(background=COR_FRAME, bd=0.5, highlightbackground=COR_BORDA, highlightthickness=3)
        self.frames1.place(relwidth=0.95, relheight=0.45, rely=0.02, relx=0.025)
        self.frames2 = tk.Frame(self.janela)
        self.frames2.configure(background=COR_FRAME, bd=0.5, highlightbackground=COR_BORDA, highlightthickness=3)
        self.frames2.place(relwidth=0.95, relheight=0.45, rely=0.52, relx=0.025)

    def botoes(self):
        self.limpar=tk.Button(self.frames1, text="Limpar")
        self.limpar.configure(background=COR_BOTAO, bd=0.5, highlightbackground=COR_BORDA,highlightthickness=4,font=("Comic Sans", 10, "bold"), foreground=COR_TEXTO)
        self.limpar.place(relwidth=0.10, relheight=0.15, rely=0.1, relx=0.15)
        self.buscar=tk.Button(self.frames1, text="Buscar")
        self.buscar.configure(background=COR_BOTAO, bd=0.5, highlightbackground=COR_BORDA, highlightthickness=4, font=("Comic Sans", 10, "bold"), foreground=COR_TEXTO)
        self.buscar.place(relwidth=0.10, relheight=0.15, rely=0.1, relx=0.25)
        self.apagar = tk.Button(self.frames1, text="Apagar")
        self.apagar.configure(background=COR_BOTAO, bd=0.5, highlightbackground=COR_BORDA,highlightthickness=4, font=("Comic Sans", 10, "bold"), foreground=COR_TEXTO)
        self.apagar.place(relwidth=0.10, relheight=0.15, rely=0.1, relx=0.60)
        self.novo = tk.Button(self.frames1, text="Novo")
        self.novo.configure(background=COR_BOTAO, bd=0.5, highlightbackground=COR_BORDA,highlightthickness=4, font=("Comic Sans", 10, "bold"), foreground=COR_TEXTO)
        self.novo.place(relwidth=0.10, relheight=0.15, rely=0.1, relx=0.70)
        self.alterar = tk.Button(self.frames1, text="Alterar")
        self.alterar.configure(background=COR_BOTAO, bd=0.5, highlightbackground=COR_BORDA,highlightthickness=4, font=("Comic Sans", 10, "bold"), foreground=COR_TEXTO)
        self.alterar.place(relwidth=0.10, relheight=0.15, rely=0.1, relx=0.80)

    def entrar(self):
        self.codigo = tk.Label(self.frames1, text="Codigo")
        self.codigo.configure(background=COR_FRAME, bd=0.5, font=("Comic Sans", 10, "bold"), foreground=COR_TEXTO)
        self.codigo.place(relwidth=0.10, relheight=0.15, rely=0.05, relx=0.02)
        self.entrar_codigo = tk.Entry(self.frames1)
        self.entrar_codigo.configure(background=COR_CAMPO, bd=0.5, highlightbackground=COR_BORDA,highlightthickness=2, font=("Comic Sans", 10, "bold"), foreground=COR_TEXTO)
        self.entrar_codigo.place(relwidth=0.10, relheight=0.15, rely= 0.2, relx=0.02)

        self.nome = tk.Label(self.frames1, text="Nome")
        self.nome.configure(background=COR_FRAME, bd = 0.5, font=("Comic Sans", 12, "bold"), foreground=COR_TEXTO)
        self.nome.place(relwidth=0.10, relheight=0.15, rely=0.40, relx=0.02)
        self.entrar_nome = tk.Entry(self.frames1)
        self.entrar_nome.configure(background=COR_CAMPO, bd=0.5, highlightbackground=COR_BORDA,highlightthickness=2, font=("Comic Sans", 10, "bold"), foreground=COR_TEXTO)
        self.entrar_nome.place(relwidth=0.5, relheight=0.15, rely= 0.40, relx=0.15)

        self.telefone = tk.Label(self.frames1, text="Telefone")
        self.telefone.configure(background=COR_FRAME, bd = 0.5, font=("Comic Sans", 12, "bold"), foreground=COR_TEXTO)
        self.telefone.place(relwidth=0.10, relheight=0.15, rely=0.60, relx=0.02)
        self.entrar_tel = tk.Entry(self.frames1)
        self.entrar_tel.configure(background=COR_CAMPO, bd=0.5, highlightbackground=COR_BORDA,highlightthickness=2, font=("Comic Sans", 10, "bold"), foreground=COR_TEXTO)
        self.entrar_tel.place(relwidth=0.3, relheight=0.15, rely=0.60, relx=0.15)

        self.cidade = tk.Label(self.frames1, text="Cidade")
        self.cidade.configure(background=COR_FRAME, bd = 0.5, font=("Comic Sans", 12, "bold"), foreground=COR_TEXTO)
        self.cidade.place(relwidth=0.10, relheight=0.15, rely=0.80, relx=0.02)
        self.entrar_cid = tk.Entry(self.frames1)
        self.entrar_cid.configure(background=COR_CAMPO, bd=0.5, highlightbackground=COR_BORDA,highlightthickness=2, font=("Comic Sans", 10, "bold"), foreground=COR_TEXTO)
        self.entrar_cid.place(relwidth=0.3, relheight=0.15, rely=0.80, relx=0.15)


    def lista_saida(self):
        self.lista_frame2=Treeview(self.frames2, height=3, columns=("Col1", "Col2", "Col3", "Col4"))

        self.lista_frame2.heading("#0", text="")
        self.lista_frame2.heading("#1", text="Codigo")
        self.lista_frame2.heading("#2", text="Nome")
        self.lista_frame2.heading("#3", text="Telefone")
        self.lista_frame2.heading("#4", text="Cidade")
        self.lista_frame2.column("#0", width=1)
        self.lista_frame2.column("#1", width=50)
        self.lista_frame2.column("#2", width=200)
        self.lista_frame2.column("#3", width=125)
        self.lista_frame2.column("#4", width=125)

        self.lista_frame2.place(relwidth=0.93, relheight=0.93, relx=0.02, rely=0.05)
    def imagem(self):
        self.img = tk.PhotoImage(file="D:\\Users\\1103572\\Downloads\\imgtkinter.png")
        self.janela.iconphoto(True, self.img)




janela=tk.Tk()
Aplication(janela)


janela.mainloop()
