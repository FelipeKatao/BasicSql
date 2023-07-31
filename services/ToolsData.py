from services.DataBaseTrataments import DatabaseImports
from services.configBase import ConfigBasicSql

class ToolsData:
    dtimp = DatabaseImports()
    cf = ConfigBasicSql()
    def ReturnAllTables(self,TreeView):
        for i in TreeView.get_children():
            TreeView.delete(i)
        CountTables = 0
        ListOfTables = self.dtimp.ReturnAllTables(self.cf.GetCon())
        ListOfTables =ListOfTables.split(",")
        ListTables_Result = list()
        ColumTables_result = list()
        idColum = 0
        for ListTables in ListOfTables:
            v = ListTables.replace("[","").replace("]","").replace("(","").replace("'","").replace(")","").replace(" ","")
            CountTables+=1
            if(v!=""):
                ListTables_Result.append(v)
                TreeView.insert('','end',v,text=v)
                #tree_tables.item(v,open=True)
                isopen = TreeView.item(v,'open')
                ColumnsOfTable = self.dtimp.ReturnAllColumnsTables(self.cf.GetCon(),v).split(",")
        
                for Colums in ColumnsOfTable:
                    val = Colums.replace("[","").replace("]","").replace("(","").replace("'","").replace(")","")
                    idColum+=1
                    if val!="":
                        ColumTables_result.append(val)
                        TreeView.insert(parent=v,index='end',iid=idColum,text=val)
                ColumTables_result.clear()