import tkinter as tk
from tkinter import TclError,ttk,Tk
from services.configBase import ConfigBasicSql

#==================================================
#Configurações da Janela como padrão 
#==================================================

class Welcome:

    ct = ConfigBasicSql()
    def CreateConfig(self,DataBase,Host,password,User,windown,UserSG):
        Config = str(Host+","+User+","+DataBase+","+password)
        self.ct.CreateConfig(Config)
        self.ct.CreateNewUser(UserSG)
        windown.destroy()
    def Screen(self,windown):
        s = ttk.Style()
        s.configure('new.TFrame', background='#7AC5CD')
        m =tk.Toplevel(windown)
        m.title("")
        m.transient(windown)
        m.configure(bg='white')
        m.attributes("-topmost",True)
        m.resizable(0,0)


        frame2 =tk.Frame(m,width=100,height=200,bg="white")
        Label = tk.Label(frame2,text="Seja bem vindo ao Basic Sql")
        Label_ = tk.Label(frame2,text="Este é um sistema onde você podera fazer edição de seus banco de dados,\n desde consultas até adicionar ou remover valores")
        Font_tuple = ("Arial", 20, "bold")
        Label.configure(foreground="gray",font=Font_tuple,background="white")
        Label_.configure(background="white")
        Label.grid(row=0,column=0)
        Label_.grid(row=1,column=0)

        frame3 = tk.Frame(m,width=200,height=300,background="white")
        Font_tuple = ("Arial", 10, "italic")
        Label_informacao = tk.Label(frame3,text="Adicione as informações para você conseguir acessar  o seu banco de dados \nseja remoto ou local.",background="white")
        Label_informacao.configure(font=Font_tuple)

        Label_informacao.grid(row=0,column=0)
        # Formulario de informações 
        Label_NomeHost = tk.Label(frame3,text="Nome do Host: ",background="white")
        Label_NomeHost.grid(column=0,row=1,sticky='W',padx=6)
        Entrada_host = tk.Entry(frame3,textvariable="Host")
        Entrada_host.grid(column=0,row=2,sticky='W',pady="5",padx=6)

        Label_NomeUser = tk.Label(frame3,text="Nome do Usuario: ",background="white")
        Label_NomeUser.grid(column=0,row=3,sticky='W',padx=6)
        Entrada_User = tk.Entry(frame3,textvariable="Usuario")
        Entrada_User.grid(column=0,row=4,sticky='W',pady="5",padx=6)

        Label_Usuario = tk.Label(frame3,text="Usuario: ",background="white")
        Label_Usuario.grid(column=0,row=5,sticky='W',padx=6)
        Entrada_Usuario = tk.Entry(frame3,textvariable="Usuario_x")
        Entrada_Usuario.grid(column=0,row=6,sticky='W',pady="5",padx=6)

        Label_DataBase = tk.Label(frame3,text="Nome da DataBase: ",background="white")
        Label_DataBase.grid(column=0,row=7,sticky='W',padx=6)
        Entrada_DataBase = tk.Entry(frame3,textvariable="Data")
        Entrada_DataBase.grid(column=0,row=8,sticky='W',pady="5",padx=6)

        Label_Password = tk.Label(frame3,text="Senha do banco: ",background="white")
        Label_Password.grid(column=0,row=9,sticky='W',padx=6)
        Entrada_Password = tk.Entry(frame3,show="*",textvariable="Pass")
        Entrada_Password.grid(column=0,row=10,sticky='W',pady="5",padx=6)
        
        Bt_criar = tk.Button(m,text="Criar conexão",command=lambda: self.CreateConfig(Entrada_DataBase.get(),Entrada_host.get(),Entrada_Password.get(),Entrada_User.get(),m,Entrada_Usuario.get()))
        Bt_criar.grid(column=0,row=11,padx=50)

        #================================================
        #Pack Elements
        #================================================
        m.geometry('500x500')
        frame2.grid(row=0,column=0,padx=5,pady=5,ipady=5)
        frame3.grid(row=1,column=0,padx=2,pady=2)