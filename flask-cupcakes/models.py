"""Models for Cupcake app."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

class Cupcake(db.Model):
    __tablename__ = "cupcakes"

    def __repr__(self):
        cupcake = self
        return f"<Cupcake {cupcake.id} {cupcake.flavor} {cupcake.size} {cupcake.rating} {cupcake.image}"
    

    id = db.Column(db.Integer,primary_key = True, autoincrement = True)
    flavor = db.Column(db.String, nullable = False)
    size = db.Column(db.String, nullable = False)
    rating = db.Column(db.Float, nullable =False)
    image = db.Column(db.String, nullable = False, default = "https://tinyurl.com/demo-cupcake")