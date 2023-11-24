from fastapi import FastAPI
import uvicorn


app = FastAPI()

@app.get("/")
async def root():
    return"Probando lo básico de fastAPI"

print()
if __name__ == "__main__":
    print("-> Inicio integrado de servicio web")
    uvicorn.run(app, host="127.0.0.1", port=8000)
else:
    print("=> Iniciado desde el servidor web")
    print("   Módulo python iniciado:", __name__)