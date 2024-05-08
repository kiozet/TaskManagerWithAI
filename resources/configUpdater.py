import sqlite3


class Config:
    def __init__(self) -> None:
        super().__init__()
        
        try:
            self.db = sqlite3.connect("db.db")
            
        except:
            self.db = None
            
        self.returnDBStatus(self.db)
        
        
    def returnDBStatus(self, db) -> bool:
        if db == None: return False
        else: return True