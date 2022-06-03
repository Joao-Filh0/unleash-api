import firebase_admin
from firebase_admin import firestore, credentials


class FirestoreDb:
    def __init__(self):
        cred = credentials.Certificate("unleash-future-toggle.json")
        firebase_admin.initialize_app(credential=cred)
        self.db = firestore.client()
        
    def read_db(self):
        dogs = []
        colec = self.db.collection("Features").get()
        for doc in colec:
            dogs.append(doc.to_dict())
        return  dogs
    def write_db(self,data):
        self.db.collection("Features").add(data)
    def update_dogs_db(self,id,data):
        self.db.collection("Features").document(id).update(data)