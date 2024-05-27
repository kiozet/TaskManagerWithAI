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
        with open("content/config.cfg", 'r') as config:
            config = config.read().split("\n")
            username = config[0]
            email = config[1]
        
        return {username, email}