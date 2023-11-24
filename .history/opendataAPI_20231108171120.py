from fastapi import FastAPI, HTTPException
import json
import uvicorn
import os

dir = os.path.dirname(__file__)

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "aaaa"}

@app.get("/prueba")
async def getPrueba():
    try:
        with open("cartografia_1.json", "r") as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="El archivo no se encontró")
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error interno del servidor")

@app.get("/{lengua_publicacion}")
async def getPrueba(lengua_publicacion):
    path = os.path.join(dir, "{filename}.json".format(filename = cartografia_1))
    
    if os.path.exists(path):
        file = open(path)
        return json.load(file)
    
    return {"Error ": "File not found"}
    
    
# -------------------------------------------------------------------------------------------------------- #
print()
if __name__ == "__main__":
    print("-> Inicio integrado de servicio web")
    uvicorn.run(app, host="127.0.0.1", port=8000)
else:
    print("=> Iniciado desde el servidor web")
    print("   Módulo python iniciado:", __name__)


# @app.get("/{título}")
# async def getPrueba(título):
#     file = open('{filename}.json'.format(filename = título))
#     return json.load(file)


# print()
# if __name__ == "__main__":
#     print("-> Inicio integrado de servicio web")
#     uvicorn.run(app, host="127.0.0.1", port=8000)
# else:
#     print("=> Iniciado desde el servidor web")
#     print("   Módulo python iniciado:", __name__)