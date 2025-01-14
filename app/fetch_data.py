import firebase_admin
from firebase_admin import credentials, firestore
import pandas as pd

# Initialize Firebase Admin SDK
cred = credentials.Certificate("firebase_credentials.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

def fetch_data(collection_name: str) -> pd.DataFrame:
    """
    Fetch all documents from a Firestore collection and return as a Pandas DataFrame.
    """
    docs = db.collection(collection_name).stream()
    data = []

    for doc in docs:
        doc_dict = doc.to_dict()
        data.append(doc_dict)

    df = pd.DataFrame(data)
    return df
