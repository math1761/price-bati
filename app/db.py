import os
import firebase_admin
from firebase_admin import credentials, firestore

def get_db():
    """
    Initialize Firebase App (if not already) and return the Firestore client.
    """
    if not firebase_admin._apps:
        # You can store the path to credentials in an env variable for production
        cred_path = os.environ.get("FIREBASE_CREDENTIALS", "firebase_credentials.json")
        cred = credentials.Certificate(cred_path)
        firebase_admin.initialize_app(cred)
    return firestore.client()
