# Importar bibliotecas necessárias
import sqlite3 
from sqlite3 import Error 

# Realiza conexão com banco de dados
def con_creation():
    connection = None    
    try:
        connection = sqlite3.connect("ball_control.db")        
    except Error as err:
        print(f"Não foi possível criar conexão com o banco banco ball_control, erro:\n {err}")
        pass
    return connection

# Executa querys CRUD
def execute_query(query_type, query):
    # Cria cursor interador para manipular informaçõs do db
    cursor = connection.cursor()
    # Realiza ação de acordo com o tipo de query
    try:
        if query_type == "INSERT" or query_type == "CREATE" or query_type == "DELETE":
            cursor.execute(query)        
            try:
                connection.commit()
            except:
                pass  
                print("\nAção realizada com sucesso!\n")
        elif query_type == "READ":
            cursor.execute(query)
            results = cursor.fetchall()
            for result in results:
                print(result)
    except Error as err:
        print(f"Não foi possível realizar a ação de {query_type}, erro:\n {err}")
    # Finaliza o cursor     
    cursor.close()