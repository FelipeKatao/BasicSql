
class Querys:
    def LoadQueryDefault(self):
        filename = "./Query.sql"
        fileList =list()
        fileopen = open(filename,"r")
        TextReturn = ""
        for file in fileopen:
            TextReturn+=file
        return TextReturn
    
    def SaveQuery(self,Value):
        filename  = "./Query.sql"
        file_open = open(filename,'w')
        Value = Value+"\n"
        ListSaved = str(Value).split("\n")
        print(ListSaved)
        Indexador = 0
        for list in ListSaved:
            ListSaved[Indexador] =list+"\n"
            Indexador+=1
        file_open.writelines(ListSaved)
        file_open.close()