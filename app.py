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

# Criando logica do app ------------------------------

Jogador_1 = "X"
Jogador_2 = "O"

score_1 = "X"
score_2 = "O"

tabela = [["1", "2", "3"] ,["4" ,"5" ,"6"], ["7" ,"8" ,"9"]]

def iniciar_jogo():
    #para controlar o jogo
    def controlar():
        pass
        #para decidir o vencedor
        def vencedor():
          
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
app_.place(x=156, y=15)

# LINHAS HORIZONTAIS
app_ = Label(frame_baixo, text="", width=46,
              relief='flat', padx="2", pady="1", anchor="center", 
              font=("Ivy 5 bold"), bg=co0, fg=co7)
app_.place(x=30, y=63)

app_ = Label(frame_baixo, text="", width=46,
              relief='flat', padx="2", pady="1", anchor="center", 
              font=("Ivy 5 bold"), bg=co0, fg=co7)
app_.place(x=30, y=127)

#linha 0 de botões  
b_0 = Button(frame_baixo, text=" ", width=3, height=1,  font=("Ivy 20 bold"), overrelief=RIDGE, relief="flat", bg=fundo, fg=co7)
b_0.place(x=30, y=15)
b_1 = Button(frame_baixo, text=" ", width=3, height=1,  font=("Ivy 20 bold"), overrelief=RIDGE, relief="flat", bg=fundo, fg=co7)
b_1.place(x=96, y=15)
b_2 = Button(frame_baixo, text=" ", width=3, height=1,  font=("Ivy 20 bold"), overrelief=RIDGE, relief="flat", bg=fundo, fg=co7)
b_2.place(x=162, y=15)

#linha 1 de botões
b_3 = Button(frame_baixo, text=" ", width=3, height=1,  font=("Ivy 20 bold"), overrelief=RIDGE, relief="flat", bg=fundo, fg=co7)
b_3.place(x=30, y=75)
b_4 = Button(frame_baixo, text=" ", width=3, height=1,  font=("Ivy 20 bold"), overrelief=RIDGE, relief="flat", bg=fundo, fg=co7)
b_4.place(x=96, y=75)
b_5 = Button(frame_baixo, text=" ", width=3, height=1,  font=("Ivy 20 bold"), overrelief=RIDGE, relief="flat", bg=fundo, fg=co7)
b_5.place(x=162, y=75)


#linha 2 de botões
b_6 = Button(frame_baixo, text=" ", width=3, height=1,  font=("Ivy 20 bold"), overrelief=RIDGE, relief="flat", bg=fundo, fg=co7)
b_6.place(x=30, y=135)
b_7 = Button(frame_baixo, text=" ", width=3, height=1,  font=("Ivy 20 bold"), overrelief=RIDGE, relief="flat", bg=fundo, fg=co7)
b_7.place(x=96, y=135)
b_8 = Button(frame_baixo, text=" ", width=3, height=1,  font=("Ivy 20 bold"), overrelief=RIDGE, relief="flat", bg=fundo, fg=co7)
b_8.place(x=162, y=135)

# botão jogar 
b_jogar = Button(frame_baixo, text="Jogar ", width=10, height=1,  font=("Ivy 10 bold"), overrelief=RIDGE, relief="raised", bg=fundo, fg=co0)
b_jogar.place(x=81, y=210)

janela.mainloop()
