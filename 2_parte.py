import tkinter
from tkinter import *
from tkinter import ttk

# colors ---------------------------------------
co0 = "#FFFFFF" # BRANCO
co1 = "#333333" # DARK BLAK
co2 = "#fcc058" # LARANJA
co3 = "#38576b" # FLAT 'CINZINHA'
co4 = "#3297a8" # AZUL
co5 = "#fff873" # AMARELO
co6 = "#fcc058" # LARANJA
co7 = "#e85151"   # VERMELHA
co8 = co4 # + VERDE
co10 = "#fcfbf7" # OUTRO BRANCO
fundo = "#3b3b3b" # ESCURO BLACK


# CRIANDO A JANELA BASE DO JOGO
janela = Tk()
janela.title = '' # DEFINE O TÍTULO DA JANELA
janela.geometry('260x370') # DEFINE O TAMANO DA JANELA
janela.configure(bg=fundo) # 'SETTANDO' A COR DE FUNDO DA TELA INICIAL


# DIVIDINDO A JANELA EM 2 FRAMES (PLACAR E 'CORPO') ------------------------------
frame_cima = Frame(janela, width=240, height=100, bg=co1, relief="raised")
frame_cima.grid(row=0, column=0, sticky=NW, padx=10, pady=10)

frame_baixo = Frame(janela, width=240, height=300, bg=fundo, relief="flat")
frame_baixo.grid(row=1, column=0, sticky=NW)

# CONFIGURANDO O FRAME DE CIMA (CABEÇALHO)
app_x = Label(frame_cima, text="X", height=1,
              relief='flat', anchor="center", 
              font=("Ivy 40 bold"), bg=co1, fg=co7)
app_x.place(x=25, y=10)

app_x = Label(frame_cima, text="Jogador 1", height=1,
              relief='flat', anchor="center", 
              font=("Ivy 7 bold"), bg=co1, fg=co0)
app_x.place(x=17, y=70)

app_x_pontos = Label(frame_cima, text="0", height=1,
              relief='flat', anchor="center", 
              font=("Ivy 30 bold"), bg=co1, fg=co0)
app_x_pontos.place(x=80, y=20)


app_separador = Label(frame_cima, text="vs", height=1,
              relief='flat', anchor="center", 
              font=("Ivy 10 bold"), bg=co1, fg=co0)
app_separador.place(x=110, y=35)


app_o = Label(frame_cima, text="O", height=1,
              relief='flat', anchor="center", 
              font=("Ivy 40 bold"), bg=co1, fg=co4)
app_o.place(x=170, y=10)

app_o = Label(frame_cima, text="Jogador 2", height=1,
              relief='flat', anchor="center", 
              font=("Ivy 7 bold"), bg=co1, fg=co0)
app_o.place(x=165, y=70)

app_o_pontos = Label(frame_cima, text="0", height=1,
              relief='flat', anchor="center", 
              font=("Ivy 30 bold"), bg=co1, fg=co0)
app_o_pontos.place(x=130, y=20)


# CONFIGURANDO O FRAME DE BAIXO ('CORPO')

# LINHAS VERTICAIS
app_ = Label(frame_baixo, text="", height=23,
              relief='flat', pady="5", anchor="center", 
              font=("Ivy 5 bold"), bg=co0, fg=co7)
app_.place(x=90, y=15)

app_ = Label(frame_baixo, text="", height=23,
              relief='flat', pady="5", anchor="center", 
              font=("Ivy 5 bold"), bg=co0, fg=co7)
app_.place(x=160, y=15)

# LINHAS HORIZONTAIS
app_ = Label(frame_baixo, text="", width=48,
              relief='flat', padx="2", pady="1", anchor="center", 
              font=("Ivy 5 bold"), bg=co0, fg=co7)
app_.place(x=30, y=63)

app_ = Label(frame_baixo, text="", width=48,
              relief='flat', padx="2", pady="1", anchor="center", 
              font=("Ivy 5 bold"), bg=co0, fg=co7)
app_.place(x=30, y=123)




janela.mainloop()