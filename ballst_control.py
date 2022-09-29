# Importar bibliotecas necessárias
import getpass
import time
from db_operator import *


menu = input("1- Novo sequencial\n\
    2- Novo tipo de divida\n\
    3- Novo lastro\n\
    4- Repactuação\n\
    5- Atribuir Lastro excedente\n\
    6- Relatório mesa\n")
    
dts_debt = ["seq","new_seq","tp_cont","dt_cont","moeda","val_princ","inst_financ","dt_ini","dt_fim","emp","tp_div","class","cont"]


if menu == "1":
    for dt in dts_debt:
        print(dt)
        dt = input(f"{dt} ")
        print(f"{dt}")
    
    
    
# Cria coneão com db
connection = con_creation()
# Captura usuario do sistema
user = getpass.getuser()
query_type = input("Tipo de query (CREATE, READ, INSERT, UPDATE, DELETE):\n").upper()
query = input("insira o comandao SQL\n")

execute_query(query_type,query)

# Finaliza conexão com db
connection.close()
