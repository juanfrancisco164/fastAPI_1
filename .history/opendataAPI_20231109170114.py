from fastapi import FastAPI, HTTPException
import json
import uvicorn
import os

dir = os.path.dirname(__file__)

app = FastAPI()

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