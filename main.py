from app.fetch_data import fetch_data
from app.preprocess import preprocess_data, save_preprocessors
from app.train_model import create_model, train_model
from app.save_model import save_model
from fastapi import FastAPI, HTTPException
from typing import List
from app.db import get_db
from app.schemas import ProjectItem
from app.predict import predict
from fastapi.openapi.utils import get_openapi
from faker import Faker
import random
import uuid

app = FastAPI(
    title="Price Bati API",
    description="API for building price prediction using Firestore data.",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

fake = Faker()

@app.get("/items", response_model=List[ProjectItem])
def get_items():
    """
    Retrieve all items (projects) from the 'projects' collection in Firestore.
    """
    db = get_db()
    try:
        docs = db.collection("projects").stream()
        items = []
        for doc in docs:
            data = doc.to_dict()
            # Convert Firestore doc to ProjectItem
            item = ProjectItem(**data)
            items.append(item)
        return items

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/seed", response_model=dict)
def seed_data(num_samples: int = 1000):
    """
    Insert a large number of random sample data into the 'projects' collection.
    """
    db = get_db()
    try:
        type_projets = ["Renovation", "Neuf", "Extension", "Restauration", "Aménagement"]
        sample_items = []

        for _ in range(num_samples):
            item = ProjectItem(
                id=str(uuid.uuid4()),
                type_projet=random.choice(type_projets),
                surface_m2=round(random.uniform(20, 500), 2),  # Surface between 20 and 500 m²
                cout_total=round(random.uniform(5000, 500000), 2)  # Cost between 5000 and 500000
            )
            sample_items.append(item)

            # Insert each item into Firestore
            doc_ref = db.collection("projects").document(item.id)
            doc_ref.set(item.dict())

        return {"status": "ok", "inserted_count": len(sample_items)}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/predict/{project_id}", response_model=float)
def predict_cost(project_id: str):
    """
    Predict the cost of a project given its ID.
    """
    db = get_db()
    try:
        doc_ref = db.collection("projects").document(project_id)
        doc = doc_ref.get()
        if doc.exists:
            data = doc.to_dict()
            surface_m2 = data["surface_m2"]
            type_projet = data["type_projet"]
            predicted_cost = predict(surface_m2, type_projet)
            return predicted_cost
        else:
            raise HTTPException(status_code=404, detail="Project not found")

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.get("/train", response_model=str)
def train():
    try:
        # Step 1: Fetch the data
        collection_name = "projects"
        df = fetch_data(collection_name)

        # Step 2: Preprocess the data
        train_dataset, test_dataset, encoder, scaler = preprocess_data(df)

        input_shape = train_dataset.element_spec[0].shape[1]
        model = create_model(input_shape)
        train_model(model, train_dataset, test_dataset, epochs=50)

        save_model(model, filename="saved_model")
        save_preprocessors(encoder, scaler)
        return "Model trained successfully!"
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))