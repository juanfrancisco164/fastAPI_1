from fastapi import FastAPI, status
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import os
import requests
from pydantic import BaseModel


app = FastAPI()

static dir = Path("./static")
app.mount("/static", StaticFiles(directory=static_dir), name="static")

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

@app.post("/provincias/personas")
async def get_personas_fisicas_data(provincia88: ProvinciaClass):
    pProv = provincia88.provincia
    params = {
        "outFields": "Personas_fisicas_2017,Personas_fisicas_2016,Personas_fisicas_2015,Personas_fisicas_2014,Personas_fisicas_2013,Personas_fisicas_2012,Personas_fisicas_2011,Personas_fisicas_2010,Personas_fisicas_2009,Personas_fisicas_2008,Personas_fisicas_2007,Personas_fisicas_2006,Personas_fisicas_2005,Personas_fisicas_2004,Personas_fisicas_2003,Personas_fisicas_2002,Personas_fisicas_2001,Personas_fisicas_2000,Personas_fisicas_1999",
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