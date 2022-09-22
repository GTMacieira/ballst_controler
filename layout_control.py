from cProfile import label
from cgitb import text
from tkinter import *

#cria a janela
Menu = Tk()
Menu.title("MENU")
Menu.geometry("400x400") # Ajustar tamnho da janela
orientation = Label(Menu, text="Menu para operação das dividas") # Cria label
orientation.grid(column=1, row=1, padx=10, pady=10) # Exibe label

botao = Button(Menu, text="Nova Divida", command="") #Cria botão, o command deve ser a função sem parenteses
botao.grid(column=0, row=2, padx=10, pady=10) # Exibe botão

#mantem a janela em exibição
Menu.mainloop()