import mysql.connector
from mysql.connector import Error

def conectar_banco():
    """Estabelece conexão com o banco de dados"""
    try:
        conexao = mysql.connector.connect(
            host='localhost',
            user='root',
            password='password',
            database='parque_de_diversões'
        )
        print("Conexão bem-sucedida!")
        return conexao 
    except Error as error:
        print(f"Erro ao conectar ao banco de dados: {error}")
        return None

def cadastrar_bilheteria():

    conexao_aberta = conectar_banco()
    if conexao_aberta:
        cursor = conexao_aberta.cursor() 
        nome = input("Nome da bilheteria: ")
        localizacao = input("Localização: ")
        capacidade = input("Capacidade (número de pessoas): ")
        status = input("Status (Aberta/Fechada): ")

        sql = "INSERT INTO bilheterias (nome, localizacao, capacidade, status) VALUES (%s, %s, %s, %s)" 
        dados = (nome, localizacao, capacidade, status)

        try:
            cursor.execute(sql, dados)
            conexao_aberta.commit()
            print(f"Bilheteria '{nome}' cadastrada com sucesso!")
        except Error as erro:
            print(f"Erro ao cadastrar: {erro}")
        finally:
            cursor.close()
            conexao_aberta.close()


def listar_bilheteria():
    """Listar as bilheterias"""
    conexao = conectar_banco()

    if conexao:
        cursor = conexao.cursor()
        sql = "SELECT nome, status FROM bilheterias"

        try:
            cursor.execute(sql)
            resultados = cursor.fetchall()

            if not resultados:
                print("Nenhuma bilheteria encontrada")
            else:
                for bilheteria in resultados:
                    print(f"{bilheteria[0]} - {bilheteria[1]}")

        except Error as erro:
            print(f"Erro ao consultar: {erro}")

        finally:
            cursor.close()
            conexao.close()

cadastrar_bilheteria()
listar_bilheteria()