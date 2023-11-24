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
    allow_origins=["*"],
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
    params = {
        "outFields": "Sociedad_Anonima_2017,Sociedad_Anonima_2016,Sociedad_Anonima_2015,Sociedad_Anonima_2014,Sociedad_Anonima_2013,Sociedad_Anonima_2012,Sociedad_Anonima_2011,Sociedad_Anonima_2010,Sociedad_Anonima_2009,Sociedad_Anonima_2008,Sociedad_Anonima_2007,Sociedad_Anonima_2006,Sociedad_Anonima_2005,Sociedad_Anonima_2004,Sociedad_Anonima_2003,Sociedad_Anonima_2002,Sociedad_Anonima_2001,Sociedad_Anonima_2000,Sociedad_Anonima_1999",
        "where": f"Texto = '{pProv}'",
        "f": "json",
        "outSR": "4326"
    }
    response = requests.get(API_URL, params=params)
    data = response.json()
    features = data["features"]
    return features

import logging

@app.post("/provincias/sociedades_limitada")
async def get_sociedades_limitada_data(provincia88: ProvinciaClass):
    pProv = provincia88.provincia
    params = {
        "outFields": "Sociedades_responsabilidad_limi_1,Sociedades_responsabilidad_limi_2,Sociedades_responsabilidad_limi_3,Sociedades_responsabilidad_limi_4,Sociedades_responsabilidad_limi_5,Sociedades_responsabilidad_limi_6,Sociedades_responsabilidad_limi_7,Sociedades_responsabilidad_limi_8,Sociedades_responsabilidad_limi_9,Sociedades_responsabilidad_limi_10,Sociedades_responsabilidad_limi_11,Sociedades_responsabilidad_limi_12,Sociedades_responsabilidad_limi_13,Sociedades_responsabilidad_limi_14,Sociedades_responsabilidad_limi_15,Sociedades_responsabilidad_limi_16,Sociedades_responsabilidad_limi_17,Sociedades_responsabilidad_limi_18",
        "where": f"Texto = '{pProv}'",
        "f": "json",
        "outSR": "4326"
    }
    try:
        response = requests.get(API_URL, params=params)
        response.raise_for_status()  # Lanzar una excepción para errores HTTP
        data = response.json()
        features = data["features"]
        return features
    except Exception as e:
        logging.error(f"Error en la solicitud a /provincias/sociedades_limitada: {e}")
        return {"error": "Error en el servidor FastAPI"}


# -------------------------------------------------------------------------------------------------------- #
dir = os.path.dirname(__file__)

print()
if __name__ == "__main__":
    print("-> Inicio integrado de servicio web")
    uvicorn.run(app, host="127.0.0.1", port=8000)
else:
    print("=> Iniciado desde el servidor web")
    print("   Módulo python iniciado:", __name__)