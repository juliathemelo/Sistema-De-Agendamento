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


def back():
    FramePrincipal.place(x=0,y=0)
    FrameAgendar.place(x=1000,y=1000)


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
nomeLabel = Label(FrameAgendar, text="Nome Completo:",font=('Times New Roman',13),bg="gold2")
nomeLabel.place(x=60,y=170)
cpfLabel = Label(FrameAgendar, text="CPF:",font=('Times New Roman',13),bg="gold2")
cpfLabel.place(x=144,y=210)
numberLabel = Label(FrameAgendar, text="Número Celular:",font=('Times New Roman',13),bg="gold2")
numberLabel.place(x=66,y=250)
dataLabel = Label(FrameAgendar, text="Data Da Consulta:",font=('Times New Roman',13),bg="gold2")
dataLabel.place(x=58,y=290)
profLabel = Label(FrameAgendar, text="Profissional:",font=('Times New Roman',13),bg="gold2")
profLabel.place(x=93,y=330)
avisoLabel = Label(FrameAgendar, text="Todas as informações necessitam está preenchidas e corretas!",font=('Times New Roman',13),bg="gold2")
avisoLabel.place(x=80,y=455)


nomeEntry = Entry(FrameAgendar,width=30)
nomeEntry.place(x=200,y=172)
cpfEntry = Entry(FrameAgendar,width=30)
cpfEntry.place(x=200,y=212)
numberEntry = Entry(FrameAgendar,width=30)
numberEntry.place(x=200,y=252)
dataEntry = Entry(FrameAgendar,width=30)
dataEntry.place(x=200,y=292)
profEntry = Entry(FrameAgendar,width=30)
profEntry.place(x=200,y=332)

#botoes da agenda
agendarButton = Button(FrameAgendar,text='Agendar',fg = "blue4", bg = "orange",width = 20, height=3)
agendarButton.place(x=550,y=170)
voltarButton = Button(FrameAgendar,text='Voltar',fg = "blue4", bg = "orange",width = 20, height=3,command=back)
voltarButton.place(x=550,y=270)


janela.mainloop()
