import sqlite3
import os


class Config:
    def __init__(self) -> None:
        super().__init__()
        
        db_path = "content/users.db"
        self.db_state = False
        
        
        if os.path.isfile(db_path):
            self.db_state = True
        
        
    def returnDBStatus(self) -> bool:
        return self.db_state
    
    def returnConfigStats(self) -> tuple:
        if os.path.isfile("content/config.cfg"):
            with open("content/config.cfg", 'r') as config:
                config = config.read().split("\n")
                username = config[0]
                email = config[1]
            
            return {username, email}
        
        
    def returnConfigProjectName(self) -> str:
        if os.path.isfile("content/config.cfg"):
            with open("content/config.cfg", 'r') as config:
                try:
                    config = config.read().split("\n")
                    projectName = config[2]
            
                    return projectName
                
                except:
                    return ''
                
    def writeCurrentProject(self, currentProjectTitle: str):
        username, email = self.returnConfigStats()
        
        with open('content/config.cfg', 'w') as config:
                config.write(f"{username}\n{email}\n{currentProjectTitle}")
                config.close()