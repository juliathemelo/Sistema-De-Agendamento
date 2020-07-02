from tkinter import*
from tkinter import messagebox
import sqlite3

#Criação da janela
janela = Tk()
janela.title('Sistema de Agendamento (nome da empresa)')
janela.geometry('800x500')
janela.configure(background='white')
janela.resizable(width=False, height=False)

#Funcoes
def botaoAgenda():
    FrameAgendar.place(x=0,y=0)


#Frame de principal(frame do menu/inicio do programa)
FramePrincipal = Frame(janela,width=800, height=500, bg='white')
FramePrincipal.place(x=0,y=0)

#background do menu principal
photo = PhotoImage(file="fundoagenda.png")
labelfundo = Label(FramePrincipal, image=photo)
labelfundo.pack()

#botoes e labels do frameprincipal
title = Label(FramePrincipal,text="Sistema de Agendamento (nome da empresa)",font=('Times New Roman',20),bg='white')
title.place(x=155,y=40)

Agendar = Button(FramePrincipal, text='Agendar Cliente',fg = "blue4", bg = "orange",width = 20, height=3, command=botaoAgenda)
Agendar.place(x=90,y=155)
Consultar = Button(FramePrincipal, text='Consultar Agendamentos',fg = "blue4",bg = "orange", width = 20,height=3)
Consultar.place(x=330, y=155)

Remover = Button(FramePrincipal, text='Remover Agendamentos', fg = "blue4",bg = "orange", width = 20,height=3)
Remover.place(x=565,y=155)

descricao1 = Label(FramePrincipal, text='Agendar um cliente por vez e adicionar o profissional que vai atendê-lo,hórario e dia da sua consulta',font=('Times New Roman',13),bg="gold2")
descricao1.place(x=50,y=266)

descricao2 = Label(FramePrincipal, text='A consulta dos clientes que já estão agendados é feita pelo CPF',font=('Times New Roman',13),bg="gold2")
descricao2.place(x=50,y=313)

descricao3 = Label(FramePrincipal, text='Remover clientes já atendidos ou consultas canceladas e remarcadas.',font=('Times New Roman',13),bg="gold2")
descricao3.place(x=50,y=358)




#Frame Cadastro (frame para cadastrar os clientes)
FrameAgendar = Frame(janela,width=800,height=500, bg='white')
FrameAgendar.place(x=1000,y=2000)
FrameAgendar.propagate(0)

#background da parte de agendamento
photoAgenda = PhotoImage(file="arteagenda.png")
labelagenda = Label(FrameAgendar, image=photoAgenda)
labelagenda.pack()

#entrys e label da agenda
tituloAgendar = Label(FrameAgendar, text="Agendamento Cliente",font=('Times New Roman',28),bg="white")
tituloAgendar.place(x=460,y=15)
nomeLabel = Label(FrameAgendar, text="Nome Completo",font=('Times New Roman',13),bg="gold2")
nomeLabel.place(x=60,y=170)





janela.mainloop()
