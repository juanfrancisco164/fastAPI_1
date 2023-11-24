from fastapi import FastAPI, HTTPException
import uvicorn
import os
import requests

dir = os.path.dirname(__file__)

app = FastAPI()

API_URL = "https://services1.arcgis.com/nCKYwcSONQTkPA4K/arcgis/rest/services/Empresas_activas_por_provincias_WFL1/FeatureServer/0/query"

@app.get("/")
async def root():
    params = {
        "outFields": "*",
        "where": "1=1",
        "f": "geojson"
    }
    response = requests.get(API_URL, params = params)
    data = response.json()
    
    features = data["features"]
    
    return features


@app.get("/provincias")
async def root():
    params = {
        "outFields": "*",
        "where": "Texto = 'Granada'",
        "f": "json",
        "outSR": "4326"
    }
    response = requests.get(API_URL, params = params)
    data = response.json()
    
    features = data["features"]
    
    return features
    
@app.get("/sociedades_cooporativas")
async def root():
    params = {
        "outFields": "*",
        "where": " (Sociedades_Cooperativas_1999 = 0 OR Sociedades_Cooperativas_1999 = 50000) ",
        "f": "json",
        "outSR": "4326"
    }
    response = requests.get(API_URL, params = params)
    data = response.json()
    
    features = data["features"]
    
    return features
    
# -------------------------------------------------------------------------------------------------------- #
print()
if __name__ == "__main__":
    print("-> Inicio integrado de servicio web")
    uvicorn.run(app, host="127.0.0.1", port=8000)
else:
    print("=> Iniciado desde el servidor web")
    print("   Módulo python iniciado:", __name__)