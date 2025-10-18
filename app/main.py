from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"mensaje": "API en Render funcionando 🚀"}

@app.post("/predict")
def predict(data: dict):
    # Aquí luego integrarás el modelo de tus compañeros
    return {"prediccion": "modelo aún no cargado", "data_recibida": data}