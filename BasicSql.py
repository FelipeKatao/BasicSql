import tkinter 
import welcomeScreen
from services.configBase import ConfigBasicSql
from services.DataBaseTrataments import DatabaseImports
from services.QueryFiles import Querys
from services.ToolsData import ToolsData
from tkinter import TclError,ttk
import tkinter as tk
from tkinter import Menu

m = tkinter.Tk()
Welc =welcomeScreen.Welcome()
cf = ConfigBasicSql()
dtimp = DatabaseImports()
qy = Querys()
Td = ToolsData()

#==================================================
#Configurações da Janela como padrão 
#==================================================

m.title("Basic Sql 0.0.1")
m.configure(bg='white')
m.state("zoomed")
m.iconbitmap(True,'./img/officedatabase_103574.ico')

#==================================================


#================================================
#Funcoes Bases 
#================================================
Create = False
def FuncA():
    if Create ==False:
        tree_tables.grid_forget()
        tree_tables_x = ttk.Treeview(frame_Tools,height=80)
        tree_tables_x.grid(column=0,row=0,sticky=tk.NS)
        Td.ReturnAllTables(tree_tables_x)
        Create == True
    else:
        tree_tables_x.grid_forget()
        tree_tables_x = ttk.Treeview(frame_Tools,height=80)
        tree_tables_x.grid(column=0,row=0,sticky=tk.NS)
        Td.ReturnAllTables(tree_tables_x)

def ExecuteSql():
    SqlQuery = text_sql_box.get("1.0",tk.END)
    print(SqlQuery)
    text_result_box.insert(tk.END,"\n Resultado: "+dtimp.ExecuteQuery(cf.GetCon(),str(SqlQuery)))

def LimparSql():
    text_sql_box.delete('1.0',tk.END)
    text_result_box.delete('1.0',tk.END)

def SalvarQuery():
    qy.SaveQuery(text_sql_box.get("1.0",tk.END))
    

#================================================

#==================================================
# Criação de Menu
#==================================================
menu = Menu(m)

fileMenu_ = tk.Menu(menu)
fileMenu_.add_command(label="Salvar Query",command=SalvarQuery)
menu.add_cascade(label="Arquivo",menu=fileMenu_)

filemenu = tk.Menu(menu)
filemenu.add_command(label="Executar", command=ExecuteSql)
filemenu.add_command(label="Limpar Sql",command=LimparSql)
menu.add_cascade(label="Sql",menu=filemenu)

ToolsMenu = tk.Menu(menu)
ToolsMenu.add_command(label="Atualizar Base",command=FuncA)
ToolsMenu.add_command(label="Obter Colunas..")
menu.add_cascade(label='View',menu=ToolsMenu)

UserBaseMenu = tk.Menu(menu)
UserBaseMenu.add_command(label="Apagar Configuracao Base")
UserBaseMenu.add_command(label="Modificar usuario")
UserBaseMenu.add_separator()
UserBaseMenu.add_command(label="Verificar Usuario")
menu.add_cascade(label="DataBase",menu=UserBaseMenu)

#==================================================
# Elementos em tela
#==================================================

frame_Tools = tk.Frame(m,highlightthickness=3,width=100,height=900)
frame_Propries = tk.Frame(m,highlightthickness=3,width=200,height=900)

tab_control = ttk.Notebook(m,height=900,width=1100)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)

tab_control.add(tab1,text="SQl Editor")
tab_control.add(tab2,text="Resultados")
Frame_textSql = tk.Canvas(tab1,bg='yellow')
Frame_textSql.grid(row=0,column=0,sticky="news")

Frame_resultText = tk.Canvas(tab2,bg='black')
Frame_textSql.grid(row=0,column=0,sticky='news')



vsb = tk.Scrollbar(tab1, orient="vertical", command=Frame_textSql.yview)
vsb.grid(row=0, column=1, sticky='ns')
text_sql_box = tk.Text(Frame_textSql,height=43,width=150)
text_sql_box.configure(font=("Arial",10,"normal"))
Frame_textSql.configure(yscrollcommand=vsb.set)
tree_tables = ttk.Treeview(frame_Tools,height=80)

text_result_box = tk.Text(tab2,height=30,width=150)
text_result_box.configure(background='black',foreground='white',font=("Arial",10,"normal"))

#================================================
#Funções da pagina  
#================================================ 

## TOOL DE TABELAS
if(cf.VerifyCon()!='\n'):
    ListOfTables = dtimp.ReturnAllTables(cf.GetCon())
    CountTables = 0
    ListOfTables =ListOfTables.split(",")
    ListTables_Result = list()
    ColumTables_result = list()
    idColum = 0
    for ListTables in ListOfTables:
        v = ListTables.replace("[","").replace("]","").replace("(","").replace("'","").replace(")","").replace(" ","")
        CountTables+=1
        if(v!=""):
            ListTables_Result.append(v)
            tree_tables.insert('','end',v,text=v)
            #tree_tables.item(v,open=True)
            isopen = tree_tables.item(v,'open')
            ColumnsOfTable = dtimp.ReturnAllColumnsTables(cf.GetCon(),v).split(",")
            
            for Colums in ColumnsOfTable:
                val = Colums.replace("[","").replace("]","").replace("(","").replace("'","").replace(")","")
                idColum+=1
                if val!="":
                    ColumTables_result.append(val)
                    tree_tables.insert(parent=v,index='end',iid=idColum,text=val)
            ColumTables_result.clear()

## END TOOL DE TABELAS

## APPLY QUERY EDITOR 
text_sql_box.insert(tk.END,qy.LoadQueryDefault())
text_result_box.insert(tk.END,"MySql 1.0.1 -DataBase connected")
## END APPLY QUERY EDITOR 

#===============================================
# COMMAND LISTERNER
#===============================================



#================================================
#Pack Elements
#================================================
m.config(menu=menu)
frame_Tools.grid(column=0,row=0,sticky=tk.N)


tab_control.grid(column=1,row=0,sticky=tk.N)
text_sql_box.grid(column=0,row=0,sticky=tk.NE)
Frame_textSql.config(scrollregion=Frame_textSql.bbox("all"))
Frame_resultText.config(scrollregion=Frame_resultText.bbox("all"))
text_result_box.grid(column=0,row=0,sticky=tk.NE)
frame_Propries.grid(column=2,row=0,sticky=tk.N)
tree_tables.grid(column=0,row=0,sticky=tk.NS)
if(cf.VerifyCon()=='\n'):
    Welc.Screen(m)
m.mainloop()

