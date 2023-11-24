from fastapi import FastAPI
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.middlewre.cors import middlewre
import uvicorn
import os
import requests


app = FastAPI()

origins = ["*"]

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
    with open("FrontEnd/empresasActivas.html", "r") as file:
        html_content = file.read()
    params = {
        "outFields": "*",
        "where": "1=1",
        "f": "geojson"
    }
    response = requests.get(API_URL, params = params)
    data = response.json()
    
    features = data["features"]
    
    return features, HTMLResponse(content=html_content)


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

# -------------------------------------------------------------------------------------------------------- #
@app.get("/static/styles.css")
async def get_css():
    return FileResponse("FrontEnd/empresasActivas.css", media_type="text/css")
    
# -------------------------------------------------------------------------------------------------------- #
dir = os.path.dirname(__file__)

print()
if __name__ == "__main__":
    print("-> Inicio integrado de servicio web")
    uvicorn.run(app, host="127.0.0.1", port=8000)
else:
    print("=> Iniciado desde el servidor web")
    print("   Módulo python iniciado:", __name__)