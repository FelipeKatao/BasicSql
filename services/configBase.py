
class ConfigBasicSql:
    def VerifyCon(self):
        filename = "./Configs/BaseConfig.txt"
        fileList =list()
        fileopen = open(filename,"r")
        indice =0
        for file in fileopen:
            fileList.append(file)
            if(str(file).find('DATABASE_SET')):
                break
            indice+=1
        fileopen.close()
        return fileList[indice]
    def GetCon(self):
        ConfGets = self.VerifyCon()
        ConfGets = str(ConfGets).replace("   ","").replace("\n","")
        ConfGets = str(ConfGets).split(",")
        return ConfGets
    
    def CreateConfig(self,ConfigBase):
        file = open("./Configs/BaseConfig.txt","r")
        FileRead = file.readlines() 
        IndexFile = 0
        for ListConfig in FileRead:
            print(ListConfig.strip())
            if(str(ListConfig) == "DATABASE_SET :\n"):
                break
            IndexFile+=1
        file.close()
        fileWriter = open("./Configs/BaseConfig.txt",'w')
        FileRead[IndexFile+1] = ConfigBase+"\n"
        fileWriter.writelines(FileRead)
        fileWriter.close()

    def CreateNewUser(self,Userbase):
        file = open("./Configs/BaseConfig.txt","r")
        FileRead = file.readlines() 
        IndexFile = 0
        for ListConfig in FileRead:
            print(ListConfig.strip())
            if(str(ListConfig) == "USER :\n"):
                break
            IndexFile+=1
        file.close()
        fileWriter = open("./Configs/BaseConfig.txt",'w')
        FileRead[IndexFile+1] = Userbase+"\n"
        fileWriter.writelines(FileRead)
        fileWriter.close()       
        