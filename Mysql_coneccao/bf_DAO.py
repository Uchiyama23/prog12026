# importar a classe

# importar a biblioteca para trabalhar com MySQL
import mysql.connector

def retornar_pessoas():

    # conectar ao servidor MySQL com usuário e senha root
    conn = mysql.connector.connect(
        host="10.10.34.239",
        user="emi",
        password="emi1020"
    )

    # criar um cursor para executar comandos SQL
    cursor = conn.cursor()

    # selecionar o banco de dados
    cursor.execute("USE  info2026emi")
    
    # executar o comando SQL para selecionar todas as pessoas
    cursor.execute('SELECT ID_COISA FROM Antonia')
    
    # obter os resultados da consulta
    pessoas = cursor.fetchall()

    # preparar uma lista de retorno
    retorno = []

    # percorrer a lista de pessoas obtidas
    
    retorno.append(pessoas)

     # fechar a conexão com o banco de dados
    conn.close()

    # retornar o retorno :-)
    return retorno

'''
alternativas:

a) retorno = [Pessoa(nome, email, telefone) for nome, email, telefone in cursor.fetchall()]

b) return [Pessoa(*pessoa) for pessoa in cursor.fetchall()]

'''
