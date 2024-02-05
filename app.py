import tkinter
from tkinter import *
from tkinter import ttk

# cores ---------------------------------------
co0 = "#FFFFFF"  # branca / white
co1 = "#333333"  # preta pesado / dark black
co2 = "#fcc058"  # laranja / orange
co3 = "#38576b"  # valor / value
co4 = "#3297a8"   # azul / blue
co5 = "#fff873"   # amarela / yellow
co6 = "#fcc058"  # laranja / orange
co7 = "#e85151"   # vermelha / red
co8 = co4   # + verde
co10 ="#fcfbf7"
fundo = "#3b3b3b" # preta / black

# criando window principal
window = Tk()
window.title('')
window.geometry('260x370')
window.configure(bg=fundo)


# Dividindo a window em 2 frames ---------------------------------------

top_frame = Frame(window, width=240, height=100, bg=co1, relief="raised")
top_frame.grid(row=0, column=0, sticky=NW, padx=10, pady=10)

bottom_frame = Frame(window, width=240, height=300, bg=fundo, relief="flat")
bottom_frame.grid(row=1, column=0, sticky=NW)


# Setting the Frame_main -----------------
app_x = Label(top_frame, text='X', height=1, relief='flat', anchor='center', font=('Ivy 40 bold'), bg=co1, fg=co7 )
app_x.place(x=25, y=10)
app_x = Label(top_frame, text='Player 1', height=1, relief='flat', anchor='center', font=('Ivy 7 bold'), bg=co1, fg=co0 )
app_x.place(x=17, y=70)
app_x_points = Label(top_frame, text='0', height=1, relief='flat', anchor='center', font=('Ivy 30 bold'), bg=co1, fg=co0 )
app_x_points.place(x=80, y=20)

app_separator = Label(top_frame, text=':', height=1, relief='flat', anchor='center', font=('Ivy 30 bold'), bg=co1, fg=co0 )
app_separator.place(x=110, y=20)

app_o = Label(top_frame, text='O', height=1, relief='flat', anchor='center', font=('Ivy 40 bold'), bg=co1, fg=co4 )
app_o.place(x=170, y=10)
app_o = Label(top_frame, text='Player 2', height=1, relief='flat', anchor='center', font=('Ivy 7 bold'), bg=co1, fg=co0 )
app_o.place(x=165, y=70)
app_o_points = Label(top_frame, text='0', height=1, relief='flat', anchor='center', font=('Ivy 30 bold'), bg=co1, fg=co0 )
app_o_points.place(x=130, y=20)

# Configurando o frame baixo ---------------------------------------


# Creating app logic -------------------

Player_1 = "X"
Player_2 = "O"

score_1 = 0
score_2 = 0

table = [['1','2','3'] , ['4','5','6'] , ['7','8','9']]

playing = 'X'
play =''
counter = 0
round_counter = 0


def start_Game():
    b_play.place(x=800, y=350)
    # to control the game
    def control(i):
        global playing
        global counter
        global play
                
        # comparing the received value
        if i==str(1):
            # checking if that position is empty or not
            if b_0['text']=='':
                # checking who is playing and thus defining the color of the symbol
                if playing =='X':
                    cor=co7
                if playing =='O':
                    cor=co8
                
                # setting the button text color
                # and mark that table position
                # with the value of the current Player
                b_0['fg'] = cor
                b_0['text'] = playing
                table[0][0]= playing
                
                # checking who is playing ,
                # to be able to switch players
                if playing =='X':
                    playing = 'O'
                    play = 'Player 1'
                else:
                    playing = 'X'
                    play = 'Player 2'
                
                # increment the counter for the next round
                counter+=1
                   
        if i==str(2):
            # verificando se aquela posicao esta vazia ou nao
            if b_1['text']=='':
                # varificando quem esta play e assim definir a cor do smbolo
                if playing =='X':
                    cor=co7
                if playing =='O':
                    cor=co8
                
                # definindo a cor do text do botao
                # e marcar aquela posicao da table 
                # com o valor do Player atual
                b_1['fg'] = cor
                b_1['text'] = playing
                table[0][1] = playing
                
                # verificando quem esta a play ,
                # para poder trocar de Player
                if playing =='X':
                    playing = 'O'
                    play = 'Player 1'
                else:
                    playing = 'X'
                    play = 'Player 2'
                
                # incrementar o counter para proxima rodada
                counter+=1
                             
        if i==str(3):
            # verificando se aquela posicao esta vazia ou nao
            if b_2['text']=='':
                # varificando quem esta play e assim definir a cor do smbolo
                if playing =='X':
                    cor=co7
                if playing =='O':
                    cor=co8
                
                # definindo a cor do text do botao
                # e marcar aquela posicao da table 
                # com o valor do Player atual
                b_2['fg'] = cor
                b_2['text'] = playing
                table[0][2]= playing
                
                # verificando quem esta a play ,
                # para poder trocar de Player
                if playing =='X':
                    playing = 'O'
                    play = 'Player 1'
                else:
                    playing = 'X'
                    play = 'Player 2'
                
                # incrementar o counter para proxima rodada
                counter+=1   
                   
        if i==str(4):
            # verificando se aquela posicao esta vazia ou nao
            if b_3['text']=='':
                # varificando quem esta play e assim definir a cor do smbolo
                if playing =='X':
                    cor=co7
                if playing =='O':
                    cor=co8
                
                # definindo a cor do text do botao
                # e marcar aquela posicao da table 
                # com o valor do Player atual
                b_3['fg'] = cor
                b_3['text'] = playing
                table[1][0] = playing
                
                # verificando quem esta a play ,
                # para poder trocar de Player
                if playing =='X':
                    playing = 'O'
                    play = 'Player 1'
                else:
                    playing = 'X'
                    play = 'Player 2'
                
                # incrementar o counter para proxima rodada
                counter+=1
                                      
        if i==str(5):
            # verificando se aquela posicao esta vazia ou nao
            if b_4['text']=='':
                # varificando quem esta play e assim definir a cor do smbolo
                if playing =='X':
                    cor=co7
                if playing =='O':
                    cor=co8
                
                # definindo a cor do text do botao
                # e marcar aquela posicao da table 
                # com o valor do Player atual
                b_4['fg'] = cor
                b_4['text'] = playing
                table[1][1] = playing
                
                # verificando quem esta a play ,
                # para poder trocar de Player
                if playing =='X':
                    playing = 'O'
                    play = 'Player 1'
                else:
                    playing = 'X'
                    play = 'Player 2'
                
                # incrementar o counter para proxima rodada
                counter+=1
                       
        if i==str(6):
            # verificando se aquela posicao esta vazia ou nao
            if b_5['text']=='':
                # varificando quem esta play e assim definir a cor do smbolo
                if playing =='X':
                    cor=co7
                if playing =='O':
                    cor=co8
                
                # definindo a cor do text do botao
                # e marcar aquela posicao da table 
                # com o valor do Player atual
                b_5['fg'] = cor
                b_5['text'] = playing
                table[1][2] = playing
                
                # verificando quem esta a play ,
                # para poder trocar de Player
                if playing =='X':
                    playing = 'O'
                    play = 'Player 1'
                else:
                    playing = 'X'
                    play = 'Player 2'
                
                # incrementar o counter para proxima rodada
                counter+=1   
                        
        if i==str(7):
            # verificando se aquela posicao esta vazia ou nao
            if b_6['text']=='':
                # varificando quem esta play e assim definir a cor do smbolo
                if playing =='X':
                    cor=co7
                if playing =='O':
                    cor=co8
                
                # definindo a cor do text do botao
                # e marcar aquela posicao da table 
                # com o valor do Player atual
                b_6['fg'] = cor
                b_6['text'] = playing
                table[2][0] = playing
                
                # verificando quem esta a play ,
                # para poder trocar de Player
                if playing =='X':
                    playing = 'O'
                    play = 'Player 1'
                else:
                    playing = 'X'
                    play = 'Player 2'
                
                # incrementar o counter para proxima rodada
                counter+=1
                     
        if i==str(8):
            # verificando se aquela posicao esta vazia ou nao
            if b_7['text']=='':
                # varificando quem esta play e assim definir a cor do smbolo
                if playing =='X':
                    cor=co7
                if playing =='O':
                    cor=co8
                
                # definindo a cor do text do botao
                # e marcar aquela posicao da table 
                # com o valor do Player atual
                b_7['fg'] = cor
                b_7['text'] = playing
                table[2][1] = playing
                
                # verificando quem esta a play ,
                # para poder trocar de Player
                if playing =='X':
                    playing = 'O'
                    play = 'Player 1'
                else:
                    playing = 'X'
                    play = 'Player 2'
                
                # incrementar o counter para proxima rodada
                counter+=1      
        
        if i==str(9):
            # verificando se aquela posicao esta vazia ou nao
            if b_8['text']=='':
                # varificando quem esta play e assim definir a cor do smbolo
                if playing =='X':
                    cor=co7
                if playing =='O':
                    cor=co8
                
                # definindo a cor do text do botao
                # e marcar aquela posicao da table 
                # com o valor do Player atual
                b_8['fg'] = cor
                b_8['text'] = playing
                table[2][2] = playing
                
                # verificando quem esta a play ,
                # para poder trocar de Player
                if playing =='X':
                    playing = 'O'
                    play = 'Player 1'
                else:
                    playing = 'X'
                    play = 'Player 2'
                
                # incrementar o counter para proxima rodada
                counter+=1
                
        # After the counter is greater than or equal to 5,
        # check if it hears any winner accordingly
        # with the following patterns inside the table
        if counter>=5:
            # rows
            if table[0][0]==table[0][1]==table[0][2]!="":
                winner(playing)
            elif table[1][0] == table[1][1]==table[1][2]!="":
                winner(playing)
            elif table[2][0] == table[2][1]==table[2][2]!="":
                winner(playing)
            
            # columns
            if table[0][0] == table[1][0]==table[2][0]!="":
                winner(playing)
            elif table[0][1] == table[1][1]==table[2][1]!="":
                winner(playing)
            elif table[0][2] == table[1][2]==table[2][2]!="":
                winner(playing)
                
                
            # diagonals
            if table[0][0] == table[1][1]==table[2][2]!="":
                winner(playing)
            elif table[0][2] == table[1][1]==table[2][0]!="":
                winner(playing)
            
            # A tie
            if counter>=9:
                winner('Draw') 
                       
    
    # to decide the winner
    def winner(i):
        global table
        global score_1
        global score_2
        global round_counter
        global counter
        
        # blocking the buttons
        b_0['state']='disable'
        b_1['state']='disable'
        b_2['state']='disable'
        b_3['state']='disable'
        b_4['state']='disable'
        b_5['state']='disable'
        b_6['state']='disable'
        b_7['state']='disable'
        b_8['state']='disable'
        
        app_winner = Label(bottom_frame, text='', width=17, relief='flat', anchor='center', font=('Ivy 13 bold'), bg=co1, fg=co2 )
        app_winner.place(x=40, y=220)
        
        if i =='X':
            score_2+=1
            app_winner['text'] = 'Player 2 won'
            app_o_points['text'] =score_2
            
        if i =='O':
            score_1+=1
            app_winner['text'] = 'Player 1 won'
            app_x_points['text'] =score_1
        
        if i=='Draw':
            app_winner['text'] = 'Draw'
            
        def start():
            # cleaning the buttons
            b_0['text']=''
            b_1['text']=''
            b_2['text']=''
            b_3['text']=''
            b_4['text']=''
            b_5['text']=''
            b_6['text']=''
            b_7['text']=''
            b_8['text']=''
            
            b_0['state']='normal'
            b_1['state']='normal'
            b_2['state']='normal'
            b_3['state']='normal'
            b_4['state']='normal'
            b_5['state']='normal'
            b_6['state']='normal'
            b_7['state']='normal'
            b_8['state']='normal'
            
            app_winner.destroy()
            b_play.destroy()
            
        # Botao play
        b_play = Button(bottom_frame, command=start, text='next round', height=1,  font=('Ivy 10 bold'), overrelief=RIDGE, relief='raised', bg=fundo, fg=co0 )
        b_play.place(x=70, y=197)
        
        
        def game_over():
            b_play.destroy()
            app_winner.destroy()
            
            finish()
        
        if round_counter>=5:
            game_over()
        else:
            round_counter+=1
            # reiniciando a table
            table = [['1','2','3'] , ['4','5','6'] , ['7','8','9']]
            counter = 0
            
           
    
    # to finish the current game
    def finish():
        global table
        global round_counter
        global score_1
        global score_2
        global counter
        
        table = [['1','2','3'] , ['4','5','6'] , ['7','8','9']]
        round_counter = 0
        score_1 = 0
        score_2 = 0
        counter = 0
        
        # bloqueando os botoes
        b_0['state']='disable'
        b_1['state']='disable'
        b_2['state']='disable'
        b_3['state']='disable'
        b_4['state']='disable'
        b_5['state']='disable'
        b_6['state']='disable'
        b_7['state']='disable'
        b_8['state']='disable'
        
        app_fim = Label(bottom_frame, text='Game over', width=17, relief='flat', anchor='center', font=('Ivy 13 bold'), bg=co1, fg=co2 )
        app_fim.place(x=25, y=90)
        
        # play de novo
        
        def play_again():
            app_x_points['text'] = '0'
            app_o_points['text'] = '0'
            app_fim.destroy()
            b_play.destroy()
            
            # chamando a funcao iniciar o jogo
            start_Game()
        
        # Botao play denovo
        b_play = Button(bottom_frame, command=play_again, text='play again', height=1,  font=('Ivy 10 bold'), overrelief=RIDGE, relief='raised', bg=fundo, fg=co0 )
        b_play.place(x=80, y=197)
        
        
    # Vertical lines
    app_ = Label(bottom_frame, text='', height=23, relief='flat', pady=5, anchor='center', font=('Ivy 5 bold'), bg=co0, fg=co7 )
    app_.place(x=90, y=15)
    app_ = Label(bottom_frame, text='', height=23, relief='flat', pady=5, anchor='center', font=('Ivy 5 bold'), bg=co0, fg=co7 )
    app_.place(x=157, y=15)

    # Horizontal lines
    app_ = Label(bottom_frame, text='', width=46, relief='flat', padx=2, pady=1, anchor='center', font=('Ivy 5 bold'), bg=co0, fg=co7 )
    app_.place(x=30, y=63)
    app_ = Label(bottom_frame, text='', width=46, relief='flat', padx=2, pady=1, anchor='center', font=('Ivy 5 bold'), bg=co0, fg=co7 )
    app_.place(x=30, y=127)
    
    # row 0
    b_0 = Button(bottom_frame,command=lambda:control('1'), text='', width=3, height=1,  font=('Ivy 20 bold'), overrelief=RIDGE, relief='flat', bg=fundo, fg=co7 )
    b_0.place(x=30, y=15)
    b_1 = Button(bottom_frame,command=lambda:control('2'), text='', width=3, height=1,  font=('Ivy 20 bold'), overrelief=RIDGE, relief='flat', bg=fundo, fg=co7 )
    b_1.place(x=96, y=15)
    b_2 = Button(bottom_frame,command=lambda:control('3'), text='', width=3, height=1,  font=('Ivy 20 bold'), overrelief=RIDGE, relief='flat', bg=fundo, fg=co7 )
    b_2.place(x=163, y=15)


    # row 1
    b_3 = Button(bottom_frame,command=lambda:control('4'), text='', width=3, height=1,  font=('Ivy 20 bold'), overrelief=RIDGE, relief='flat', bg=fundo, fg=co7 )
    b_3.place(x=30, y=75)
    b_4 = Button(bottom_frame,command=lambda:control('5'), text='', width=3, height=1,  font=('Ivy 20 bold'), overrelief=RIDGE, relief='flat', bg=fundo, fg=co7 )
    b_4.place(x=96, y=75)
    b_5 = Button(bottom_frame,command=lambda:control('6'), text='', width=3, height=1,  font=('Ivy 20 bold'), overrelief=RIDGE, relief='flat', bg=fundo, fg=co7 )
    b_5.place(x=163, y=75)

    # row 2
    b_6 = Button(bottom_frame,command=lambda:control('7'), text='', width=3, height=1,  font=('Ivy 20 bold'), overrelief=RIDGE, relief='flat', bg=fundo, fg=co7 )
    b_6.place(x=30, y=135)
    b_7 = Button(bottom_frame,command=lambda:control('8'), text='', width=3, height=1,  font=('Ivy 20 bold'), overrelief=RIDGE, relief='flat', bg=fundo, fg=co7 )
    b_7.place(x=96, y=135)
    b_8 = Button(bottom_frame,command=lambda:control('9'), text='', width=3, height=1,  font=('Ivy 20 bold'), overrelief=RIDGE, relief='flat', bg=fundo, fg=co7 )
    b_8.place(x=163, y=135)

# Botao play
b_play = Button(bottom_frame, command=start_Game, text='Play', width=10, height=1,  font=('Ivy 10 bold'), overrelief=RIDGE, relief='raised', bg=fundo, fg=co0 )
b_play.place(x=85, y=197)


window.mainloop()
 

