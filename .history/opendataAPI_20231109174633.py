from fastapi import FastAPI, HTTPException
import uvicorn
import os

dir = os.path.dirname(__file__)

app = FastAPI()

API_URL = "https://services1.arcgis.com/nCKYwcSONQTkPA4K/arcgis/rest/services/Empresas_activas_por_provincias_WFL1/FeatureServer/0/query?outFields=*&where=1%3D1&f=geojson"


@app.get("/")
async def root():
    return {"message": "aaaa"}
    
    
# -------------------------------------------------------------------------------------------------------- #
print()
if __name__ == "__main__":
    print("-> Inicio integrado de servicio web")
    uvicorn.run(app, host="127.0.0.1", port=8000)
else:
    print("=> Iniciado desde el servidor web")
    print("   Módulo python iniciado:", __name__)