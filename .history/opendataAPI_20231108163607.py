from fastapi import FastAPI
from fastapi.responses import JSONResponse
import uvicorn
import json

app = FastAPI()

@app.get("/")
async def root():
    return {"message" : "aaaa"}

@app.get("/prueba")
async def getPrueba():
    file = open("cartografia_1.json")
    return json.load(file)

@app.get("/{título}")
async def getPrueba({título}):
    file = open("{filename}.json".format{filename = título})
    return json.load(file)


print()
if __name__ == "__main__":
    print("-> Inicio integrado de servicio web")
    uvicorn.run(app, host="127.0.0.1", port=8000)
else:
    print("=> Iniciado desde el servidor web")
    print("   Módulo python iniciado:", __name__)