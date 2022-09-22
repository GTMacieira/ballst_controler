from cProfile import label
from cgitb import text
from tkinter import *
from turtle import hideturtle

#cria a janela
root = Tk()

class application():
    def __init__(self):
        self.root=root # Inclui o root dentro da função        
        self.menu() # Chama a função menu
        root.mainloop() # Mantem a janela em exibição
    def menu(self):
        self.root.title("MENU") # Define o nome da janela como MENU
        self.root.configure(background='#191970') # Define a cor de fundo da janela
        self.root.geometry("500x400") # Define tamanho da janela
        self.root.resizable(True,True) # Define se será possivel ajustar o tamanho da janela
        self.root.maxsize(width=900, height=700) # Define tamanho maximo da tela
        self.root.minsize(width=500, height=400) # Define tamanho minimo da tela
        orientation = Label(Menu, text="Menu para operação das dividas").place(x=100, y= 10) # Cria label
        orientation.grid(column=1, row=1, padx=10, pady=10) # Exibe label
        new_seq_botton = Button(Menu, text="NOVO SEQUENCIAL", height = 3, width = 25, command= 'new_seq' ).place(x =10 , y = 40) #Cria botão, o command deve ser a função sem parenteses
        new_ballast_botton = Button(Menu, text="NOVO LASTRO",height = 3, width = 25, command="").place(x = 205, y = 40) #Cria botão, o command deve ser a função sem parenteses
        repact_botton = Button(Menu, text="REPACTUAÇÃO",height = 3, width = 25, command="").place(x =10 , y = 100) #Cria botão, o command deve ser a função sem parenteses
        atri_ballsat_botton = Button(Menu, text="ATRIBUIR LASTRO EXCEDENTE",height = 3, width = 25, command="").place(x = 205, y = 100) #Cria botão, o command deve ser a função sem parenteses
        res_mesa_botton = Button(Menu, text="RELATÓRIO MESA",height = 3, width = 25, command="").place(x = 10, y = 160) #Cria botão, o command deve ser a função sem parenteses



# 
application()

