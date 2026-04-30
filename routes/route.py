from flask import Blueprint, request, jsonify
from datetime import datetime, timedelta
from logger.logger import Logger

class FileGeneratorRoute(Blueprint):

    def __init__(self, service):
        super().__init__("file_generator", __name__)
        self.logger = Logger()
        self.service = service
        self.register_routes()

    def register_routes(self): 
        self.route("/api/v1/reglas2025Get", methods=["POST"])(self.reglas2025Get)        
        self.route("/api/healthcheck", methods=["GET"])(self.healthcheck)

    def fetch_request_data(self):
        """Function to fetch the request data"""
        try:
            request_data = request.json
            if not request_data:
                return 400, "Invalid data", None
            return 200, None, request_data
        except Exception as e:
            self.logger.error(f"Error fetching request data: {e}")
            return 500, "Error fetching request data", None
        
         
        
    def reglas2025Get(self):
        """Endpoint para obtener los datos de Reglas de SII 2025"""
        try:
            reglas2025_data, status_code = self.service.Control_SII()
            self.logger.debug("Datos obtenidos de Reglas SII 2025: ")
            self.logger.debug(reglas2025_data)
            return jsonify(reglas2025_data), status_code
        except Exception as e:
            self.logger.error(f"Error en reglas2025_data: {e}")
            return jsonify({"error": "Internal server error"}), 500
    
                
    def healthcheck(self):
        """Function to check the health of the services API inside the docker container"""
        return jsonify({"status": "Up"}), 200