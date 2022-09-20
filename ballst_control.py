# Importar bibliotecas necessárias
import getpass
import time
from db_operator import *


    
# Cria coneão com db
connection = con_creation()
# Captura usuario do sistema
user = getpass.getuser()
query_type = input("Tipo de query (CREATE, READ, INSERT, UPDATE, DELETE):\n").upper()
query = input("insira o comandao SQL\n")

execute_query(query_type,query)

# Finaliza conexão com db
connection.close()
