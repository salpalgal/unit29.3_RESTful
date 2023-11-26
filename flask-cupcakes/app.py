"""Flask app for Cupcakes"""
from flask import Flask, render_template, request, redirect, jsonify
from models import Cupcake, db, connect_db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)

from flask_debugtoolbar import DebugToolbarExtension
app.config['SECRET_KEY'] = "SECRET!"
debug = DebugToolbarExtension(app)
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

def serialize(cupcake):
        return {
            "id": cupcake.id,
            "flavor": cupcake.flavor,
            "size": cupcake.size,
            "rating": cupcake.rating,
            "image": cupcake.image
        }

@app.route("/api/cupcakes", methods =["GET"])
def get_all_cupcakes():
    cupcakes = Cupcake.query.all()
    serialized = [serialize(cupcake) for cupcake in cupcakes]
    return jsonify(cupcakes=serialized)

@app.route("/api/cupcakes/<int:cupcake_id>", methods= ["GET"])
def get_cupcake(cupcake_id):
    cupcake = Cupcake.query.get_or_404(cupcake_id)
    serialized = serialize(cupcake)
    return jsonify(cupcake=serialized)

@app.route("/api/cupcakes", methods = ["POST"])
def post_cupcake():
    flavor = request.json["flavor"]
    size = request.json["size"]
    rating =  request.json["rating"]
    image =  request.json["image"]
    cupcake = Cupcake(flavor= flavor, size =size, rating = rating, image= image)
    db.session.add(cupcake)
    db.session.commit()
    serialized = serialize(cupcake)
    return (jsonify(cupcake=serialized), 201)