import mysql.connector

class DatabaseImports:

    def ReturnAllTables(self,params):
        con = mysql.connector.connect( host =params[0],user =params[1],password = params[3],database = params[2])
        cursor = con.cursor()
        cursor.execute("show tables")
        Result = str(cursor.fetchall())
        con.close()
        return Result
    
    def ReturnAllColumnsTables(self,params,Table):
        con = mysql.connector.connect( host =params[0],user =params[1],password = params[3],database = params[2])
        cursor = con.cursor()
        cursor.execute("select COLUMN_NAME from information_schema.COLUMNS where TABLE_NAME='"+Table+"'")
        Result = str(cursor.fetchall())
        con.close()
        return Result
    
    def ExecuteQuery(self,params,Query):
        con = mysql.connector.connect( host =params[0],user =params[1],password = params[3],database = params[2])
        cursor = con.cursor()
        try:
            cursor.execute(Query)
        except Exception as Ex:
            return "Sua query possui Erros: "+str(Ex)
        try:
            con.commit()
            con.close()
            return "Query executada com sucesso!!"
        except Exception as ea:
            try:
                Result = str(cursor.fetchall())
                con.close()
                return Result    
            except Exception as e:
                return "Sua query possui erros de Sintaxe Erro: \n"+str(e)
