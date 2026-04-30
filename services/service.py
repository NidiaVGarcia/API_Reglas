from datetime import datetime, timedelta
from logger.logger import Logger

class Service:

    def __init__(self, db_conn):
        self.logger = Logger()
        self.db_conn = db_conn

    def Control_SII(self):
        
        try:
            reglas_collection = self.db_conn.db['reglas2025']
            projection = {
                "_id": 1,
                "ip_ori": 1,
                "ip_dest": 1,
                "puerto": 1,
                "memo_atn": 1
            }
            documents = list(reglas_collection.find({}, projection))
            reglassii2025 = [
                {
                    "_id": str(doc["_id"]),
                    "ip_ori": doc.get("ip_ori", ""),
                    "ip_dest": doc.get("ip_dest", ""),
                    "puerto": doc.get("puerto", ""),
                    "memo_atn": doc.get("memo_atn", "")
                }
                for doc in documents
            ]
            return reglassii2025, 200
        except Exception as e:
            self.logger.error(f"Error al obtener datos de la colección 'reglas2025': {e}")
            return {"error": "Error al obtener datos de Reglas SII 2025"}, 500
        
    
        
    
        
    