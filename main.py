import pickle

import numpy as np
from fastapi import FastAPI
from pydantic import BaseModel
import joblib  # ou pickle pour charger votre modèle

# Initialisez l'application FastAPI
app = FastAPI()


class InputData(BaseModel):
    Infrarouge: int
    Rouge: int
    Temperature: float


# Chargez votre modèle ML
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(base_dir, "app/model/dialu.pkl")
with open(model_path, "rb") as file:
    model = pickle.load(file)


# Endpoint pour faire une prédiction
@app.post("/predict/")
async def predict(data: InputData):
    features = [
        data.Infrarouge,
        data.Rouge,
        data.Temperature  # conserve la valeur float
    ]
    prediction = model.predict([features])[0]
    return {"result": int(prediction)}
