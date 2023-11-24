from fastapi import FastAPI
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import os
import requests
from pydantic import BaseModel


app = FastAPI()

origins = ["*"]

class ProvinciaClass (BaseModel):
    provincia: str

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

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


@app.post("/provincias")
async def root(provincia88: ProvinciaClass):
    pProv = provincia88.provincia
    params = {
        "outFields": "*",
        "where": f"Texto = '{pProv}'",
        "f": "json",
        "outSR": "4326"
    }
    response = requests.get(API_URL, params = params)
    data = response.json()
    
    features = data["features"]
    
    return features

@app.post("/provincias/sociedades_anonimas")
async def get_sociedades_anonimas_data(provincia88: ProvinciaClass):
    pProv = provincia88.provincia
    año_seleccionado = "2017"  # Puedes cambiar esto según el año seleccionado
    params = {
        "outFields": f"Texto,Sociedad_Anonima_{año_seleccionado}",
        "where": f"Texto = '{pProv}'",
        "f": "json",
        "outSR": "4326"
    }
    response = requests.get(API_URL, params=params)
    data = response.json()
    features = data["features"]
    return features

@app.post("/provincias/sociedades_limitada")
async def get_sociedades_limitada_data(provincia88: ProvinciaClass):
    pProv = provincia88.provincia
    año_seleccionado = "2017"  # Puedes cambiar esto según el año seleccionado
    params = {
        "outFields": f"Texto,Sociedades_responsabilidad_limi_{año_seleccionado}",
        "where": f"Texto = '{pProv}'",
        "f": "json",
        "outSR": "4326"
    }
    response = requests.get(API_URL, params=params)
    data = response.json()
    features = data["features"]
    return features

# -------------------------------------------------------------------------------------------------------- #
dir = os.path.dirname(__file__)

print()
if __name__ == "__main__":
    print("-> Inicio integrado de servicio web")
    uvicorn.run(app, host="127.0.0.1", port=8000)
else:
    print("=> Iniciado desde el servidor web")
    print("   Módulo python iniciado:", __name__)