import mysql.connector
import tkinter 

filename = "./consulta.sql"
fileList = list()
QUERY_sql =""
Result = ""
Result02 = ""

fileopen = open(filename,"r")
for file in fileopen:
    fileList.append(file.split('`'))
    QUERY_sql+=file+" "
print(QUERY_sql)
fileopen.close()

MeuBd = mysql.connector.connect( host ="db4free.net",user ="usuario_0_poli",password = "9090ola1",database = "teste_9")

cursor = MeuBd.cursor()
cursor.execute(QUERY_sql)

try:
    MeuBd.commit()
    print("Query executada com sucesso")
except:

    Result = str(cursor.fetchall())



print("==============================================")
#cursor.execute("show COLUMNS from Test012;")
print(fileList)
indice_procura = 0
for procurar in fileList:
    if str(procurar).find("SELECT"):
        break
    indice_procura+=1
print(Result)
Cabecalho = fileList[indice_procura][1]
print(Cabecalho)
cursor.execute("show COLUMNS from "+Cabecalho)
Result02 = str(cursor.fetchall())
# Test012;
print(Result02)
print("==============================================")