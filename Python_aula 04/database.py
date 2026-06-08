#pip install mysql-connector-python
import mysql.connector

from mysql.connector import Error

def connectar_banco():
    """EStabelece conexão"""
    try:
        #tentar conectar
        conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="parque_diversoes"
        )
        if conexao.is_connected():
            print("conectou")
            return conexao
    except Error as erro:
        print(f"Erro ao conectar: {erro}")
        return None
def cadastrar_atracao():
    """inserir novas atrações no parque"""

    conexao_aberta = connectar_banco()
    if conexao_aberta:
        cursor = conexao_aberta.cursor()
        nome = input("nome da atração: ")
        status = input("status (funcionando/manutenção): ")
        sql = "INSERT INTO atracoes (nome, status) VALUES (%s,%s)"
        dados = (nome, status)
        try:
            cursor.execute(sql, dados)
            conexao_aberta.commit()
            print(f"{nome} cadastrado com sucesso!")
        except Error as erro:
            print(f"erro ao cadastrar : {erro}")
            return None
def cadastrar_bilheteria():
    """inserir novas atrações no parque"""

    conexao_aberta = connectar_banco()
    if conexao_aberta:
        cursor = conexao_aberta.cursor()
        visitante = input("nome do visitante: ")
        valor = input("valor a pagar: ")
        sql = "INSERT INTO bilheteria (visitante, valor) VALUES (%s,%s)"
        dados = (visitante, valor)
        try:
            cursor.execute(sql, dados)
            conexao_aberta.commit()
            print(f"{visitante} cadastrado com sucesso!")
        except Error as erro:
            print(f"erro ao cadastrar : {erro}")
        finally:
            cursor.close()
            conexao_aberta.close()


def listar_atracoes():
    """listar atraçoes"""
    conexao = connectar_banco()
    if conexao:
        cursor = conexao.cursor()
        sql = "SELECT nome, status FROM atracoes"
    try:
        cursor.execute(sql)
        resultados = cursor.fetchall()
        if not resultados:
            print("Nenhum resultado encontrado")
        else:
            for atracao in resultados:
                print(f"{atracao[0]} - {atracao[1]}")
    except Error as erro:
        print(f"Erro ao consultar: {erro} ")

def listar_bilheteria():
    """listar atraçoes"""
    conexao = connectar_banco()
    if conexao:
        cursor = conexao.cursor()
        sql = "SELECT visitante, valor FROM bilheteria"
    try:
        cursor.execute(sql)
        resultados = cursor.fetchall()
        if not resultados:
            print("Nenhum resultado encontrado")
        else:
            for bilheteria in resultados:
                print(f"{bilheteria[0]} - {bilheteria[1]}")
    except Error as erro:
        print(f"Erro ao consultar: {erro} ")

def listar_atracoes_by_status():
    """busca e listar atracoes pelo status"""
    conexao = connectar_banco()
    if conexao:
        cursor = conexao.cursor()
        # funcionando, manutenção, interditado, auditoria 
        status_busca = input("digite o status: ")
        # consultar sql
        sql = " SELECT nome, status FROM atracoes where status = %s"
        dados = (status_busca,)
        try: 
            cursor.execute(sql, dados)
            resultados = cursor.fetchall()
            if not resultados:
                print(f"Nenhuma atração com esse status")
            else:
                for atracao in resultados:
                    print(f"Atração: {atracao[0]}")
                
        except Error as erro:
            print(f"Erro ao  buscar: {erro}")
        finally:
            cursor.close()
            conexao.close()

def apagar_atracao ():
    """apagar atrção pelo nome"""
    conexao = connectar_banco()
    if conexao:
        cursor = conexao.cursor()
        nome_atracao = input("Digite o nome da atração: ")
        sql = "DELETE FROM atracoes where nome = %s"
        dados = (nome_atracao,)
        try:
            cursor.execute(sql, dados)
            linhas = cursor.rowcount
            if linhas == 0:
                print(f"não há registros com nome {nome_atracao}")
            else:
                confirmacao = input("Tem certeza? s/n ")
                if confirmacao == 's':
                    conexao.commit()
                    print(f"{nome_atracao} excluida")
                else:
                    conexao.rollback()
                    print("Ação cancelada")

        except Error as erro:
            print(f"Erro ao apagar: {erro}")
        finally:
            cursor.close()
            conexao.close()

def apagar_bilheteria ():
    """apagar atrção pelo nome"""
    conexao = connectar_banco()
    if conexao:
        cursor = conexao.cursor()
        nome_bilheteria = input("Digite o nome do visitante: ")
        sql = "DELETE FROM bilheteria where visitante = %s"
        dados = (nome_bilheteria,)
        try:
            cursor.execute(sql, dados)
            linhas = cursor.rowcount
            if linhas == 0:
                print(f"não há registros com nome {nome_bilheteria}")
            else:
                confirmacao = input("Tem certeza? s/n ")
                if confirmacao == 's':
                    conexao.commit()
                    print(f"{nome_bilheteria} excluida")
                else:

                    conexao.rollback()
                    print("Ação cancelada")

        except Error as erro:
            print(f"Erro ao apagar: {erro}")
        finally:
            cursor.close()
            conexao.close()




while True :
    opcao = input("Escolha  uma Opção: ")
    match opcao:
        case '1': # cadastrar atração
            cadastrar_atracao()
        case '2': #cadastrar bilhete
            cadastrar_bilheteria()
        case '3': # listar todos
            listar_atracoes()
        case '4': # listar por status
            listar_atracoes_by_status()
        case '5':
            listar_bilheteria()
        case '6':
            apagar_atracao()
        case '7':
            apagar_bilheteria()
        case '8':
            lucro_total()
        case'0':            
            break


#cadastrar_atracao()
#cadastrar_bilheteria()
#listar_atracoes()
#listar_bilheteria()