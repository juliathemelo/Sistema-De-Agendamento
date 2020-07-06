from tkinter import*
from tkinter import messagebox
import clientes

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

def botaoConsulta():
    FrameConsulta.place(x=0,y=0)


def back():
    FramePrincipal.place(x=0,y=0)
    FrameAgendar.place(x=1000,y=1000)
    FrameConsulta.place(x=1000,y=1000)

    ListaCpf.delete(0,END)
    nomeEntry.delete(0,END)
    cpfEntry.delete(0,END)
    numberEntry.delete(0,END)
    dataEntry.delete(0,END)
    horarioEntry.delete(0,END)
    profEntry.delete(0,END)

#Funcao de cadastro

def registrarCliente():
    Name = nomeEntry.get()
    Cpf = cpfEntry.get()
    Number = numberEntry.get()
    Data = dataEntry.get()
    Horario = horarioEntry.get()
    Prof = profEntry.get()
    clientes.cursor.execute("""
    INSERT INTO clientes(Name,Cpf,Number,Data,Horario,Profissional)VALUES(?,?,?,?,?,?)
    """,(Name,Cpf,Number,Data,Horario,Prof))
    clientes.conn.commit()
    messagebox.showinfo(title="Aviso",message="Agendamendo Concluido")
    nomeEntry.delete(0,END)
    cpfEntry.delete(0,END)
    numberEntry.delete(0,END)
    dataEntry.delete(0,END)
    horarioEntry.delete(0,END)
    profEntry.delete(0,END)
    

def consultaAll():
    ListaCpf.delete(0,END)
    conn = sqlite3.connect("clientes.db")
    cursor = conn.cursor()
    cursor.execute(""" SELECT * FROM clientes""")
    var = cursor.fetchall()
    if var is None:
        print('Nada Marcado Ainda')
    else:
        for i in var:
            ListaCpf.insert(0,"-|- Nome -|- Cpf -|- Número -|- Data da Consulta -|- Horario -|- Profissional -|-")
            ListaCpf.insert(1,' | '.join(i))
    conn.close()

def consultaCpf():
    ListaCpf.delete(0,END)
    conn = sqlite3.connect("clientes.db")
    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM clientes WHERE Cpf = ?""",(Entrycpf.get(),))
    var = cursor.fetchone()
    if var is None:
        print('Nada Marcado Ainda')
    ListaCpf.insert(0,"-|- Nome -|- Cpf -|- Número -|- Data da Consulta -|- Horario -|- Profissional -|-")
    ListaCpf.insert(1," | ".join(var))
    Entrycpf.delete(0,END)
    conn.close()
    







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

Consultar = Button(FramePrincipal, text='Consultar Agendamentos',fg = "blue4",bg = "orange", width = 20,height=3,command=botaoConsulta)
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
nomeLabel = Label(FrameAgendar, text="Nome e Sobrenome:",font=('Times New Roman',13),bg="gold2")
nomeLabel.place(x=90,y=130)
cpfLabel = Label(FrameAgendar, text="CPF:",font=('Times New Roman',13),bg="gold2")
cpfLabel.place(x=196,y=170)
numberLabel = Label(FrameAgendar, text="Número Celular:",font=('Times New Roman',13),bg="gold2")
numberLabel.place(x=118,y=210)
dataLabel = Label(FrameAgendar, text="Data Da Consulta:",font=('Times New Roman',13),bg="gold2")
dataLabel.place(x=110,y=250)
horarioLabel = Label(FrameAgendar, text="Hora da Consulta:",font=('Times New Roman',13),bg="gold2")
horarioLabel.place(x=111,y=290)
profLabel = Label(FrameAgendar, text="Profissional:",font=('Times New Roman',13),bg="gold2")
profLabel.place(x=144,y=330)
avisoLabel = Label(FrameAgendar, text="Todas as informações necessitam está preenchidas e corretas!",font=('Times New Roman',13),bg="gold2")
avisoLabel.place(x=80,y=455)


nomeEntry = Entry(FrameAgendar,width=30)
nomeEntry.place(x=250,y=133)
cpfEntry = Entry(FrameAgendar,width=30)
cpfEntry.place(x=250,y=173)
numberEntry = Entry(FrameAgendar,width=30)
numberEntry.place(x=250,y=214)
dataEntry = Entry(FrameAgendar,width=30)
dataEntry.place(x=250,y=253)
horarioEntry = Entry(FrameAgendar,width=30)
horarioEntry.place(x=250,y=292)
profEntry = Entry(FrameAgendar,width=30)
profEntry.place(x=250,y=332)

#botoes da agenda
agendarButton = Button(FrameAgendar,text='Agendar',fg = "blue4", bg = "orange",width = 20, height=3,command=registrarCliente)
agendarButton.place(x=550,y=170)
voltarButton = Button(FrameAgendar,text='Voltar',fg = "blue4", bg = "orange",width = 20, height=3,command=back)
voltarButton.place(x=550,y=270)




#Frame consultar atendimentos
FrameConsulta = Frame(janela,width=800,height=500, bg='white')
FrameConsulta.place(x=1000,y=2000)
FrameConsulta.propagate(0)

#background
photoConsulta = PhotoImage(file="arteconsulta.png")
labelConsulta = Label(FrameConsulta, image=photoConsulta)
labelConsulta.pack()

#list box
Labelfundo1 = Label(FrameConsulta,width = 70,height=2,bg="LightBlue")
Labelfundo1.place(x=70,y=90)
Labelfundo1 = Label(FrameConsulta,width = 70,height=2,bg="LightBlue")
Labelfundo1.place(x=70,y=400)
ListaCpf = Listbox(FrameConsulta,width='80',font=('Times New Roman',10),height='20')
ListaCpf.place(x=75,y=100)
tituloConsulta = Label(FrameConsulta, text="Consulta Cliente",font=('Times New Roman',28),bg="white")
tituloConsulta.place(x=460,y=15)
textLabel = Label(FrameConsulta,text="Insira o CPF para Consultar",font=('Times New Roman',13),bg="gold2")
textLabel.place(x=570,y=100)
ButtonConsulta = Button(FrameConsulta,text='Consultar por CPF',fg = "blue4", bg = "orange",width = 20,command=consultaCpf)
ButtonConsulta.place(x=598,y=190)
Labelfundo = Label(FrameConsulta,width = 30,height=2,bg="blue4")
Labelfundo.place(x=565,y=142)
Entrycpf = Entry(FrameConsulta,width=30)
Entrycpf.place(x=580,y=150)
ButtonConsulta1 = Button(FrameConsulta,text='Consultar Todos Marcados',fg = "blue4", bg = "orange",width = 20,command=consultaAll)
ButtonConsulta1.place(x=598,y=240)
voltarButton = Button(FrameConsulta,text='Voltar',fg = "blue4", bg = "orange",width = 20,command=back)
voltarButton.place(x=598,y=290)




janela.mainloop()
