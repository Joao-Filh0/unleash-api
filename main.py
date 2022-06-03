from flask import Flask,jsonify,request
from client import FirestoreDb



app = Flask(__name__)

firestore_db = FirestoreDb()

@app.route("/features/",methods =["GET"])
def get_features():
    list_features = firestore_db.read_db()
    
    return jsonify(list_features)

@app.route("/features/",methods =["POST"])
def post_features():
    r = request.get_json()
    id = r["featureName"]
    firestore_db.update_dogs_db(id,r)
    
    return jsonify(r)


app.run(debug=True)